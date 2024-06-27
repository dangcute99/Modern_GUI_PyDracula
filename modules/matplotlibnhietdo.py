import sys
import os
import datetime
import pandas as pd
import socket
from playsound import playsound
import threading
from multiprocessing import Process
import numpy as np
from matplotlib.ticker import MultipleLocator
import mysql.connector
import matplotlib.pyplot as plt
from PySide6.QtCore import QTimer, Qt,QObject, Signal, QDateTime
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QApplication, QTableWidget,QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import pygame.mixer
from server import *
tram70 ="172.20.10.48"
tram45 ="172.20.10.01"
tram01 = "172.20.10.02"
tram48="172.20.10.4"
tram71="172.20.10.71"
tram76="172.20.10.76"
class MatplotlibCanvasNhietdo(FigureCanvas):
    dataReceived = Signal(str, float, float, float, float, float, float, float, float, float, float, float, float, float, float, datetime.datetime)

    def __init__(self):
        self.fignhietdo, self.ax = plt.subplots()
        super().__init__(self.fignhietdo)
        self.temperature = []
        self.time = []
        self.ax.set_xlabel('Thời gian')
        self.ax.set_ylabel('Nhiệt độ')
        self.ax.set_ylim(0, 50)
        self.data_count = 0
        self.nhietdo_lower = 20
        self.nhietdo_high = 25
        self.threshold_lines = []  # List to store references to threshold lines
        y_major_locator = MultipleLocator(5)
        self.ax.yaxis.set_major_locator(y_major_locator)

    def update_figureNhietdo(self, client_address, temperature, humidity, light,  voltage_dc1, voltage_dc2,
                                    voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low, dienap_high, current_time):
       if client_address == tram70:
            if nhietdo_lower is not None and nhietdo_lower != 0 and self.nhietdo_lower != nhietdo_lower:
                self.ax.axhline(self.nhietdo_lower, color='gray', linestyle='--')  # Draw dashed line for old lower threshold
                self.nhietdo_lower = float(nhietdo_lower)
            if nhietdo_high is not None and nhietdo_high != 0 and self.nhietdo_high != nhietdo_high:
                self.ax.axhline(self.nhietdo_high, color='gray', linestyle='--')  # Draw dashed line for old higher threshold
                self.nhietdo_high = float(nhietdo_high)

            current_time = datetime.datetime.now().strftime('%H:%M')
            if temperature is not None and temperature != 0: 
                self.temperature.append(float(temperature))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.temperature.pop(0)
                    self.time.pop(0)

            self.ax.clear()

            filtered_temperature = [temp for temp in self.temperature if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.temperature[i] is not None and self.temperature[i] != 0]

            if len(filtered_temperature) < 24:
                self.ax.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Temperature')
                self.ax.set_xticks(range(len(filtered_temperature)))
                self.ax.set_xticklabels(filtered_time)
            else:
                self.ax.plot(range(24), filtered_temperature[-24:], '-o', label='Temperature')
                self.ax.set_xticks(range(24))
                self.ax.set_xticklabels(filtered_time[-24:])

            self.ax.set_xlim(0, 23)
            self.ax.set_xlabel('Time')
            self.ax.set_ylabel('Temperature')
            self.ax.set_ylim(0, 50)
            y_major_locator = MultipleLocator(5)
            self.ax.yaxis.set_major_locator(y_major_locator)
            self.ax.legend()

            if self.nhietdo_lower is not None and self.nhietdo_high is not None:
                self.ax.axhline(self.nhietdo_lower, color='b', linestyle='--', label='Low Temperature Threshold')
                self.ax.axhline(self.nhietdo_high, color='b', linestyle='--', label='High Temperature Threshold')
                self.ax.text(23, self.nhietdo_lower, f'{self.nhietdo_lower:.1f}', ha='right', va='bottom')
                self.ax.text(23, self.nhietdo_high, f'{self.nhietdo_high:.1f}', ha='right', va='bottom')

            self.update_red_dots(self.nhietdo_lower, self.nhietdo_high, temperature)
            self.draw()
    def update_red_dots(self, threshold_low, threshold_high, temperature):
        colored_dots = [line for line in self.ax.lines if line.get_markerfacecolor() == 'red']
        for line in colored_dots:
            x_index = float(line.get_xdata())
            if (
                self.temperature[x_index] is None or
                self.temperature[x_index] == 0 or
                not (self.temperature[x_index] < float(threshold_low) or self.temperature[x_index] > float(threshold_high))
            ):
                line.remove()
        
        for i, temp in enumerate(self.temperature):
            if temp is not None and temp != 0:
                if  temp > float(threshold_high):
                    self.ax.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.ax.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif temp < float(threshold_low) :
                    self.ax.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.ax.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                    ha='center', va='bottom', color='red', fontsize=10)
        # Change the color of the last data point if it exceeds the thresholds
        if temperature is not None and temperature != 0:
            if temperature < float(threshold_low) or temperature > float(threshold_high):
                self.ax.plot(len(self.temperature) - 1, temperature, 'ro')
        
        # Add legend to show the label for red dots (if they exist)
        if any(temp < float(threshold_low) or temp > float(threshold_high) for temp in self.temperature):
            self.ax.legend(['Nhiệt độ'])
class MatplotlibCanvasNhietdo2(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.fignhietdo2, self.axnhhietdo = plt.subplots()
        super().__init__(self.fignhietdo2)
        self.temperature =[]
        self.time =[]
        self.axnhhietdo.set_xlabel('Thời gian')
        self.axnhhietdo.set_ylabel('Nhiệt độ')
        self.axnhhietdo.set_ylim(0, 50)
        self.data_count = 0
        self.nhietdo_lower = 20
        self.nhietdo_high = 25
        y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
        self.axnhhietdo.yaxis.set_major_locator(y_major_locator)
       
    def update_figureNhietdo2(self, client_address, temperature, humidity, light,  voltage_dc1, voltage_dc2,
                                    voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low, dienap_high, current_time):
        if client_address == tram45:
            if nhietdo_lower is not None and nhietdo_lower != 0 and self.nhietdo_lower != nhietdo_lower:
                self.axnhhietdo.axhline(self.nhietdo_lower, color='gray', linestyle='--')  # Draw dashed line for old lower threshold
                self.nhietdo_lower = float(nhietdo_lower)
            if nhietdo_high is not None and nhietdo_high != 0 and self.nhietdo_high != nhietdo_high:
                self.axnhhietdo.axhline(self.nhietdo_high, color='gray', linestyle='--')  # Draw dashed line for old higher threshold
                self.nhietdo_high = float(nhietdo_high)

            current_time = datetime.datetime.now().strftime('%H:%M')
            if temperature is not None and temperature != 0: 
                self.temperature.append(float(temperature))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.temperature.pop(0)
                    self.time.pop(0)

            self.axnhhietdo.clear()

            filtered_temperature = [temp for temp in self.temperature if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.temperature[i] is not None and self.temperature[i] != 0]

            if len(filtered_temperature) < 24:
                self.axnhhietdo.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Temperature')
                self.axnhhietdo.set_xticks(range(len(filtered_temperature)))
                self.axnhhietdo.set_xticklabels(filtered_time)
            else:
                self.axnhhietdo.plot(range(24), filtered_temperature[-24:], '-o', label='Temperature')
                self.axnhhietdo.set_xticks(range(24))
                self.axnhhietdo.set_xticklabels(filtered_time[-24:])

            self.axnhhietdo.set_xlim(0, 23)
            self.axnhhietdo.set_xlabel('Time')
            self.axnhhietdo.set_ylabel('Temperature')
            self.axnhhietdo.set_ylim(0, 50)
            y_major_locator = MultipleLocator(5)
            self.axnhhietdo.yaxis.set_major_locator(y_major_locator)
            self.axnhhietdo.legend()

            if self.nhietdo_lower is not None and self.nhietdo_high is not None:
                self.axnhhietdo.axhline(self.nhietdo_lower, color='b', linestyle='--', label='Low Temperature Threshold')
                self.axnhhietdo.axhline(self.nhietdo_high, color='b', linestyle='--', label='High Temperature Threshold')
                self.axnhhietdo.text(23, self.nhietdo_lower, f'{self.nhietdo_lower:.1f}', ha='right', va='bottom')
                self.axnhhietdo.text(23, self.nhietdo_high, f'{self.nhietdo_high:.1f}', ha='right', va='bottom')

            self.update_red_dots(self.nhietdo_lower, self.nhietdo_high, temperature)
            self.draw()

    
    def update_red_dots(self, threshold_low, threshold_high, temperature):
            colored_dots = [line for line in self.axnhhietdo.lines if line.get_markerfacecolor() in ['red', 'blue']]
            for line in colored_dots:
                x_index = float(line.get_xdata())
                if (
                    self.temperature[x_index] is None or
                    self.temperature[x_index] == 0 or
                    not (self.temperature[x_index] < float(threshold_low) or self.temperature[x_index] > float(threshold_high))
                ):
                    line.remove()
            
            for i, temp in enumerate(self.temperature):
                if temp is not None and temp != 0:
                    if  temp > float(threshold_high):
                        self.axnhhietdo.plot(i, temp, 'ro', label='Nhiệt độ')
                        self.axnhhietdo.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                        ha='center', va='bottom', color='red', fontsize=10)
                    elif temp < float(threshold_low) :
                        self.axnhhietdo.plot(i, temp, 'ro', label='Nhiệt độ')
                        self.axnhhietdo.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                        ha='center', va='bottom', color='red', fontsize=10)
            if temperature is not None and temperature != 0:
                if temperature < float(threshold_low) or temperature > float(threshold_high):
                    self.axnhhietdo.plot(len(self.temperature) - 1, temperature, 'ro')

            if any(temp < float(threshold_low) or temp > float(threshold_high) for temp in self.temperature):
                self.axnhhietdo.legend(['Nhiệt độ'])
class MatplotlibCanvasDoam(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdoam, self.ax2 = plt.subplots()
        super().__init__(self.figdoam)
        self.humidity = []
        self.time = []
        self.ax2.set_xlabel('Thời gian')
        self.ax2.set_ylabel('Độ ẩm')
        self.ax2.set_ylim(0, 100)
        self.data_count = 0
        self.doam_low = 40 
        self.doam_high = 70
        y_major_locator = MultipleLocator(10)  
        self.ax2.yaxis.set_major_locator(y_major_locator)
          

    def update_figureDoam(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram70:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if doam_low is not None and doam_low != 0:
                self.doam_low = float(doam_low)  
            if doam_high is not None and doam_high != 0:
                self.doam_high = float(doam_high) 
            if humidity is not None and humidity != 0:  
                self.humidity.append(float(humidity))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.time.pop(0)
                    self.humidity.pop(0)
            self.ax2.clear()
            filtered_temperature = [temp for temp in self.humidity if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.humidity[i] is not None and self.humidity[i] != 0]

            if len(filtered_temperature) < 24:
                    self.ax2.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Độ ẩm')
                    self.ax2.set_xticks(range(len(filtered_temperature)))
                    self.ax2.set_xticklabels(filtered_time)
            else:
                    self.ax2.plot(range(24), filtered_temperature[-24:], '-o', label='Độ ẩm')
                    self.ax2.set_xticks(range(24))
                    self.ax2.set_xticklabels(filtered_time[-24:])

            self.ax2.set_xlim(0, 23)
            self.ax2.set_xlabel('Thời gian')
            self.ax2.set_ylabel('Độ ẩm')
            self.ax2.set_ylim(0, 100)
            y_major_locator = MultipleLocator(10)  
            self.ax2.yaxis.set_major_locator(y_major_locator)
            self.ax2.legend()

            self.ax2.axhline(self.doam_low, color='b', linestyle='--', label='Ngưỡng Độ ẩm thấp')
            self.ax2.axhline(self.doam_high, color='b', linestyle='--', label='Ngưỡng Độ ẩm cao')
            self.ax2.text(23, self.doam_low, f'{self.doam_low:.1f}', ha='right', va='bottom')
            self.ax2.text(23, self.doam_high, f'{self.doam_high:.1f}', ha='right', va='bottom')
            self.update_red_dots(self.doam_low, self.doam_high, humidity)
            self.draw()

    def update_red_dots(self, doam_low, doam_high, humidity):
        # Clear the previous red dots
        red_dots = [line for line in self.ax2.lines if line.get_color() == 'red']
        for line in red_dots:
            line.remove()
        for i, temp in enumerate(self.humidity):
                if temp is not None and temp != 0:
                    if  temp > float(doam_high):
                        self.ax2.plot(i, temp, 'ro', label='Độ ẩm')
                        self.ax2.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                        ha='center', va='bottom', color='red', fontsize=10)
                    elif temp < float(doam_low) :
                        self.ax2.plot(i, temp, 'ro', label='Độ ẩm')
                        self.ax2.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                        ha='center', va='bottom', color='red', fontsize=10)
        if humidity is not None and humidity != 0:
            if humidity < float(doam_low) or humidity > float(doam_high):
                self.ax2.plot(len(self.humidity) - 1, humidity, 'ro')
            if any(temp < float(doam_low) or temp > float(doam_high) for temp in self.humidity):
                self.ax2.legend(['Độ ẩm'])
class MatplotlibCanvasDoam2(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdoam2, self.axdoam = plt.subplots()
        super().__init__(self.figdoam2)
        self.humidity = []
        self.time = []
        self.axdoam.set_xlabel('Thời gian')
        self.axdoam.set_ylabel('Độ ẩm')
        self.axdoam.set_ylim(0, 100)
        self.data_count = 0
        self.doam_low = 40 
        self.doam_high = 70 
        y_major_locator = MultipleLocator(10)  
        self.axdoam.yaxis.set_major_locator(y_major_locator)

    def update_figureDoam2(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram45:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if doam_low is not None and doam_low != 0:
                self.doam_low = float(doam_low)  
            if doam_high is not None and doam_high != 0:
                self.doam_high = float(doam_high)  
            if humidity is not None and humidity != 0:  
                self.humidity.append(float(humidity))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.time.pop(0)
                    self.humidity.pop(0)
            self.axdoam.clear()
            filtered_temperature = [temp for temp in self.humidity if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.humidity[i] is not None and self.humidity[i] != 0]

            if len(filtered_temperature) < 24:
                    self.axdoam.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Độ ẩm')
                    self.axdoam.set_xticks(range(len(filtered_temperature)))
                    self.axdoam.set_xticklabels(filtered_time)
            else:
                    self.axdoam.plot(range(24), filtered_temperature[-24:], '-o', label='Độ ẩm')
                    self.axdoam.set_xticks(range(24))
                    self.axdoam.set_xticklabels(filtered_time[-24:])

            self.axdoam.set_xlim(0, 23)
            self.axdoam.set_xlabel('Thời gian')
            self.axdoam.set_ylabel('Độ ẩm')
            self.axdoam.set_ylim(0, 100)
            y_major_locator = MultipleLocator(10)  # Khoảng cách là 5
            self.axdoam.yaxis.set_major_locator(y_major_locator)
            self.axdoam.legend()
            self.axdoam.axhline(self.doam_low, color='b', linestyle='--', label='Ngưỡng Độ ẩm thấp')
            self.axdoam.axhline(self.doam_high, color='b', linestyle='--', label='Ngưỡng Độ ẩm cao')
            self.axdoam.text(23, self.doam_low, f'{self.doam_low:.1f}', ha='right', va='bottom')
            self.axdoam.text(23, self.doam_high, f'{self.doam_high:.1f}', ha='right', va='bottom')
            self.update_red_dotsdoam(self.doam_low, self.doam_high, humidity)
            self.draw()

    def update_red_dotsdoam(self, doam_low, doam_high, humidity):
        red_dots = [line for line in self.axdoam.lines if line.get_color() == 'red']
        for line in red_dots:
            line.remove()
        for i, temp in enumerate(self.humidity):
                if temp is not None and temp != 0:
                    if  temp > float(doam_high):
                        self.axdoam.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoam.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                        ha='center', va='bottom', color='red', fontsize=10)
                    elif temp < float(doam_low) :
                        self.axdoam.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoam.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                        ha='center', va='bottom', color='red', fontsize=10)
        if humidity is not None and humidity != 0:  
        # Change the color of the last data point if it exceeds the thresholds
            if humidity < float(doam_low) or humidity > float(doam_high):
                self.axdoam.plot(len(self.humidity) - 1, humidity, 'ro')
            # Add legend to show the label for red dots (if they exist)
            if any(temp < float(doam_low) or temp > float(doam_high) for temp in self.humidity):
                self.axdoam.legend(['Độ ẩm'])
class MatplotlibCanvasDienap(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap, self.ax3 = plt.subplots()
        super().__init__(self.figdienap)
        self.voltage_dc1 = []
        self.dienap_low = 47.0
        self.dienap_low1 = 48.0
        self.dienap_high = 58.5
        self.time = []
        self.ax3.set_xlim(0, 23)
        self.ax3.set_xlabel('Thời gian')
        self.ax3.set_ylabel('Điện áp')
        self.ax3.set_ylim(30, 70)  
        self.data_count = 0
        y_major_locator = MultipleLocator(5) 
        self.ax3.yaxis.set_major_locator(y_major_locator)

    def update_figureDienap(self, client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                            voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                            dienap_low, dienap_low1, dienap_high, current_time):
        if client_address == tram70:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = float(dienap_low)  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = float(dienap_low1)  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = float(dienap_high)  
            if voltage_dc1 is not None and voltage_dc1 != 0:
                self.voltage_dc1.append(float(voltage_dc1))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc1.pop(0)
                    self.time.pop(0)
            self.ax3.clear()  

            if len(self.voltage_dc1) < 24:
                self.ax3.plot(range(len(self.voltage_dc1)), self.voltage_dc1, '-o', label='Điện áp DC1')
                self.ax3.set_xticks(range(len(self.voltage_dc1)))
                self.ax3.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp ')
                self.ax3.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.ax3.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.ax3.set_xlim(0, 23)
                self.ax3.set_xticklabels(self.time)
            else:
                self.ax3.plot(range(24), self.voltage_dc1[-24:], '-o', label='Điện áp DC1')
                self.ax3.set_xticks(range(24))
                self.ax3.set_xlim(0, 23)
                self.ax3.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp ')
                self.ax3.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.ax3.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.ax3.set_xticklabels(self.time[-24:])
            self.ax3.set_xlabel('Thời gian')
            self.ax3.set_ylabel('Điện áp')
            self.ax3.set_ylim(30, 70)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.ax3.yaxis.set_major_locator(y_major_locator)
            self.ax3.text(23, self.dienap_low, f'{self.dienap_low:.1f}', ha='right', va='top')
            self.ax3.text(23, self.dienap_low1, f'{self.dienap_low1:.1f}', ha='right', va='bottom')
            self.ax3.text(23, self.dienap_high, f'{self.dienap_high:.1f}', ha='right', va='bottom')
            self.ax3.legend()
            self.update_red_dots(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc1)
            self.draw()

    def update_red_dots(self, dienap_low, dienap_high, dienap_low1, voltage_dc1):
        dots = [line for line in self.ax3.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc1):
            if voltage is not None and voltage != 0:
                if voltage <= dienap_low1:
                    self.ax3.plot(i, voltage, 'ro', label='Điện áp DC1 (quá ngưỡng thấp 1)')
                    self.ax3.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < dienap_low:
                    self.ax3.plot(i, voltage, 'go', label='Điện áp DC1 (quá ngưỡng thấp)')
                elif voltage > dienap_high:
                    self.ax3.plot(i, voltage, 'ro', label='Điện áp DC1 (quá ngưỡng cao)')
                    self.ax3.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.ax3.plot(i, voltage, 'bo', label='Điện áp DC1 (trong ngưỡng)')

        if voltage_dc1 is not None and voltage_dc1 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc1
            if voltage_dc1 <= dienap_low1:
                self.ax3.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.ax3.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc1 < dienap_low:
                self.ax3.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'go')
            elif voltage_dc1 > dienap_high:
                self.ax3.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.ax3.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.ax3.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'bo')
class MatplotlibCanvasDienap2(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap2, self.ax4 = plt.subplots()
        super().__init__(self.figdienap2)
        self.voltage_dc2 = []
        self.dienap_low = 47.0
        self.dienap_low1 = 48.0
        self.dienap_high = 58.5
        self.time = []
        self.ax4.set_xlim(0, 23)
        self.ax4.set_xlabel('Thời gian')
        self.ax4.set_ylabel('Điện áp')
        self.ax4.set_ylim(30, 70)  
        self.data_count = 0
        y_major_locator = MultipleLocator(5) 
        self.ax4.yaxis.set_major_locator(y_major_locator)

    def update_figureDienap2(self, client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                            voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                            dienap_low, dienap_low1, dienap_high, current_time):
        if client_address == tram70:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = float(dienap_low)  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = float(dienap_low1)  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = float(dienap_high)  
            if voltage_dc2 is not None and voltage_dc2 != 0:
                self.voltage_dc2.append(float(voltage_dc2))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc2.pop(0)
                    self.time.pop(0)
            self.ax4.clear()  

            if len(self.voltage_dc2) < 24:
                self.ax4.plot(range(len(self.voltage_dc2)), self.voltage_dc2, '-o', label='Điện áp DC2')
                self.ax4.set_xticks(range(len(self.voltage_dc2)))
                self.ax4.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp ')
                self.ax4.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.ax4.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.ax4.set_xlim(0, 23)
                self.ax4.set_xticklabels(self.time)
            else:
                self.ax4.plot(range(24), self.voltage_dc2[-24:], '-o', label='Điện áp DC1')
                self.ax4.set_xticks(range(24))
                self.ax4.set_xlim(0, 23)
                self.ax4.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp')
                self.ax4.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.ax4.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.ax4.set_xticklabels(self.time[-24:])
            self.ax4.set_xlabel('Thời gian')
            self.ax4.set_ylabel('Điện áp')
            self.ax4.set_ylim(30, 70)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.ax4.yaxis.set_major_locator(y_major_locator)
            self.ax4.text(23, self.dienap_low, f'{self.dienap_low:.1f}', ha='right', va='top')
            self.ax4.text(23, self.dienap_low1, f'{self.dienap_low1:.1f}', ha='right', va='bottom')
            self.ax4.text(23, self.dienap_high, f'{self.dienap_high:.1f}', ha='right', va='bottom')
            self.ax4.legend()
            self.update_red_dots2(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc2)
            self.draw()

    def update_red_dots2(self, dienap_low, dienap_high, dienap_low1, voltage_dc2):
        dots = [line for line in self.ax4.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc2 and thresholds
        for i, voltage in enumerate(self.voltage_dc2):
            if voltage is not None and voltage != 0:
                if voltage <= dienap_low1:
                    self.ax4.plot(i, voltage, 'ro', label='Điện áp DC2 (quá ngưỡng thấp 1)')
                    self.ax4.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < dienap_low:
                    self.ax4.plot(i, voltage, 'go', label='Điện áp DC2 (quá ngưỡng thấp)')
                elif voltage > dienap_high:
                    self.ax4.plot(i, voltage, 'ro', label='Điện áp DC2 (quá ngưỡng cao)')
                    self.ax4.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.ax4.plot(i, voltage, 'bo', label='Điện áp DC2 (trong ngưỡng)')

        if voltage_dc2 is not None and voltage_dc2 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc2
            if voltage_dc2 <= dienap_low1:
                self.ax4.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.ax4.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc2 < dienap_low:
                self.ax4.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'go')
            elif voltage_dc2 > dienap_high:
                self.ax4.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.ax4.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.ax4.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'bo')
class MatplotlibCanvasDienap3(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap3, self.ax5 = plt.subplots()
        super().__init__(self.figdienap3)
        self.voltage_dc1 = []
        self.dienap_low = 47.0
        self.dienap_low1 = 48.0
        self.dienap_high = 58.5
        self.time = []
        self.ax5.set_xlim(0, 23)
        self.ax5.set_xlabel('Thời gian')
        self.ax5.set_ylabel('Điện áp')
        self.ax5.set_ylim(30, 70)  
        self.data_count = 0
        y_major_locator = MultipleLocator(5) 
        self.ax5.yaxis.set_major_locator(y_major_locator)

    def update_figureDienap3(self, client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                            voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                            dienap_low, dienap_low1, dienap_high, current_time):
        if client_address == tram45:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = float(dienap_low)  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = float(dienap_low1)  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = float(dienap_high)  
            if voltage_dc1 is not None and voltage_dc1 != 0:
                self.voltage_dc1.append(float(voltage_dc1))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc1.pop(0)
                    self.time.pop(0)
            self.ax5.clear()  

            if len(self.voltage_dc1) < 24:
                self.ax5.plot(range(len(self.voltage_dc1)), self.voltage_dc1, '-o', label='Điện áp DC1')
                self.ax5.set_xticks(range(len(self.voltage_dc1)))
                self.ax5.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.ax5.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.ax5.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.ax5.set_xlim(0, 23)
                self.ax5.set_xticklabels(self.time)
            else:
                self.ax5.plot(range(24), self.voltage_dc1[-24:], '-o', label='Điện áp DC1')
                self.ax5.set_xticks(range(24))
                self.ax5.set_xlim(0, 23)
                self.ax5.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.ax5.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.ax5.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.ax5.set_xticklabels(self.time[-24:])
            self.ax5.set_xlabel('Thời gian')
            self.ax5.set_ylabel('Điện áp')
            self.ax5.set_ylim(30, 70)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.ax5.yaxis.set_major_locator(y_major_locator)
            self.ax5.text(23, self.dienap_low, f'{self.dienap_low:.1f}', ha='right', va='top')
            self.ax5.text(23, self.dienap_low1, f'{self.dienap_low1:.1f}', ha='right', va='bottom')
            self.ax5.text(23, self.dienap_high, f'{self.dienap_high:.1f}', ha='right', va='bottom')
            self.ax5.legend()
            self.update_red_dots3(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc1)
            self.draw()

    def update_red_dots3(self, dienap_low, dienap_high, dienap_low1, voltage_dc1):
        dots = [line for line in self.ax5.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc1):
            if voltage is not None and voltage != 0:
                if voltage <= dienap_low1:
                    self.ax5.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng thấp 1)')
                    self.ax5.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < dienap_low:
                    self.ax5.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > dienap_high:
                    self.ax5.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.ax5.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.ax5.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc1 is not None and voltage_dc1 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc1
            if voltage_dc1 <= dienap_low1:
                self.ax5.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.ax5.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc1 < dienap_low:
                self.ax5.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'go')
            elif voltage_dc1 > dienap_high:
                self.ax5.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.ax5.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.ax5.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'bo')
class MatplotlibCanvasDienap4(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap4, self.ax6 = plt.subplots()
        super().__init__(self.figdienap4)
        self.voltage_dc2 = []
        self.dienap_low = 47.0
        self.dienap_low1 = 48.0
        self.dienap_high = 58.5
        self.time = []
        self.ax6.set_xlim(0, 23)
        self.ax6.set_xlabel('Thời gian')
        self.ax6.set_ylabel('Điện áp')
        self.ax6.set_ylim(30, 70)  
        self.data_count = 0
        y_major_locator = MultipleLocator(5) 
        self.ax6.yaxis.set_major_locator(y_major_locator)

    def update_figureDienap4(self, client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                            voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                            dienap_low, dienap_low1, dienap_high, current_time):
        if client_address == tram45:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = float(dienap_low)  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = float(dienap_low1)  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = float(dienap_high)  
            if voltage_dc2 is not None and voltage_dc2 != 0:
                self.voltage_dc2.append(float(voltage_dc2))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc2.pop(0)
                    self.time.pop(0)
            self.ax6.clear()  

            if len(self.voltage_dc2) < 24:
                self.ax6.plot(range(len(self.voltage_dc2)), self.voltage_dc2, '-o', label='Điện áp DC2')
                self.ax6.set_xticks(range(len(self.voltage_dc2)))
                self.ax6.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp ')
                self.ax6.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.ax6.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.ax6.set_xlim(0, 23)
                self.ax6.set_xticklabels(self.time)
            else:
                self.ax6.plot(range(24), self.voltage_dc2[-24:], '-o', label='Điện áp DC1')
                self.ax6.set_xticks(range(24))
                self.ax6.set_xlim(0, 23)
                self.ax6.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp')
                self.ax6.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.ax6.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.ax6.set_xticklabels(self.time[-24:])
            self.ax6.set_xlabel('Thời gian')
            self.ax6.set_ylabel('Điện áp')
            self.ax6.set_ylim(30, 70)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.ax6.yaxis.set_major_locator(y_major_locator)
            self.ax6.text(23, self.dienap_low, f'{self.dienap_low:.1f}', ha='right', va='top')
            self.ax6.text(23, self.dienap_low1, f'{self.dienap_low1:.1f}', ha='right', va='bottom')
            self.ax6.text(23, self.dienap_high, f'{self.dienap_high:.1f}', ha='right', va='bottom')
            self.ax6.legend()
            self.update_red_dots4(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc2)
            self.draw()

    def update_red_dots4(self, dienap_low, dienap_high, dienap_low1, voltage_dc2):
        dots = [line for line in self.ax6.lines if line.get_color() in ['red', 'green']]
        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc2):
            if voltage is not None and voltage != 0:
                if dienap_low <= voltage <= dienap_low1:  
                    self.ax6.plot(i, voltage, 'yo', label='Điện áp DC (trong ngưỡng thấp)')
                    self.ax6.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < dienap_low:
                    self.ax6.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > dienap_high:
                    self.ax6.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.ax6.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.ax6.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc2 is not None and voltage_dc2 != 0:
            if dienap_low < voltage_dc2 < dienap_low1:  # Between dienap_low and dienap_low1
                self.ax6.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'yo')
                self.ax6.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2),
                                textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc2 < dienap_low:
                self.ax6.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'go')
            elif voltage_dc2 > dienap_high:
                self.ax6.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.ax6.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2),
                                textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.ax6.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'bo')

#tram 01-------------------------------------------------------------------------------------------------------------------------
class MatplotlibCanvasNhietdo01(FigureCanvas):
    
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.fignhietdo01, self.axnhietdo01 = plt.subplots()
        super().__init__(self.fignhietdo01)
        self.temperature =[]
        self.time =[]
        self.axnhietdo01.set_xlabel('Thời gian')
        self.axnhietdo01.set_ylabel('Nhiệt độ')
        self.axnhietdo01.set_ylim(0, 50)
        self.data_count = 0
        self.nhietdo_lower = 20
        self.nhietdo_high = 25
        y_major_locator = MultipleLocator(5)  
        self.axnhietdo01.yaxis.set_major_locator(y_major_locator)
       
    def update_figureNhietdo01(self, client_address, temperature, humidity, light,  voltage_dc1, voltage_dc2,
                                    voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low, dienap_high):
        if client_address == tram01:
            if nhietdo_lower is not None and nhietdo_lower != 0:
                self.nhietdo_lower = nhietdo_lower 
            if nhietdo_high is not None and nhietdo_high != 0:
                    self.nhietdo_high = nhietdo_high  # Cập nhật ngưỡng cao nếu có giá trị gửi lên
            current_time = datetime.datetime.now().strftime('%H:%M')
     
            if temperature is not None and temperature != 0:  # Kiểm tra giá trị nhiệt độ không phải là None hoặc 0
                self.temperature.append(float(temperature))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.temperature.pop(0)
                    self.time.pop(0)
            self.axnhietdo01.clear()

            # Filter out None values from temperature and corresponding time
            filtered_temperature = [temp for temp in self.temperature if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.temperature[i] is not None and self.temperature[i] != 0]

            if len(filtered_temperature) < 24:
                self.axnhietdo01.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Nhiệt độ')
                self.axnhietdo01.set_xticks(range(len(filtered_temperature)))
                self.axnhietdo01.set_xticklabels(filtered_time)
              
            else:
                self.axnhietdo01.plot(range(24), filtered_temperature[-24:], '-o', label='Nhiệt độ')
                self.axnhietdo01.set_xticks(range(24))
                self.axnhietdo01.set_xticklabels(filtered_time[-24:])
              

            self.axnhietdo01.set_xlim(0, 23)
            self.axnhietdo01.set_xlabel('Thời gian')
            self.axnhietdo01.set_ylabel('Nhiệt độ')
            self.axnhietdo01.set_ylim(0, 50)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axnhietdo01.yaxis.set_major_locator(y_major_locator)
            # Draw 
            self.axnhietdo01.axhline(self.nhietdo_lower, color='b', linestyle='--', label='Ngưỡng nhiệt độ thấp')
            self.axnhietdo01.axhline(self.nhietdo_high, color='b', linestyle='--', label='Ngưỡng nhiệt độ cao')
            self.axnhietdo01.text(23, self.nhietdo_lower, int(self.nhietdo_lower), ha='right', va='bottom')
            self.axnhietdo01.text(23, self.nhietdo_high, int(self.nhietdo_high), ha='right', va='bottom')
            self.axnhietdo01.legend()
         
            self.update_red_dots01(self.nhietdo_lower, self.nhietdo_high, temperature)
            self.draw()
    def update_red_dots01(self, threshold_low, threshold_high, temperature):
        colored_dots = [line for line in self.axnhietdo01.lines if line.get_markerfacecolor() in ['red', 'blue']]
        for line in colored_dots:
            x_index = float(line.get_xdata())
            if (
                self.temperature[x_index] is None or
                self.temperature[x_index] == 0 or
                not (self.temperature[x_index] < float(threshold_low) or self.temperature[x_index] > float(threshold_high))
            ):
                line.remove()
        
        for i, temp in enumerate(self.temperature):
            if temp is not None and temp != 0:
                if  temp > float(threshold_high):
                    self.axnhietdo01.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.axnhietdo01.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif temp < float(threshold_low) :
                    self.axnhietdo01.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.axnhietdo01.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                    ha='center', va='bottom', color='red', fontsize=10)
        # Change the color of the last data point if it exceeds the thresholds
        if temperature is not None and temperature != 0:
            if temperature < float(threshold_low) or temperature > float(threshold_high):
                self.axnhietdo01.plot(len(self.temperature) - 1, temperature, 'ro')
        
        # Add legend to show the label for red dots (if they exist)
        if any(temp < float(threshold_low) or temp > float(threshold_high) for temp in self.temperature):
            self.axnhietdo01.legend(['Nhiệt độ'])
class MatplotlibCanvasDoam01(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdoam01, self.axdoamtram01 = plt.subplots()
        super().__init__(self.figdoam01)
        self.humidity = []
        self.time = []
        self.axdoamtram01.set_xlabel('Thời gian')
        self.axdoamtram01.set_ylabel('Độ ẩm')
        self.axdoamtram01.set_ylim(0, 100)
        self.data_count = 0
        self.doam_low = 40 
        self.doam_high = 70
        y_major_locator = MultipleLocator(10)  
        self.axdoamtram01.yaxis.set_major_locator(y_major_locator)
          

    def update_figureDoam01(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram01:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if doam_low is not None and doam_low != 0:
                self.doam_low = doam_low  
            if doam_high is not None and doam_high != 0:
                self.doam_high = doam_high 
            if humidity is not None and humidity != 0:  
                self.humidity.append(humidity)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.time.pop(0)
                    self.humidity.pop(0)
            self.axdoamtram01.clear()
            filtered_temperature = [temp for temp in self.humidity if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.humidity[i] is not None and self.humidity[i] != 0]

            if len(filtered_temperature) < 24:
                    self.axdoamtram01.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Độ ẩm')
                    self.axdoamtram01.set_xticks(range(len(filtered_temperature)))
                    self.axdoamtram01.set_xticklabels(filtered_time)
            else:
                    self.axdoamtram01.plot(range(24), filtered_temperature[-24:], '-o', label='Độ ẩm')
                    self.axdoamtram01.set_xticks(range(24))
                    self.axdoamtram01.set_xticklabels(filtered_time[-24:])

            self.axdoamtram01.set_xlim(0, 23)
            self.axdoamtram01.set_xlabel('Thời gian')
            self.axdoamtram01.set_ylabel('Độ ẩm')
            self.axdoamtram01.set_ylim(0, 100)
            y_major_locator = MultipleLocator(10)  
            self.axdoamtram01.yaxis.set_major_locator(y_major_locator)
            self.axdoamtram01.legend()

            self.axdoamtram01.axhline(self.doam_low, color='b', linestyle='--', label='Ngưỡng Độ ẩm thấp')
            self.axdoamtram01.axhline(self.doam_high, color='b', linestyle='--', label='Ngưỡng Độ ẩm cao')
            self.axdoamtram01.text(23, self.doam_low, int(self.doam_low), ha='right', va='bottom')
            self.axdoamtram01.text(23, self.doam_high, int(self.doam_high), ha='right', va='bottom')
            self.update_red_dots01(self.doam_low, self.doam_high, humidity)
            self.draw()

    def update_red_dots01(self, doam_low, doam_high, humidity):
        # Clear the previous red dots
        red_dots = [line for line in self.axdoamtram01.lines if line.get_color() == 'red']
        for line in red_dots:
            line.remove()
        for i, temp in enumerate(self.humidity):
                if temp is not None and temp != 0:
                    if  temp > float(doam_high):
                        self.axdoamtram01.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoamtram01.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                        ha='center', va='bottom', color='red', fontsize=10)
                    elif temp < float(doam_low) :
                        self.axdoamtram01.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoamtram01.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                        ha='center', va='bottom', color='red', fontsize=10)
        if humidity is not None and humidity != 0:
            if humidity < float(doam_low) or humidity > float(doam_high):
                self.axdoamtram01.plot(len(self.humidity) - 1, humidity, 'ro')
            if any(temp < float(doam_low) or temp > float(doam_high) for temp in self.humidity):
                self.axdoamtram01.legend(['Độ ẩm'])
class MatplotlibCanvasDienap011(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap011, self.axdienap1tram01 = plt.subplots()
        super().__init__(self.figdienap011)
        self.voltage_dc1 = []
        self.dienap_low= 47
        self.dienap_low1 =48
        self.dienap_high =58.5
        self.time = []
        self.axdienap1tram01.set_xlim(0, 23)
        self.axdienap1tram01.set_xlabel('Thời gian')
        self.axdienap1tram01.set_ylabel('Điện áp')
        self.axdienap1tram01.set_ylim(20, 60)  
        self.data_count = 0
        y_major_locator = MultipleLocator(5) 
        self.axdienap1tram01.yaxis.set_major_locator(y_major_locator)

    def update_figureDienap011(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                    voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram01:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high  
            if voltage_dc1 is not None and voltage_dc1 !=0:
                self.voltage_dc1.append(voltage_dc1)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc1.pop(0)
                    self.time.pop(0)
            self.axdienap1tram01.clear()  

            if len(self.voltage_dc1) < 24:
                self.axdienap1tram01.plot(range(len(self.voltage_dc1)), self.voltage_dc1, '-o', label='Điện áp DC1')
                self.axdienap1tram01.set_xticks(range(len(self.voltage_dc1)))
                self.axdienap1tram01.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap1tram01.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap1tram01.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap1tram01.set_xlim(0, 23)
                self.axdienap1tram01.set_xticklabels(self.time)
            else:
                self.axdienap1tram01.plot(range(24), self.voltage_dc1[-24:], '-o', label='Điện áp DC1')
                self.axdienap1tram01.set_xticks(range(24))
                self.axdienap1tram01.set_xlim(0, 23)
                self.axdienap1tram01.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap1tram01.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap1tram01.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap1tram01.set_xticklabels(self.time[-24:])
            self.axdienap1tram01.set_xlabel('Thời gian')
            self.axdienap1tram01.set_ylabel('Điện áp')
            self.axdienap1tram01.set_ylim(20, 60)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axdienap1tram01.yaxis.set_major_locator(y_major_locator)
            self.axdienap1tram01.text(23, self.dienap_low, int(self.dienap_low), ha='right', va='top')
            self.axdienap1tram01.text(23, self.dienap_low1, int(self.dienap_low1), ha='right', va='bottom')
            self.axdienap1tram01.text(23, self.dienap_high, int(self.dienap_high), ha='right', va='bottom')
            self.axdienap1tram01.legend()
            self.update_red_dots01(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc1)
            self.draw()
    def update_red_dots01(self, dienap_low, dienap_high,dienap_low1, voltage_dc1):
        dots = [line for line in self.axdienap1tram01.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc1):
            if voltage is not None and voltage != 0:
                if voltage < float(dienap_low1):
                    self.axdienap1tram01.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng thấp 1)')
                    self.axdienap1tram01.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < float(dienap_low):
                    self.axdienap1tram01.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > float(dienap_high):
                    self.axdienap1tram01.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.axdienap1tram01.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.axdienap1tram01.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc1 is not None and voltage_dc1 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc1
            if voltage_dc1 < float(dienap_low1):
                self.axdienap1tram01.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.axdienap1tram01.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc1 < float(dienap_low):
                self.axdienap1tram01.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'go')
            elif voltage_dc1 > float(dienap_high):
                self.axdienap1tram01.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.axdienap1tram01.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.axdienap1tram01.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'bo')
class MatplotlibCanvasDienap012(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap012, self.axdienap2tram01 = plt.subplots()
        super().__init__(self.figdienap012)
        self.voltage_dc2 = []
        self.dienap_low= 47
        self.dienap_low1 =48
        self.dienap_high =58.5
        self.time = []
        self.axdienap2tram01.set_xlim(0, 23)
        self.axdienap2tram01.set_xlabel('Thời gian')
        self.axdienap2tram01.set_ylabel('Điện áp')
        self.axdienap2tram01.set_ylim(20, 60)  
        y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
        self.axdienap2tram01.yaxis.set_major_locator(y_major_locator)
        self.data_count = 0

    def update_figureDienap012(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram01:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high  
            if voltage_dc2 is not None and voltage_dc2 !=0:
                self.voltage_dc2.append(voltage_dc2)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc2.pop(0)
                    self.time.pop(0)
            self.axdienap2tram01.clear()  

            if len(self.voltage_dc2) < 24:
                self.axdienap2tram01.plot(range(len(self.voltage_dc2)), self.voltage_dc2, '-o', label='Điện áp DC2')
                self.axdienap2tram01.set_xticks(range(len(self.voltage_dc2)))
                self.axdienap2tram01.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap2tram01.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap2tram01.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap2tram01.set_xlim(0, 23)
                self.axdienap2tram01.set_xticklabels(self.time)
            else:
                self.axdienap2tram01.plot(range(24), self.voltage_dc2[-24:], '-o', label='Điện áp DC2')
                self.axdienap2tram01.set_xticks(range(24))
                self.axdienap2tram01.set_xlim(0, 23)
                self.axdienap2tram01.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap2tram01.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap2tram01.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap2tram01.set_xticklabels(self.time[-24:])
            self.axdienap2tram01.set_xlabel('Thời gian')
            self.axdienap2tram01.set_ylabel('Điện áp')
            self.axdienap2tram01.set_ylim(20, 60)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axdienap2tram01.yaxis.set_major_locator(y_major_locator)
            self.axdienap2tram01.text(23, self.dienap_low, int(self.dienap_low), ha='right', va='top')
            self.axdienap2tram01.text(23, self.dienap_low1, int(self.dienap_low1), ha='right', va='bottom')
            self.axdienap2tram01.text(23, self.dienap_high, int(self.dienap_high), ha='right', va='bottom')
            self.axdienap2tram01.legend()
            self.update_red_dots012(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc2)
            self.draw()
    def update_red_dots012(self, dienap_low, dienap_high,dienap_low1, voltage_dc2):
        dots = [line for line in self.axdienap2tram01.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc2):
            if voltage is not None and voltage != 0:
                if voltage < float(dienap_low1):
                    self.axdienap2tram01.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng thấp 1)')
                    self.axdienap2tram01.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < float(dienap_low):
                    self.axdienap2tram01.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > float(dienap_high):
                    self.axdienap2tram01.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.axdienap2tram01.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.axdienap2tram01.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc2 is not None and voltage_dc2 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc2
            if voltage_dc2 < float(dienap_low1):
                self.axdienap2tram01.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.axdienap2tram01.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc2 < float(dienap_low):
                self.axdienap2tram01.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'go')
            elif voltage_dc2 > float(dienap_high):
                self.axdienap2tram01.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.axdienap2tram01.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.axdienap2tram01.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'bo')
#tram48-------------------------------------------------------------------------------------------------------------------------------
class MatplotlibCanvasNhietdo48(FigureCanvas):
    
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.fignhietdo48, self.axnhietdo48 = plt.subplots()
        super().__init__(self.fignhietdo48)
        self.temperature =[]
        self.time =[]
        self.axnhietdo48.set_xlabel('Thời gian')
        self.axnhietdo48.set_ylabel('Nhiệt độ')
        self.axnhietdo48.set_ylim(0, 50)
        self.data_count = 0
        self.nhietdo_lower = 20
        self.nhietdo_high = 25
        y_major_locator = MultipleLocator(5)  
        self.axnhietdo48.yaxis.set_major_locator(y_major_locator)
       
    def update_figureNhietdo48(self, client_address, temperature, humidity, light,  voltage_dc1, voltage_dc2,
                                    voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low, dienap_high):
        if client_address == tram48:
            if nhietdo_lower is not None and nhietdo_lower != 0:
                self.nhietdo_lower = nhietdo_lower 
            if nhietdo_high is not None and nhietdo_high != 0:
                    self.nhietdo_high = nhietdo_high  # Cập nhật ngưỡng cao nếu có giá trị gửi lên
            current_time = datetime.datetime.now().strftime('%H:%M')
     
            if temperature is not None and temperature != 0:  # Kiểm tra giá trị nhiệt độ không phải là None hoặc 0
                self.temperature.append(float(temperature))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.temperature.pop(0)
                    self.time.pop(0)
            self.axnhietdo48.clear()

            # Filter out None values from temperature and corresponding time
            filtered_temperature = [temp for temp in self.temperature if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.temperature[i] is not None and self.temperature[i] != 0]

            if len(filtered_temperature) < 24:
                self.axnhietdo48.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Nhiệt độ')
                self.axnhietdo48.set_xticks(range(len(filtered_temperature)))
                self.axnhietdo48.set_xticklabels(filtered_time)
              
            else:
                self.axnhietdo48.plot(range(24), filtered_temperature[-24:], '-o', label='Nhiệt độ')
                self.axnhietdo48.set_xticks(range(24))
                self.axnhietdo48.set_xticklabels(filtered_time[-24:])
              

            self.axnhietdo48.set_xlim(0, 23)
            self.axnhietdo48.set_xlabel('Thời gian')
            self.axnhietdo48.set_ylabel('Nhiệt độ')
            self.axnhietdo48.set_ylim(0, 50)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axnhietdo48.yaxis.set_major_locator(y_major_locator)
            # Draw 
            self.axnhietdo48.axhline(self.nhietdo_lower, color='b', linestyle='--', label='Ngưỡng nhiệt độ thấp')
            self.axnhietdo48.axhline(self.nhietdo_high, color='b', linestyle='--', label='Ngưỡng nhiệt độ cao')
            self.axnhietdo48.text(23, self.nhietdo_lower, int(self.nhietdo_lower), ha='right', va='bottom')
            self.axnhietdo48.text(23, self.nhietdo_high, int(self.nhietdo_high), ha='right', va='bottom')
            self.axnhietdo48.legend()
         
            self.update_red_dots48(self.nhietdo_lower, self.nhietdo_high, temperature)
            self.draw()
    def update_red_dots48(self, threshold_low, threshold_high, temperature):
        colored_dots = [line for line in self.axnhietdo48.lines if line.get_markerfacecolor() in ['red', 'blue']]
        for line in colored_dots:
            x_index = float(line.get_xdata())
            if (
                self.temperature[x_index] is None or
                self.temperature[x_index] == 0 or
                not (self.temperature[x_index] < float(threshold_low) or self.temperature[x_index] > float(threshold_high))
            ):
                line.remove()
        
        for i, temp in enumerate(self.temperature):
            if temp is not None and temp != 0:
                if  temp > float(threshold_high):
                    self.axnhietdo48.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.axnhietdo48.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif temp < float(threshold_low) :
                    self.axnhietdo48.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.axnhietdo48.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                    ha='center', va='bottom', color='red', fontsize=10)
        # Change the color of the last data point if it exceeds the thresholds
        if temperature is not None and temperature != 0:
            if temperature < float(threshold_low) or temperature > float(threshold_high):
                self.axnhietdo48.plot(len(self.temperature) - 1, temperature, 'ro')
        
        # Add legend to show the label for red dots (if they exist)
        if any(temp < float(threshold_low) or temp > float(threshold_high) for temp in self.temperature):
            self.axnhietdo48.legend(['Nhiệt độ'])
class MatplotlibCanvasDoam48(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdoam48, self.axdoamtram48 = plt.subplots()
        super().__init__(self.figdoam48)
        self.humidity = []
        self.time = []
        self.axdoamtram48.set_xlabel('Thời gian')
        self.axdoamtram48.set_ylabel('Độ ẩm')
        self.axdoamtram48.set_ylim(0, 100)
        self.data_count = 0
        self.doam_low = 40 
        self.doam_high = 70
        y_major_locator = MultipleLocator(10)  
        self.axdoamtram48.yaxis.set_major_locator(y_major_locator)
          

    def update_figureDoam48(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram48:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if doam_low is not None and doam_low != 0:
                self.doam_low = doam_low  
            if doam_high is not None and doam_high != 0:
                self.doam_high = doam_high 
            if humidity is not None and humidity != 0:  
                self.humidity.append(humidity)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.time.pop(0)
                    self.humidity.pop(0)
            self.axdoamtram48.clear()
            filtered_temperature = [temp for temp in self.humidity if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.humidity[i] is not None and self.humidity[i] != 0]

            if len(filtered_temperature) < 24:
                    self.axdoamtram48.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Độ ẩm')
                    self.axdoamtram48.set_xticks(range(len(filtered_temperature)))
                    self.axdoamtram48.set_xticklabels(filtered_time)
            else:
                    self.axdoamtram48.plot(range(24), filtered_temperature[-24:], '-o', label='Độ ẩm')
                    self.axdoamtram48.set_xticks(range(24))
                    self.axdoamtram48.set_xticklabels(filtered_time[-24:])

            self.axdoamtram48.set_xlim(0, 23)
            self.axdoamtram48.set_xlabel('Thời gian')
            self.axdoamtram48.set_ylabel('Độ ẩm')
            self.axdoamtram48.set_ylim(0, 100)
            y_major_locator = MultipleLocator(10)  
            self.axdoamtram48.yaxis.set_major_locator(y_major_locator)
            self.axdoamtram48.legend()

            self.axdoamtram48.axhline(self.doam_low, color='b', linestyle='--', label='Ngưỡng Độ ẩm thấp')
            self.axdoamtram48.axhline(self.doam_high, color='b', linestyle='--', label='Ngưỡng Độ ẩm cao')
            self.axdoamtram48.text(23, self.doam_low, int(self.doam_low), ha='right', va='bottom')
            self.axdoamtram48.text(23, self.doam_high, int(self.doam_high), ha='right', va='bottom')
            self.update_red_dots48(self.doam_low, self.doam_high, humidity)
            self.draw()

    def update_red_dots48(self, doam_low, doam_high, humidity):
        # Clear the previous red dots
        red_dots = [line for line in self.axdoamtram48.lines if line.get_color() == 'red']
        for line in red_dots:
            line.remove()
        for i, temp in enumerate(self.humidity):
                if temp is not None and temp != 0:
                    if  temp > float(doam_high):
                        self.axdoamtram48.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoamtram48.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                        ha='center', va='bottom', color='red', fontsize=10)
                    elif temp < float(doam_low) :
                        self.axdoamtram48.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoamtram48.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                        ha='center', va='bottom', color='red', fontsize=10)
        if humidity is not None and humidity != 0:
            if humidity < float(doam_low) or humidity > float(doam_high):
                self.axdoamtram48.plot(len(self.humidity) - 1, humidity, 'ro')
            if any(temp < float(doam_low) or temp > float(doam_high) for temp in self.humidity):
                self.axdoamtram48.legend(['Độ ẩm'])
class MatplotlibCanvasDienap148(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap148, self.axdienap1tram148 = plt.subplots()
        super().__init__(self.figdienap148)
        self.voltage_dc1 = []
        self.dienap_low= 47
        self.dienap_low1 =48
        self.dienap_high =58.5
        self.time = []
        self.axdienap1tram148.set_xlim(0, 23)
        self.axdienap1tram148.set_xlabel('Thời gian')
        self.axdienap1tram148.set_ylabel('Điện áp')
        self.axdienap1tram148.set_ylim(20, 60)  
        self.data_count = 0
        y_major_locator = MultipleLocator(5) 
        self.axdienap1tram148.yaxis.set_major_locator(y_major_locator)

    def update_figureDienap148(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                    voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram48:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high  
            if voltage_dc1 is not None and voltage_dc1 !=0:
                self.voltage_dc1.append(voltage_dc1)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc1.pop(0)
                    self.time.pop(0)
            self.axdienap1tram148.clear()  

            if len(self.voltage_dc1) < 24:
                self.axdienap1tram148.plot(range(len(self.voltage_dc1)), self.voltage_dc1, '-o', label='Điện áp DC1')
                self.axdienap1tram148.set_xticks(range(len(self.voltage_dc1)))
                self.axdienap1tram148.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap1tram148.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap1tram148.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap1tram148.set_xlim(0, 23)
                self.axdienap1tram148.set_xticklabels(self.time)
            else:
                self.axdienap1tram148.plot(range(24), self.voltage_dc1[-24:], '-o', label='Điện áp DC1')
                self.axdienap1tram148.set_xticks(range(24))
                self.axdienap1tram148.set_xlim(0, 23)
                self.axdienap1tram148.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap1tram148.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap1tram148.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap1tram148.set_xticklabels(self.time[-24:])
            self.axdienap1tram148.set_xlabel('Thời gian')
            self.axdienap1tram148.set_ylabel('Điện áp')
            self.axdienap1tram148.set_ylim(20, 60)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axdienap1tram148.yaxis.set_major_locator(y_major_locator)
            self.axdienap1tram148.text(23, self.dienap_low, int(self.dienap_low), ha='right', va='top')
            self.axdienap1tram148.text(23, self.dienap_low1, int(self.dienap_low1), ha='right', va='bottom')
            self.axdienap1tram148.text(23, self.dienap_high, int(self.dienap_high), ha='right', va='bottom')
            self.axdienap1tram148.legend()
            self.update_red_dots148(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc1)
            self.draw()
    def update_red_dots148(self, dienap_low, dienap_high,dienap_low1, voltage_dc1):
        dots = [line for line in self.axdienap1tram148.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc1):
            if voltage is not None and voltage != 0:
                if voltage < float(dienap_low1):
                    self.axdienap1tram148.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng thấp 1)')
                    self.axdienap1tram148.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < float(dienap_low):
                    self.axdienap1tram148.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > float(dienap_high):
                    self.axdienap1tram148.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.axdienap1tram148.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.axdienap1tram148.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc1 is not None and voltage_dc1 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc1
            if voltage_dc1 < float(dienap_low1):
                self.axdienap1tram148.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.axdienap1tram148.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc1 < float(dienap_low):
                self.axdienap1tram148.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'go')
            elif voltage_dc1 > float(dienap_high):
                self.axdienap1tram148.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.axdienap1tram148.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.axdienap1tram148.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'bo')
class MatplotlibCanvasDienap248(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap248, self.axdienap2tram48 = plt.subplots()
        super().__init__(self.figdienap248)
        self.voltage_dc2 = []
        self.dienap_low= 47
        self.dienap_low1 =48
        self.dienap_high =58.5
        self.time = []
        self.axdienap2tram48.set_xlim(0, 23)
        self.axdienap2tram48.set_xlabel('Thời gian')
        self.axdienap2tram48.set_ylabel('Điện áp')
        self.axdienap2tram48.set_ylim(20, 60)  
        y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
        self.axdienap2tram48.yaxis.set_major_locator(y_major_locator)
        self.data_count = 0

    def update_figureDienap248(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram48:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high  
            if voltage_dc2 is not None and voltage_dc2 !=0:
                self.voltage_dc2.append(voltage_dc2)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc2.pop(0)
                    self.time.pop(0)
            self.axdienap2tram48.clear()  

            if len(self.voltage_dc2) < 24:
                self.axdienap2tram48.plot(range(len(self.voltage_dc2)), self.voltage_dc2, '-o', label='Điện áp DC2')
                self.axdienap2tram48.set_xticks(range(len(self.voltage_dc2)))
                self.axdienap2tram48.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap2tram48.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap2tram48.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap2tram48.set_xlim(0, 23)
                self.axdienap2tram48.set_xticklabels(self.time)
            else:
                self.axdienap2tram48.plot(range(24), self.voltage_dc2[-24:], '-o', label='Điện áp DC2')
                self.axdienap2tram48.set_xticks(range(24))
                self.axdienap2tram48.set_xlim(0, 23)
                self.axdienap2tram48.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap2tram48.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap2tram48.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap2tram48.set_xticklabels(self.time[-24:])
            self.axdienap2tram48.set_xlabel('Thời gian')
            self.axdienap2tram48.set_ylabel('Điện áp')
            self.axdienap2tram48.set_ylim(20, 60)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axdienap2tram48.yaxis.set_major_locator(y_major_locator)
            self.axdienap2tram48.text(23, self.dienap_low, int(self.dienap_low), ha='right', va='top')
            self.axdienap2tram48.text(23, self.dienap_low1, int(self.dienap_low1), ha='right', va='bottom')
            self.axdienap2tram48.text(23, self.dienap_high, int(self.dienap_high), ha='right', va='bottom')
            self.axdienap2tram48.legend()
            self.update_red_dots248(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc2)
            self.draw()
    def update_red_dots248(self, dienap_low, dienap_high,dienap_low1, voltage_dc2):
        dots = [line for line in self.axdienap2tram48.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc2):
            if voltage is not None and voltage != 0:
                if voltage < float(dienap_low1):
                    self.axdienap2tram48.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng thấp 1)')
                    self.axdienap2tram48.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < float(dienap_low):
                    self.axdienap2tram48.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > float(dienap_high):
                    self.axdienap2tram48.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.axdienap2tram48.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.axdienap2tram48.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc2 is not None and voltage_dc2 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc2
            if voltage_dc2 < float(dienap_low1):
                self.axdienap2tram48.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.axdienap2tram48.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc2 < float(dienap_low):
                self.axdienap2tram48.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'go')
            elif voltage_dc2 > float(dienap_high):
                self.axdienap2tram48.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.axdienap2tram48.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.axdienap2tram48.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'bo')
#tram71-------------------------------------------------------------------------------------------------------------------
class MatplotlibCanvasNhietdo71(FigureCanvas):
    
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.fignhietdo71, self.axnhietdo71 = plt.subplots()
        super().__init__(self.fignhietdo71)
        self.temperature =[]
        self.time =[]
        self.axnhietdo71.set_xlabel('Thời gian')
        self.axnhietdo71.set_ylabel('Nhiệt độ')
        self.axnhietdo71.set_ylim(0, 50)
        self.data_count = 0
        self.nhietdo_lower = 20
        self.nhietdo_high = 25
        y_major_locator = MultipleLocator(5)  
        self.axnhietdo71.yaxis.set_major_locator(y_major_locator)
       
    def update_figureNhietd71(self, client_address, temperature, humidity, light,  voltage_dc1, voltage_dc2,
                                    voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low, dienap_high):
        if client_address == tram71:
            if nhietdo_lower is not None and nhietdo_lower != 0:
                self.nhietdo_lower = nhietdo_lower 
            if nhietdo_high is not None and nhietdo_high != 0:
                    self.nhietdo_high = nhietdo_high  # Cập nhật ngưỡng cao nếu có giá trị gửi lên
            current_time = datetime.datetime.now().strftime('%H:%M')
     
            if temperature is not None and temperature != 0:  # Kiểm tra giá trị nhiệt độ không phải là None hoặc 0
                self.temperature.append(float(temperature))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.temperature.pop(0)
                    self.time.pop(0)
            self.axnhietdo71.clear()

            # Filter out None values from temperature and corresponding time
            filtered_temperature = [temp for temp in self.temperature if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.temperature[i] is not None and self.temperature[i] != 0]

            if len(filtered_temperature) < 24:
                self.axnhietdo71.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Nhiệt độ')
                self.axnhietdo71.set_xticks(range(len(filtered_temperature)))
                self.axnhietdo71.set_xticklabels(filtered_time)
              
            else:
                self.axnhietdo71.plot(range(24), filtered_temperature[-24:], '-o', label='Nhiệt độ')
                self.axnhietdo71.set_xticks(range(24))
                self.axnhietdo71.set_xticklabels(filtered_time[-24:])
              

            self.axnhietdo71.set_xlim(0, 23)
            self.axnhietdo71.set_xlabel('Thời gian')
            self.axnhietdo71.set_ylabel('Nhiệt độ')
            self.axnhietdo71.set_ylim(0, 50)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axnhietdo71.yaxis.set_major_locator(y_major_locator)
            # Draw 
            self.axnhietdo71.axhline(self.nhietdo_lower, color='b', linestyle='--', label='Ngưỡng nhiệt độ thấp')
            self.axnhietdo71.axhline(self.nhietdo_high, color='b', linestyle='--', label='Ngưỡng nhiệt độ cao')
            self.axnhietdo71.text(23, self.nhietdo_lower, int(self.nhietdo_lower), ha='right', va='bottom')
            self.axnhietdo71.text(23, self.nhietdo_high, int(self.nhietdo_high), ha='right', va='bottom')
            self.axnhietdo71.legend()
         
            self.update_red_dots71(self.nhietdo_lower, self.nhietdo_high, temperature)
            self.draw()
    def update_red_dots71(self, threshold_low, threshold_high, temperature):
        colored_dots = [line for line in self.axnhietdo71.lines if line.get_markerfacecolor() in ['red', 'blue']]
        for line in colored_dots:
            x_index = float(line.get_xdata())
            if (
                self.temperature[x_index] is None or
                self.temperature[x_index] == 0 or
                not (self.temperature[x_index] < float(threshold_low) or self.temperature[x_index] > float(threshold_high))
            ):
                line.remove()
        
        for i, temp in enumerate(self.temperature):
            if temp is not None and temp != 0:
                if  temp > float(threshold_high):
                    self.axnhietdo71.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.axnhietdo71.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif temp < float(threshold_low) :
                    self.axnhietdo71.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.axnhietdo71.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                    ha='center', va='bottom', color='red', fontsize=10)
        # Change the color of the last data point if it exceeds the thresholds
        if temperature is not None and temperature != 0:
            if temperature < float(threshold_low) or temperature > float(threshold_high):
                self.axnhietdo71.plot(len(self.temperature) - 1, temperature, 'ro')
        
        # Add legend to show the label for red dots (if they exist)
        if any(temp < float(threshold_low) or temp > float(threshold_high) for temp in self.temperature):
            self.axnhietdo71.legend(['Nhiệt độ'])
class MatplotlibCanvasDoam71(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdoam71, self.axdoamtram71 = plt.subplots()
        super().__init__(self.figdoam71)
        self.humidity = []
        self.time = []
        self.axdoamtram71.set_xlabel('Thời gian')
        self.axdoamtram71.set_ylabel('Độ ẩm')
        self.axdoamtram71.set_ylim(0, 100)
        self.data_count = 0
        self.doam_low = 40 
        self.doam_high = 70
        y_major_locator = MultipleLocator(10)  
        self.axdoamtram71.yaxis.set_major_locator(y_major_locator)
          

    def update_figureDoam71(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram71:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if doam_low is not None and doam_low != 0:
                self.doam_low = doam_low  
            if doam_high is not None and doam_high != 0:
                self.doam_high = doam_high 
            if humidity is not None and humidity != 0:  
                self.humidity.append(humidity)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.time.pop(0)
                    self.humidity.pop(0)
            self.axdoamtram71.clear()
            filtered_temperature = [temp for temp in self.humidity if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.humidity[i] is not None and self.humidity[i] != 0]

            if len(filtered_temperature) < 24:
                    self.axdoamtram71.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Độ ẩm')
                    self.axdoamtram71.set_xticks(range(len(filtered_temperature)))
                    self.axdoamtram71.set_xticklabels(filtered_time)
            else:
                    self.axdoamtram71.plot(range(24), filtered_temperature[-24:], '-o', label='Độ ẩm')
                    self.axdoamtram71.set_xticks(range(24))
                    self.axdoamtram71.set_xticklabels(filtered_time[-24:])

            self.axdoamtram71.set_xlim(0, 23)
            self.axdoamtram71.set_xlabel('Thời gian')
            self.axdoamtram71.set_ylabel('Độ ẩm')
            self.axdoamtram71.set_ylim(0, 100)
            y_major_locator = MultipleLocator(10)  
            self.axdoamtram71.yaxis.set_major_locator(y_major_locator)
            self.axdoamtram71.legend()

            self.axdoamtram71.axhline(self.doam_low, color='b', linestyle='--', label='Ngưỡng Độ ẩm thấp')
            self.axdoamtram71.axhline(self.doam_high, color='b', linestyle='--', label='Ngưỡng Độ ẩm cao')
            self.axdoamtram71.text(23, self.doam_low, int(self.doam_low), ha='right', va='bottom')
            self.axdoamtram71.text(23, self.doam_high, int(self.doam_high), ha='right', va='bottom')
            self.update_red_dots71(self.doam_low, self.doam_high, humidity)
            self.draw()

    def update_red_dots71(self, doam_low, doam_high, humidity):
        # Clear the previous red dots
        red_dots = [line for line in self.axdoamtram71.lines if line.get_color() == 'red']
        for line in red_dots:
            line.remove()
        for i, temp in enumerate(self.humidity):
                if temp is not None and temp != 0:
                    if  temp > float(doam_high):
                        self.axdoamtram71.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoamtram71.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                        ha='center', va='bottom', color='red', fontsize=10)
                    elif temp < float(doam_low) :
                        self.axdoamtram71.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoamtram71.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                        ha='center', va='bottom', color='red', fontsize=10)
        if humidity is not None and humidity != 0:
            if humidity < float(doam_low) or humidity > float(doam_high):
                self.axdoamtram71.plot(len(self.humidity) - 1, humidity, 'ro')
            if any(temp < float(doam_low) or temp > float(doam_high) for temp in self.humidity):
                self.axdoamtram71.legend(['Độ ẩm'])
class MatplotlibCanvasDienap171(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap171, self.axdienap1tram71 = plt.subplots()
        super().__init__(self.figdienap171)
        self.voltage_dc1 = []
        self.dienap_low= 47
        self.dienap_low1 =48
        self.dienap_high =58.5
        self.time = []
        self.axdienap1tram71.set_xlim(0, 23)
        self.axdienap1tram71.set_xlabel('Thời gian')
        self.axdienap1tram71.set_ylabel('Điện áp')
        self.axdienap1tram71.set_ylim(20, 60)  
        self.data_count = 0
        y_major_locator = MultipleLocator(5) 
        self.axdienap1tram71.yaxis.set_major_locator(y_major_locator)

    def update_figureDienap171(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                    voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram71:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high  
            if voltage_dc1 is not None and voltage_dc1 !=0:
                self.voltage_dc1.append(voltage_dc1)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc1.pop(0)
                    self.time.pop(0)
            self.axdienap1tram71.clear()  

            if len(self.voltage_dc1) < 24:
                self.axdienap1tram71.plot(range(len(self.voltage_dc1)), self.voltage_dc1, '-o', label='Điện áp DC1')
                self.axdienap1tram71.set_xticks(range(len(self.voltage_dc1)))
                self.axdienap1tram71.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap1tram71.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap1tram71.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap1tram71.set_xlim(0, 23)
                self.axdienap1tram71.set_xticklabels(self.time)
            else:
                self.axdienap1tram71.plot(range(24), self.voltage_dc1[-24:], '-o', label='Điện áp DC1')
                self.axdienap1tram71.set_xticks(range(24))
                self.axdienap1tram71.set_xlim(0, 23)
                self.axdienap1tram71.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap1tram71.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap1tram71.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap1tram71.set_xticklabels(self.time[-24:])
            self.axdienap1tram71.set_xlabel('Thời gian')
            self.axdienap1tram71.set_ylabel('Điện áp')
            self.axdienap1tram71.set_ylim(20, 60)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axdienap1tram71.yaxis.set_major_locator(y_major_locator)
            self.axdienap1tram71.text(23, self.dienap_low, int(self.dienap_low), ha='right', va='top')
            self.axdienap1tram71.text(23, self.dienap_low1, int(self.dienap_low1), ha='right', va='bottom')
            self.axdienap1tram71.text(23, self.dienap_high, int(self.dienap_high), ha='right', va='bottom')
            self.axdienap1tram71.legend()
            self.update_red_dots171(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc1)
            self.draw()
    def update_red_dots171(self, dienap_low, dienap_high,dienap_low1, voltage_dc1):
        dots = [line for line in self.axdienap1tram71.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc1):
            if voltage is not None and voltage != 0:
                if voltage < float(dienap_low1):
                    self.axdienap1tram71.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng thấp 1)')
                    self.axdienap1tram71.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < float(dienap_low):
                    self.axdienap1tram71.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > float(dienap_high):
                    self.axdienap1tram71.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.axdienap1tram71.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.axdienap1tram71.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc1 is not None and voltage_dc1 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc1
            if voltage_dc1 < float(dienap_low1):
                self.axdienap1tram71.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.axdienap1tram71.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc1 < float(dienap_low):
                self.axdienap1tram71.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'go')
            elif voltage_dc1 > float(dienap_high):
                self.axdienap1tram71.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.axdienap1tram71.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.axdienap1tram71.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'bo')
class MatplotlibCanvasDienap271(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap271, self.axdienap2tram271 = plt.subplots()
        super().__init__(self.figdienap271)
        self.voltage_dc2 = []
        self.dienap_low= 47
        self.dienap_low1 =48
        self.dienap_high =58.5
        self.time = []
        self.axdienap2tram271.set_xlim(0, 23)
        self.axdienap2tram271.set_xlabel('Thời gian')
        self.axdienap2tram271.set_ylabel('Điện áp')
        self.axdienap2tram271.set_ylim(20, 60)  
        y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
        self.axdienap2tram271.yaxis.set_major_locator(y_major_locator)
        self.data_count = 0

    def update_figureDienap271(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram71:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high  
            if voltage_dc2 is not None and voltage_dc2 !=0:
                self.voltage_dc2.append(voltage_dc2)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc2.pop(0)
                    self.time.pop(0)
            self.axdienap2tram271.clear()  

            if len(self.voltage_dc2) < 24:
                self.axdienap2tram271.plot(range(len(self.voltage_dc2)), self.voltage_dc2, '-o', label='Điện áp DC2')
                self.axdienap2tram271.set_xticks(range(len(self.voltage_dc2)))
                self.axdienap2tram271.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap2tram271.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap2tram271.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap2tram271.set_xlim(0, 23)
                self.axdienap2tram271.set_xticklabels(self.time)
            else:
                self.axdienap2tram271.plot(range(24), self.voltage_dc2[-24:], '-o', label='Điện áp DC2')
                self.axdienap2tram271.set_xticks(range(24))
                self.axdienap2tram271.set_xlim(0, 23)
                self.axdienap2tram271.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap2tram271.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap2tram271.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap2tram271.set_xticklabels(self.time[-24:])
            self.axdienap2tram271.set_xlabel('Thời gian')
            self.axdienap2tram271.set_ylabel('Điện áp')
            self.axdienap2tram271.set_ylim(20, 60)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axdienap2tram271.yaxis.set_major_locator(y_major_locator)
            self.axdienap2tram271.text(23, self.dienap_low, int(self.dienap_low), ha='right', va='top')
            self.axdienap2tram271.text(23, self.dienap_low1, int(self.dienap_low1), ha='right', va='bottom')
            self.axdienap2tram271.text(23, self.dienap_high, int(self.dienap_high), ha='right', va='bottom')
            self.axdienap2tram271.legend()
            self.update_red_dots271(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc2)
            self.draw()
    def update_red_dots271(self, dienap_low, dienap_high,dienap_low1, voltage_dc2):
        dots = [line for line in self.axdienap2tram271.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc2):
            if voltage is not None and voltage != 0:
                if voltage < float(dienap_low1):
                    self.axdienap2tram271.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng thấp 1)')
                    self.axdienap2tram271.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < float(dienap_low):
                    self.axdienap2tram271.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > float(dienap_high):
                    self.axdienap2tram271.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.axdienap2tram271.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.axdienap2tram271.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc2 is not None and voltage_dc2 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc2
            if voltage_dc2 < float(dienap_low1):
                self.axdienap2tram271.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.axdienap2tram271.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc2 < float(dienap_low):
                self.axdienap2tram271.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'go')
            elif voltage_dc2 > float(dienap_high):
                self.axdienap2tram271.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.axdienap2tram271.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.axdienap2tram271.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'bo')
#tram78--------------------------------------------------------------------------------------------------------------------------------
class MatplotlibCanvasNhietdo76(FigureCanvas):
    
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.fignhietdo76, self.axnhietdo76 = plt.subplots()
        super().__init__(self.fignhietdo76)
        self.temperature =[]
        self.time =[]
        self.axnhietdo76.set_xlabel('Thời gian')
        self.axnhietdo76.set_ylabel('Nhiệt độ')
        self.axnhietdo76.set_ylim(0, 50)
        self.data_count = 0
        self.nhietdo_lower = 20
        self.nhietdo_high = 25
        y_major_locator = MultipleLocator(5)  
        self.axnhietdo76.yaxis.set_major_locator(y_major_locator)
       
    def update_figureNhietdo76(self, client_address, temperature, humidity, light,  voltage_dc1, voltage_dc2,
                                    voltage_ac, voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low, dienap_high):
        if client_address == tram76:
            if nhietdo_lower is not None and nhietdo_lower != 0:
                self.nhietdo_lower = nhietdo_lower 
            if nhietdo_high is not None and nhietdo_high != 0:
                    self.nhietdo_high = nhietdo_high  # Cập nhật ngưỡng cao nếu có giá trị gửi lên
            current_time = datetime.datetime.now().strftime('%H:%M')
     
            if temperature is not None and temperature != 0:  # Kiểm tra giá trị nhiệt độ không phải là None hoặc 0
                self.temperature.append(float(temperature))
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.temperature.pop(0)
                    self.time.pop(0)
            self.axnhietdo76.clear()

            # Filter out None values from temperature and corresponding time
            filtered_temperature = [temp for temp in self.temperature if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.temperature[i] is not None and self.temperature[i] != 0]

            if len(filtered_temperature) < 24:
                self.axnhietdo76.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Nhiệt độ')
                self.axnhietdo76.set_xticks(range(len(filtered_temperature)))
                self.axnhietdo76.set_xticklabels(filtered_time)
              
            else:
                self.axnhietdo76.plot(range(24), filtered_temperature[-24:], '-o', label='Nhiệt độ')
                self.axnhietdo76.set_xticks(range(24))
                self.axnhietdo76.set_xticklabels(filtered_time[-24:])
              

            self.axnhietdo76.set_xlim(0, 23)
            self.axnhietdo76.set_xlabel('Thời gian')
            self.axnhietdo76.set_ylabel('Nhiệt độ')
            self.axnhietdo76.set_ylim(0, 50)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axnhietdo76.yaxis.set_major_locator(y_major_locator)
            # Draw 
            self.axnhietdo76.axhline(self.nhietdo_lower, color='b', linestyle='--', label='Ngưỡng nhiệt độ thấp')
            self.axnhietdo76.axhline(self.nhietdo_high, color='b', linestyle='--', label='Ngưỡng nhiệt độ cao')
            self.axnhietdo76.text(23, self.nhietdo_lower, int(self.nhietdo_lower), ha='right', va='bottom')
            self.axnhietdo76.text(23, self.nhietdo_high, int(self.nhietdo_high), ha='right', va='bottom')
            self.axnhietdo76.legend()
         
            self.update_red_dots76(self.nhietdo_lower, self.nhietdo_high, temperature)
            self.draw()
    def update_red_dots76(self, threshold_low, threshold_high, temperature):
        colored_dots = [line for line in self.axnhietdo76.lines if line.get_markerfacecolor() in ['red', 'blue']]
        for line in colored_dots:
            x_index = float(line.get_xdata())
            if (
                self.temperature[x_index] is None or
                self.temperature[x_index] == 0 or
                not (self.temperature[x_index] < float(threshold_low) or self.temperature[x_index] > float(threshold_high))
            ):
                line.remove()
        
        for i, temp in enumerate(self.temperature):
            if temp is not None and temp != 0:
                if  temp > float(threshold_high):
                    self.axnhietdo76.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.axnhietdo76.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif temp < float(threshold_low) :
                    self.axnhietdo76.plot(i, temp, 'ro', label='Nhiệt độ')
                    self.axnhietdo76.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                    ha='center', va='bottom', color='red', fontsize=10)
        # Change the color of the last data point if it exceeds the thresholds
        if temperature is not None and temperature != 0:
            if temperature < float(threshold_low) or temperature > float(threshold_high):
                self.axnhietdo76.plot(len(self.temperature) - 1, temperature, 'ro')
        
        # Add legend to show the label for red dots (if they exist)
        if any(temp < float(threshold_low) or temp > float(threshold_high) for temp in self.temperature):
            self.axnhietdo76.legend(['Nhiệt độ'])
class MatplotlibCanvasDoam76(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdoam76, self.axdoamtram76 = plt.subplots()
        super().__init__(self.figdoam76)
        self.humidity = []
        self.time = []
        self.axdoamtram76.set_xlabel('Thời gian')
        self.axdoamtram76.set_ylabel('Độ ẩm')
        self.axdoamtram76.set_ylim(0, 100)
        self.data_count = 0
        self.doam_low = 40 
        self.doam_high = 70
        y_major_locator = MultipleLocator(10)  
        self.axdoamtram76.yaxis.set_major_locator(y_major_locator)
          

    def update_figureDoam76(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram76:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if doam_low is not None and doam_low != 0:
                self.doam_low = doam_low  
            if doam_high is not None and doam_high != 0:
                self.doam_high = doam_high 
            if humidity is not None and humidity != 0:  
                self.humidity.append(humidity)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.time.pop(0)
                    self.humidity.pop(0)
            self.axdoamtram76.clear()
            filtered_temperature = [temp for temp in self.humidity if temp is not None and temp != 0]
            filtered_time = [time for i, time in enumerate(self.time) if self.humidity[i] is not None and self.humidity[i] != 0]

            if len(filtered_temperature) < 24:
                    self.axdoamtram76.plot(range(len(filtered_temperature)), filtered_temperature, '-o', label='Độ ẩm')
                    self.axdoamtram76.set_xticks(range(len(filtered_temperature)))
                    self.axdoamtram76.set_xticklabels(filtered_time)
            else:
                    self.axdoamtram76.plot(range(24), filtered_temperature[-24:], '-o', label='Độ ẩm')
                    self.axdoamtram76.set_xticks(range(24))
                    self.axdoamtram76.set_xticklabels(filtered_time[-24:])

            self.axdoamtram76.set_xlim(0, 23)
            self.axdoamtram76.set_xlabel('Thời gian')
            self.axdoamtram76.set_ylabel('Độ ẩm')
            self.axdoamtram76.set_ylim(0, 100)
            y_major_locator = MultipleLocator(10)  
            self.axdoamtram76.yaxis.set_major_locator(y_major_locator)
            self.axdoamtram76.legend()

            self.axdoamtram76.axhline(self.doam_low, color='b', linestyle='--', label='Ngưỡng Độ ẩm thấp')
            self.axdoamtram76.axhline(self.doam_high, color='b', linestyle='--', label='Ngưỡng Độ ẩm cao')
            self.axdoamtram76.text(23, self.doam_low, int(self.doam_low), ha='right', va='bottom')
            self.axdoamtram76.text(23, self.doam_high, int(self.doam_high), ha='right', va='bottom')
            self.update_red_dots76(self.doam_low, self.doam_high, humidity)
            self.draw()

    def update_red_dots76(self, doam_low, doam_high, humidity):
        # Clear the previous red dots
        red_dots = [line for line in self.axdoamtram76.lines if line.get_color() == 'red']
        for line in red_dots:
            line.remove()
        for i, temp in enumerate(self.humidity):
                if temp is not None and temp != 0:
                    if  temp > float(doam_high):
                        self.axdoamtram76.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoamtram76.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, 5),
                                        ha='center', va='bottom', color='red', fontsize=10)
                    elif temp < float(doam_low) :
                        self.axdoamtram76.plot(i, temp, 'ro', label='Độ ẩm')
                        self.axdoamtram76.annotate(f'{temp:.2f}', (i, temp), textcoords='offset points', xytext=(0, -17),
                                        ha='center', va='bottom', color='red', fontsize=10)
        if humidity is not None and humidity != 0:
            if humidity < float(doam_low) or humidity > float(doam_high):
                self.axdoamtram76.plot(len(self.humidity) - 1, humidity, 'ro')
            if any(temp < float(doam_low) or temp > float(doam_high) for temp in self.humidity):
                self.axdoamtram76.legend(['Độ ẩm'])
class MatplotlibCanvasDienap176(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap176, self.axdienap1tram176 = plt.subplots()
        super().__init__(self.figdienap176)
        self.voltage_dc1 = []
        self.dienap_low= 47
        self.dienap_low1 =48
        self.dienap_high =58.5
        self.time = []
        self.axdienap1tram176.set_xlim(0, 23)
        self.axdienap1tram176.set_xlabel('Thời gian')
        self.axdienap1tram176.set_ylabel('Điện áp')
        self.axdienap1tram176.set_ylim(20, 60)  
        self.data_count = 0
        y_major_locator = MultipleLocator(5) 
        self.axdienap1tram176.yaxis.set_major_locator(y_major_locator)

    def update_figureDienap176(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                    voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                    dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram76:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high  
            if voltage_dc1 is not None and voltage_dc1 !=0:
                self.voltage_dc1.append(voltage_dc1)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc1.pop(0)
                    self.time.pop(0)
            self.axdienap1tram176.clear()  

            if len(self.voltage_dc1) < 24:
                self.axdienap1tram176.plot(range(len(self.voltage_dc1)), self.voltage_dc1, '-o', label='Điện áp DC1')
                self.axdienap1tram176.set_xticks(range(len(self.voltage_dc1)))
                self.axdienap1tram176.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap1tram176.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap1tram176.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap1tram176.set_xlim(0, 23)
                self.axdienap1tram176.set_xticklabels(self.time)
            else:
                self.axdienap1tram176.plot(range(24), self.voltage_dc1[-24:], '-o', label='Điện áp DC1')
                self.axdienap1tram176.set_xticks(range(24))
                self.axdienap1tram176.set_xlim(0, 23)
                self.axdienap1tram176.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap1tram176.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap1tram176.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap1tram176.set_xticklabels(self.time[-24:])
            self.axdienap1tram176.set_xlabel('Thời gian')
            self.axdienap1tram176.set_ylabel('Điện áp')
            self.axdienap1tram176.set_ylim(20, 60)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axdienap1tram176.yaxis.set_major_locator(y_major_locator)
            self.axdienap1tram176.text(23, self.dienap_low, int(self.dienap_low), ha='right', va='top')
            self.axdienap1tram176.text(23, self.dienap_low1, int(self.dienap_low1), ha='right', va='bottom')
            self.axdienap1tram176.text(23, self.dienap_high, int(self.dienap_high), ha='right', va='bottom')
            self.axdienap1tram176.legend()
            self.update_red_dots176(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc1)
            self.draw()
    def update_red_dots176(self, dienap_low, dienap_high,dienap_low1, voltage_dc1):
        dots = [line for line in self.axdienap1tram176.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc1):
            if voltage is not None and voltage != 0:
                if voltage < float(dienap_low1):
                    self.axdienap1tram176.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng thấp 1)')
                    self.axdienap1tram176.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < float(dienap_low):
                    self.axdienap1tram176.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > float(dienap_high):
                    self.axdienap1tram176.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.axdienap1tram176.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.axdienap1tram176.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc1 is not None and voltage_dc1 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc1
            if voltage_dc1 < float(dienap_low1):
                self.axdienap1tram176.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.axdienap1tram176.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc1 < float(dienap_low):
                self.axdienap1tram176.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'go')
            elif voltage_dc1 > float(dienap_high):
                self.axdienap1tram176.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'ro')
                self.axdienap1tram176.annotate(f'{voltage_dc1:.2f}', (len(self.voltage_dc1) - 1, voltage_dc1), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.axdienap1tram176.plot(len(self.voltage_dc1) - 1, voltage_dc1, 'bo')
class MatplotlibCanvasDienap276(FigureCanvas):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    def __init__(self):
        self.figdienap276, self.axdienap2tram276 = plt.subplots()
        super().__init__(self.figdienap276)
        self.voltage_dc2 = []
        self.dienap_low= 47
        self.dienap_low1 =48
        self.dienap_high =58.5
        self.time = []
        self.axdienap2tram276.set_xlim(0, 23)
        self.axdienap2tram276.set_xlabel('Thời gian')
        self.axdienap2tram276.set_ylabel('Điện áp')
        self.axdienap2tram276.set_ylim(20, 60)  
        y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
        self.axdienap2tram276.yaxis.set_major_locator(y_major_locator)
        self.data_count = 0

    def update_figureDienap276(self,client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time):
        if client_address == tram76:
            current_time = datetime.datetime.now().strftime('%H:%M')
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low  
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1  
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high  
            if voltage_dc2 is not None and voltage_dc2 !=0:
                self.voltage_dc2.append(voltage_dc2)
                self.time.append(current_time)
                self.data_count += 1
                if self.data_count > 24:
                    self.voltage_dc2.pop(0)
                    self.time.pop(0)
            self.axdienap2tram276.clear()  

            if len(self.voltage_dc2) < 24:
                self.axdienap2tram276.plot(range(len(self.voltage_dc2)), self.voltage_dc2, '-o', label='Điện áp DC2')
                self.axdienap2tram276.set_xticks(range(len(self.voltage_dc2)))
                self.axdienap2tram276.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap2tram276.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap2tram276.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap2tram276.set_xlim(0, 23)
                self.axdienap2tram276.set_xticklabels(self.time)
            else:
                self.axdienap2tram276.plot(range(24), self.voltage_dc2[-24:], '-o', label='Điện áp DC2')
                self.axdienap2tram276.set_xticks(range(24))
                self.axdienap2tram276.set_xlim(0, 23)
                self.axdienap2tram276.axhline(self.dienap_low, color='r', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 1')
                self.axdienap2tram276.axhline(self.dienap_low1, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC thấp 2')
                self.axdienap2tram276.axhline(self.dienap_high, color='b', linestyle='--', label='Ngưỡng quá Điện áp DC cao')
                self.axdienap2tram276.set_xticklabels(self.time[-24:])
            self.axdienap2tram276.set_xlabel('Thời gian')
            self.axdienap2tram276.set_ylabel('Điện áp')
            self.axdienap2tram276.set_ylim(20, 60)
            y_major_locator = MultipleLocator(5)  # Khoảng cách là 5
            self.axdienap2tram276.yaxis.set_major_locator(y_major_locator)
            self.axdienap2tram276.text(23, self.dienap_low, int(self.dienap_low), ha='right', va='top')
            self.axdienap2tram276.text(23, self.dienap_low1, int(self.dienap_low1), ha='right', va='bottom')
            self.axdienap2tram276.text(23, self.dienap_high, int(self.dienap_high), ha='right', va='bottom')
            self.axdienap2tram276.legend()
            self.update_red_dots276(self.dienap_low, self.dienap_high,self.dienap_low1, voltage_dc2)
            self.draw()
    def update_red_dots276(self, dienap_low, dienap_high,dienap_low1, voltage_dc2):
        dots = [line for line in self.axdienap2tram276.lines if line.get_color() in ['red', 'green']]

        for line in dots:
            line.remove()

        # Draw dots based on the voltage_dc1 and thresholds
        for i, voltage in enumerate(self.voltage_dc2):
            if voltage is not None and voltage != 0:
                if voltage < float(dienap_low1):
                    self.axdienap2tram276.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng thấp 1)')
                    self.axdienap2tram276.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, -15),
                                    ha='center', va='bottom', color='red', fontsize=10)
                elif voltage < float(dienap_low):
                    self.axdienap2tram276.plot(i, voltage, 'go', label='Điện áp DC (quá ngưỡng thấp)')
                elif voltage > float(dienap_high):
                    self.axdienap2tram276.plot(i, voltage, 'ro', label='Điện áp DC (quá ngưỡng cao)')
                    self.axdienap2tram276.annotate(f'{voltage:.2f}', (i, voltage), textcoords='offset points', xytext=(0, 5),
                                    ha='center', va='bottom', color='red', fontsize=10)
                else:
                    self.axdienap2tram276.plot(i, voltage, 'bo', label='Điện áp DC (trong ngưỡng)')

        if voltage_dc2 is not None and voltage_dc2 != 0:  
            # Change the color of the last data point if it exceeds the thresholds for voltage_dc2
            if voltage_dc2 < float(dienap_low1):
                self.axdienap2tram276.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.axdienap2tram276.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, -15),
                                ha='center', va='bottom', color='red', fontsize=10)
            elif voltage_dc2 < float(dienap_low):
                self.axdienap2tram276.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'go')
            elif voltage_dc2 > float(dienap_high):
                self.axdienap2tram276.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'ro')
                self.axdienap2tram276.annotate(f'{voltage_dc2:.2f}', (len(self.voltage_dc2) - 1, voltage_dc2), textcoords='offset points', xytext=(0, 5),
                                ha='center', va='bottom', color='red', fontsize=10)
            else:
                self.axdienap2tram276.plot(len(self.voltage_dc2) - 1, voltage_dc2, 'bo')
