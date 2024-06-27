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

from server import *
from modules.data import *
from modules.problem import Problem
from modules.ui_main import *

class FuntionData(QMainWindow):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    global bit_humi_a70,bit_temp_a70,bit_ac1_a70,bit_ac2_a70,bit_dc1_a70,bit_dc2_a70,bit_humi_a45,bit_temp_a45,bit_ac1_a45,bit_ac2_a45,bit_dc1_a45,bit_dc2_a45,bit_canh_bao,bit_coi
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        global widgets
        widgets = self.ui
        self.current_widget = None
        self.problem_dialog = None
        self.problem_dialog_2 =None
        self.selected_start_date = None
        self.selected_end_date = None
        self.active_button = None  
        self.nhietdo_lower = 20
        self.nhietdo_high = 25
        self.doam_low = 40  
        self.doam_high = 70
        self.dienap_low =47
        self.dienap_low1 =48
        self.dienap_high =58.5
        self.problem_dialog = QDialog()
        self.problem_dialog_2 = QDialog()
        self.problem = Problem()
        self.problem.setupUi(self.problem_dialog_2)
        self.problem.setupUi(self.problem_dialog)
        self.problem_dialog.exec()
        self.problem_dialog_2.exec()

        
    def update_nhietdo_values(self, client_address, temperature, humidity, light,fire, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high,current_time):
        # Update nhietdo_lower and nhietdo_high based on the values received from the client\
        if nhietdo_lower is not None and nhietdo_lower !=0:
            self.nhietdo_lower = nhietdo_lower
        if nhietdo_high is not None and nhietdo_high !=0 :
            self.nhietdo_high = nhietdo_high
        if doam_low is not None and doam_low !=0:
            self.doam_low = doam_low
        if doam_high is not None and doam_high !=0:
            self.doam_high = doam_high
        if dienap_low is not None and dienap_low !=0 :
            self.dienap_low = dienap_low
        if dienap_low1 is not None and dienap_low1 !=0 :
            self.dienap_low1 = dienap_low1
        if dienap_high is not None and dienap_high !=0 :
            self.dienap_high = dienap_high
    
       
    def fecth_and_popula_data_temp(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="suconhietdo"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, temperature, nhietdo_lower, nhietdo_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND temperature IS NOT NULL ;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            print(result)
            self.populate_temperature_table(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as error:
            print("Error fetching data from MySQL:", error)
    def populate_temperature_table(self, data):
        self.ui.tableWidget_nhietdo_2.clearContents()
        self.ui.tableWidget_nhietdo_2.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None
        global bit_temp_a70,bit_coi
        for row_idx, (time, temperature, nhietdo_lower, nhietdo_high ) in enumerate(data):
            if time is None or temperature is None or nhietdo_lower is None or nhietdo_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")

            if nhietdo_lower is not None and nhietdo_high is not None:
                nhietdo_lower = self.nhietdo_lower  
                nhietdo_high = self.nhietdo_high  
            print(nhietdo_lower,nhietdo_high)
            if float(nhietdo_lower) <= float(temperature) <= float(nhietdo_high):
                alert_type = None
               
            elif float(temperature) < nhietdo_lower:
                alert_type = "Sự cố nhiệt độ thấp"
          
            elif float(temperature) > nhietdo_high:
                alert_type = "Sự cố nhiệt độ cao"

    
            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_nhietdo_2.rowCount()
                    self.ui.tableWidget_nhietdo_2.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_nhietdo_2.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_nhietdo_2.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_nhietdo_2.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                # Tìm chỉ số của sự cố khác sau sự cố hiện tại
                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_temp, next_lower, next_high = next_row

                    if float(next_lower) <= float(next_temp) <= float(next_high):
                        next_alert_type = None
                    elif float(next_temp) < float(next_lower):
                        next_alert_type = "Sự cố nhiệt độ thấp"
                    elif float(next_temp) > float(next_high):
                        next_alert_type = "Sự cố nhiệt độ cao"

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                # Kiểm tra nếu không có sự cố khác xảy ra sau sự cố hiện tại
                # và dữ liệu thỏa mãn hoặc không thỏa mãn sau sự cố hiện tại
                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_temp, next_lower, next_high = next_row

                    if float(next_lower) <= float(next_temp) <= float(next_high):
                        next_alert_type = None
                    elif float(next_temp) < float(next_lower):
                        next_alert_type = "Sự cố nhiệt độ thấp"
                    elif float(next_temp) > float(next_high):
                        next_alert_type = "Sự cố nhiệt độ cao"
                    

        # Adding the last row if there's an ongoing alert
        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_nhietdo_2.rowCount()
            self.ui.tableWidget_nhietdo_2.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_nhietdo_2.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_nhietdo_2.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_nhietdo_2.setItem(row_position, 2, item_next_data_time)
            
            # Check if the last data entry is None and add its time to column 3
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_nhietdo_2.rowCount()
                        self.ui.tableWidget_nhietdo_2.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_nhietdo_2.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_nhietdo_2.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_nhietdo_2.setItem(row_position, 2, item_next_data_time)         
    def fecth_and_popula_data_hum(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodoam"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, humidity,doam_low,doam_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND humidity IS NOT NULL;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            self.populate_temperature_table_doam(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as error:
            print("Error fetching data from MySQL:", error)
    def populate_temperature_table_doam(self, data):
        self.ui.tableWidget_doam_2.clearContents()
        self.ui.tableWidget_doam_2.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, humidity, doam_low, doam_high ) in enumerate(data):
            if time is None or humidity is None or doam_low is None or doam_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")

            if doam_low is not None and doam_high is not None:
                doam_low = self.doam_low  
                doam_high = self.doam_high  
            print(doam_low,doam_high)
            if float(doam_low) <= float(humidity) <= float(doam_high):
                alert_type = None
            elif float(humidity) < doam_low:
                alert_type = "Sự cố độ ẩm thấp"
            elif float(humidity) > doam_high:
                alert_type = "Sự cố độ ẩm cao"
    
            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_doam_2.rowCount()
                    self.ui.tableWidget_doam_2.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_doam_2.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_doam_2.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_doam_2.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                # Tìm chỉ số của sự cố khác sau sự cố hiện tại
                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_temp, next_lower, next_high = next_row

                    if str(next_lower) <= str(next_temp) <= str(next_high):
                        next_alert_type = None
                    elif str(next_temp) < str(next_lower):
                        next_alert_type = "Sự cố độ ẩm thấp"
                    elif str(next_temp) > str(next_high):
                        next_alert_type = "Sự cố độ ẩm cao"

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                # Kiểm tra nếu không có sự cố khác xảy ra sau sự cố hiện tại
                # và dữ liệu thỏa mãn hoặc không thỏa mãn sau sự cố hiện tại
                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_temp, next_lower, next_high = next_row

                    if str(next_lower) <= str(next_temp) <= str(next_high):
                        next_alert_type = None
                    elif str(next_temp) < str(next_lower):
                        next_alert_type = "Sự cố độ ẩm thấp"
                    elif str(next_temp) > str(next_high):
                        next_alert_type = "Sự cố độ ẩm cao"
                    if next_alert_type is not None:
                        next_data_time = next_time

        # Adding the last row if there's an ongoing alert
        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_doam_2.rowCount()
            self.ui.tableWidget_doam_2.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_doam_2.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_doam_2.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_doam_2.setItem(row_position, 2, item_next_data_time)
            
            # Check if the last data entry is None and add its time to column 3
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_doam_2.rowCount()
                        self.ui.tableWidget_doam_2.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_doam_2.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_doam_2.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_doam_2.setItem(row_position, 2, item_next_data_time) 
    def fecth_and_popula_data_ac1(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucoac1"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, voltage_ac1, dienapac_low, dienapac_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND voltage_ac1 IS NOT NULL;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            
            self.populate_temperature_table_ac1(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as error:
            print("Error fetching data from MySQL:", error)
    def populate_temperature_table_ac1(self, data):
        self.ui.tableWidget_ac1.clearContents()
        self.ui.tableWidget_ac1.setRowCount(0)
        next_alert_type = None 
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None
        
        for row_idx, (time, voltage_ac, dienapac_low, dienapac_high) in enumerate(data):
            if time is None or voltage_ac is None or dienapac_low is None or dienapac_high is None:
                continue
            
            
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            
            if float(voltage_ac) == float(dienapac_low):
                alert_type = "Sự cố AC1 mất"
            elif float(voltage_ac) == float(dienapac_high):
                alert_type = None
            
            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_ac1.rowCount()
                    self.ui.tableWidget_ac1.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_ac1.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_ac1.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_ac1.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if str(next_voltage_ac) == str(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif str(next_voltage_ac) == str(next_voltage_ac_high):
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if str(next_voltage_ac) == str(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif str(next_voltage_ac) == str(next_voltage_ac_high):
                        next_alert_type = None
                    if next_alert_type is not None:
                        next_data_time = next_time

        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_ac1.rowCount()
            self.ui.tableWidget_ac1.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_ac1.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_ac1.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_ac1.setItem(row_position, 2, item_next_data_time)     
    def fecth_and_popula_data_ac2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucoac2"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, voltage_ac2, dienapac_low, dienapac_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND voltage_ac2 IS NOT NULL;"
            
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()

            self.populate_temperature_table_ac2(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as error:
            print("Error fetching data from MySQL:", error)
    def populate_temperature_table_ac2(self, data):
        self.ui.tableWidget_ac2.clearContents()
        self.ui.tableWidget_ac2.setRowCount(0)
        next_alert_type = None 
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None
        
        for row_idx, (time, voltage_ac2, dienapac_low, dienapac_high) in enumerate(data):
            if time is None or voltage_ac2 is None or dienapac_low is None or dienapac_high is None:
                continue
            
            
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")

            if float(voltage_ac2) == float(dienapac_low):
                alert_type = "Sự cố AC2 mất"
            elif float(voltage_ac2) == float(dienapac_high):
                alert_type = None
            
            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_ac2.rowCount()
                    self.ui.tableWidget_ac2.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_ac2.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_ac2.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_ac2.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if str(next_voltage_ac) == str(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif str(next_voltage_ac) == str(next_voltage_ac_high):
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if str(next_voltage_ac) == str(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif str(next_voltage_ac) == str(next_voltage_ac_high):
                        next_alert_type = None
                    if next_alert_type is not None:
                        next_data_time = next_time

        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_ac2.rowCount()
            self.ui.tableWidget_ac2.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_ac2.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_ac2.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_ac2.setItem(row_position, 2, item_next_data_time)
    def fecth_and_popula_data_dc1(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodc1"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, voltage_dc1, dienap_low,dienap_low1, dienap_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND voltage_dc1 IS NOT NULL;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            self.populate_table_dc1(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    def populate_table_dc1(self, data):
        self.ui.tableWidget_dc1_2.clearContents()
        self.ui.tableWidget_dc1_2.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None
        
        for row_idx, (time, voltage_dc1, dienap_low,dienap_low1, dienap_high ) in enumerate(data):
            if time is None or voltage_dc1 is None or dienap_low is None or dienap_low1 is None or dienap_high is None:
                continue
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            # print(self.data)
            dienap_low = self.dienap_low  
            dienap_low1 = self.dienap_low1
            dienap_high = self.dienap_high 
            if float(dienap_low) <= float(voltage_dc1) < float(dienap_low1):
                alert_type = "Sự cố điện áp DC1 mức 1"
            elif float(voltage_dc1) < float(dienap_low1):
                alert_type = "Sự cố điện áp DC1 mức 2"
            elif float(voltage_dc1) > float(dienap_high):
                alert_type = "Sự cố điện áp DC1 cao"
            else:
                alert_type = None

            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_dc1_2.rowCount()
                    self.ui.tableWidget_dc1_2.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_dc1_2.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_dc1_2.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_dc1_2.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_voltage_dc1, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc1) < float(next_dienap_low1):
                        next_alert_type = "Sự cố điện áp DC1 mức 1"
                    elif float(next_voltage_dc1) < float(next_dienap_low):
                        next_alert_type = "Sự cố điện áp DC1 mức 2"
                    elif float(next_voltage_dc1) > float(next_dienap_high):
                        next_alert_type = "Sự cố điện áp DC1 cao"
                    else:
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_dc1, next_dienap_low, next_dienap_low1, next_dienap_high = next_row
                    if float(next_dienap_low) <= float(next_voltage_dc1) < float(next_dienap_low1):
                        next_alert_type = "Sự cố điện áp DC1 mức 1"
                    elif float(next_voltage_dc1) < float(next_dienap_low):
                        next_alert_type = "Sự cố điện áp DC1 mức 2"
                    elif float(next_voltage_dc1) > float(next_dienap_high):
                        next_alert_type = "Sự cố điện áp DC1 cao"
                    else:
                        next_alert_type = None
                    if next_alert_type is not None:
                        next_data_time = next_time

        # Adding the last row if there's an ongoing alert
        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_dc1_2.rowCount()
            self.ui.tableWidget_dc1_2.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_dc1_2.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_dc1_2.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_dc1_2.setItem(row_position, 2, item_next_data_time)
            
            # Check if the last data entry is None and add its time to column 3
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_dc1_2.rowCount()
                        self.ui.tableWidget_dc1_2.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_dc1_2.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_dc1_2.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_dc1_2.setItem(row_position, 2, item_next_data_time) 
    def fecth_and_popula_data_dc2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodc2"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, voltage_dc2, dienap_low,dienap_low1, dienap_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND voltage_dc2 IS NOT NULL;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            self.populate_temperature_table_dc2(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    def populate_temperature_table_dc2(self, data):
        self.ui.tableWidget_dc2_2.clearContents()
        self.ui.tableWidget_dc2_2.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None
        
        for row_idx, (time, voltage_dc2, dienap_low,dienap_low1, dienap_high ) in enumerate(data):
            if time is None or voltage_dc2 is None or dienap_low is None or dienap_low1 is None or dienap_high is None:
                continue
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            
            dienap_low = self.dienap_low  
            dienap_low1 = self.dienap_low1
            dienap_high = self.dienap_high 
            if float(dienap_low) <= float(voltage_dc2) < float(dienap_low1):
                alert_type = "Sự cố điện áp DC2 mức 1"
            elif float(voltage_dc2) < float(dienap_low1):
                alert_type = "Sự cố điện áp DC2 mức 2"
            elif float(voltage_dc2) > float(dienap_high):
                alert_type = "Sự cố điện áp DC2 cao"
            else:
                alert_type = None

            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_dc2_2.rowCount()
                    self.ui.tableWidget_dc2_2.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_dc2_2.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_dc2_2.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_dc2_2.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) < float(next_dienap_low1):
                        next_alert_type = "Sự cố điện áp DC1 mức 1"
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = "Sự cố điện áp DC1 mức 2"
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = "Sự cố điện áp DC1 cao"
                    else:
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) < float(next_dienap_low1):
                        next_alert_type = "Sự cố điện áp DC1 mức 1"
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = "Sự cố điện áp DC1 mức 2"
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = "Sự cố điện áp DC1 cao"
                    else:
                        next_alert_type = None
                    if next_alert_type is not None:
                        next_data_time = next_time

        # Adding the last row if there's an ongoing alert
        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_dc2_2.rowCount()
            self.ui.tableWidget_dc2_2.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_dc2_2.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_dc2_2.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_dc2_2.setItem(row_position, 2, item_next_data_time)
            
            # Check if the last data entry is None and add its time to column 3
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_dc2_2.rowCount()
                        self.ui.tableWidget_dc2_2.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_dc2_2.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_dc2_2.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_dc2_2.setItem(row_position, 2, item_next_data_time) 
    def export_to_exceltemp(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_nhietdo_2.rowCount()):
                        temperature_item = self.ui.tableWidget_nhietdo_2.item(row, 0)
                        time_item = self.ui.tableWidget_nhietdo_2.item(row, 1)
                        time_end = self.ui.tableWidget_nhietdo_2.item(row,2)
                        if temperature_item and time_item:
                            temperature = temperature_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([temperature, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.") 
    def export_to_excelhum(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_doam_2.rowCount()):
                        humidity_item = self.ui.tableWidget_doam_2.item(row, 0)
                        time_item = self.ui.tableWidget_doam_2.item(row, 1)
                        time_end = self.ui.tableWidget_doam_2.item(row,2)
                        if humidity_item and time_item:
                            humidity = humidity_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([humidity, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.") 
    def export_to_exceldc1(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_dc1_2.rowCount()):
                        temperature_item = self.ui.tableWidget_dc1_2.item(row, 0)
                        time_item = self.ui.tableWidget_dc1_2.item(row, 1)
                        time_end = self.ui.tableWidget_dc1_2.item(row,2)
                        if temperature_item and time_item:
                            temperature = temperature_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([temperature, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.")
    def export_to_exceldc2(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_dc2_2.rowCount()):
                        voltage_dc2_item = self.ui.tableWidget_dc2_2.item(row, 0)
                        time_item = self.ui.tableWidget_dc2_2.item(row, 1)
                        time_end = self.ui.tableWidget_dc2_2.item(row,2)
                        if voltage_dc2_item and time_item:
                            voltage_dc2 = voltage_dc2_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([voltage_dc2, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.") 
    def export_to_excelac1(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_ac1.rowCount()):
                        voltage_ac_item = self.ui.tableWidget_ac1.item(row, 0)
                        time_item = self.ui.tableWidget_ac1.item(row, 1)
                        time_end = self.ui.tableWidget_ac1.item(row,2)
                        if voltage_ac_item and time_item:
                            voltage_ac = voltage_ac_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([voltage_ac, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.")  
    def export_to_excelac2(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_ac2.rowCount()):
                        voltage_ac2_item = self.ui.tableWidget_ac2.item(row, 0)
                        time_item = self.ui.tableWidget_ac2.item(row, 1)
                        time_end = self.ui.tableWidget_ac2.item(row,2)
                        if voltage_ac2_item and time_item:
                            voltage_ac2 = voltage_ac2_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([voltage_ac2, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.")  
    def fecth_and_popula_data_temp2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="suconhietdo45"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, temperature, nhietdo_lower, nhietdo_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND temperature IS NOT NULL ;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            print(result)
            self.populate_temperature_table2(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as error:
            print("Error fetching data from MySQL:", error)
    def populate_temperature_table2(self, data):
        self.ui.tableWidget_nhietdo_3.clearContents()
        self.ui.tableWidget_nhietdo_3.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, temperature, nhietdo_lower, nhietdo_high ) in enumerate(data):
            if time is None or temperature is None or nhietdo_lower is None or nhietdo_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")

            if nhietdo_lower is not None and nhietdo_high is not None:
                nhietdo_lower = self.nhietdo_lower  
                nhietdo_high = self.nhietdo_high  
            print(nhietdo_lower,nhietdo_high)
            if float(nhietdo_lower) <= float(temperature) <= float(nhietdo_high):
                alert_type = None
            elif float(temperature) < nhietdo_lower:
                alert_type = "Sự cố nhiệt độ thấp"
            elif float(temperature) > nhietdo_high:
                alert_type = "Sự cố nhiệt độ cao"
    
            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_nhietdo_3.rowCount()
                    self.ui.tableWidget_nhietdo_3.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_nhietdo_3.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_nhietdo_3.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_nhietdo_3.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                # Tìm chỉ số của sự cố khác sau sự cố hiện tại
                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_temp, next_lower, next_high = next_row

                    if float(next_lower) <= float(next_temp) <= float(next_high):
                        next_alert_type = None
                    elif float(next_temp) < float(next_lower):
                        next_alert_type = "Sự cố nhiệt độ thấp"
                    elif float(next_temp) > float(next_high):
                        next_alert_type = "Sự cố nhiệt độ cao"

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                # Kiểm tra nếu không có sự cố khác xảy ra sau sự cố hiện tại
                # và dữ liệu thỏa mãn hoặc không thỏa mãn sau sự cố hiện tại
                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_temp, next_lower, next_high = next_row

                    if float(next_lower) <= float(next_temp) <= float(next_high):
                        next_alert_type = None
                    elif float(next_temp) < float(next_lower):
                        next_alert_type = "Sự cố nhiệt độ thấp"
                    elif float(next_temp) > float(next_high):
                        next_alert_type = "Sự cố nhiệt độ cao"
                    # if next_alert_type is not None:
                    #     next_data_time = next_time

        # Adding the last row if there's an ongoing alert
        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_nhietdo_3.rowCount()
            self.ui.tableWidget_nhietdo_3.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_nhietdo_3.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_nhietdo_3.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_nhietdo_3.setItem(row_position, 2, item_next_data_time)
            
            # Check if the last data entry is None and add its time to column 3
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_nhietdo_3.rowCount()
                        self.ui.tableWidget_nhietdo_3.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_nhietdo_3.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_nhietdo_3.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_nhietdo_3.setItem(row_position, 2, item_next_data_time)     
    def fecth_and_popula_data_hum2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodoam45"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, humidity,doam_low,doam_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND humidity IS NOT NULL;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            self.populate_temperature_table_doam2(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as error:
            print("Error fetching data from MySQL:", error)
    def populate_temperature_table_doam2(self, data):
        self.ui.tableWidget_doam_3.clearContents()
        self.ui.tableWidget_doam_3.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, humidity, doam_low, doam_high ) in enumerate(data):
            if time is None or humidity is None or doam_low is None or doam_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")

            if doam_low is not None and doam_high is not None:
                doam_low = self.doam_low  
                doam_high = self.doam_high  
            print(doam_low,doam_high)
            if float(doam_low) <= float(humidity) <= float(doam_high):
                alert_type = None
            elif float(humidity) < doam_low:
                alert_type = "Sự cố độ ẩm thấp"
            elif float(humidity) > doam_high:
                alert_type = "Sự cố độ ẩm cao"
    
            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_doam_3.rowCount()
                    self.ui.tableWidget_doam_3.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_doam_3.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_doam_3.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_doam_3.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                # Tìm chỉ số của sự cố khác sau sự cố hiện tại
                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_temp, next_lower, next_high = next_row

                    if str(next_lower) <= str(next_temp) <= str(next_high):
                        next_alert_type = None
                    elif str(next_temp) < str(next_lower):
                        next_alert_type = "Sự cố độ ẩm thấp"
                    elif str(next_temp) > str(next_high):
                        next_alert_type = "Sự cố độ ẩm cao"

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                # Kiểm tra nếu không có sự cố khác xảy ra sau sự cố hiện tại
                # và dữ liệu thỏa mãn hoặc không thỏa mãn sau sự cố hiện tại
                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_temp, next_lower, next_high = next_row

                    if str(next_lower) <= str(next_temp) <= str(next_high):
                        next_alert_type = None
                    elif str(next_temp) < str(next_lower):
                        next_alert_type = "Sự cố độ ẩm thấp"
                    elif str(next_temp) > str(next_high):
                        next_alert_type = "Sự cố độ ẩm cao"
                    if next_alert_type is not None:
                        next_data_time = next_time

        # Adding the last row if there's an ongoing alert
        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_doam_3.rowCount()
            self.ui.tableWidget_doam_3.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_doam_3.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_doam_3.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_doam_3.setItem(row_position, 2, item_next_data_time)
            
            # Check if the last data entry is None and add its time to column 3
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_doam_3.rowCount()
                        self.ui.tableWidget_doam_3.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_doam_3.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_doam_3.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_doam_3.setItem(row_position, 2, item_next_data_time) 
    def fecth_and_popula_data_ac1_2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucoac145"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, voltage_ac1, dienapac_low, dienapac_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND voltage_ac1 IS NOT NULL;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            
            self.populate_temperature_table_ac1_2(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as error:
            print("Error fetching data from MySQL:", error)
    def populate_temperature_table_ac1_2(self, data):
        self.ui.tableWidget_ac1_2.clearContents()
        self.ui.tableWidget_ac1_2.setRowCount(0)
        next_alert_type = None 
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None
        
        for row_idx, (time, voltage_ac, dienapac_low, dienapac_high) in enumerate(data):
            if time is None or voltage_ac is None or dienapac_low is None or dienapac_high is None:
                continue
            
            
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            
            if float(voltage_ac) == float(dienapac_low):
                alert_type = "Sự cố AC1 mất"
            elif float(voltage_ac) == float(dienapac_high):
                alert_type = None
            
            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_ac1_2.rowCount()
                    self.ui.tableWidget_ac1_2.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_ac1_2.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_ac1_2.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_ac1_2.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if str(next_voltage_ac) == str(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif str(next_voltage_ac) == str(next_voltage_ac_high):
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if str(next_voltage_ac) == str(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif str(next_voltage_ac) == str(next_voltage_ac_high):
                        next_alert_type = None
                    if next_alert_type is not None:
                        next_data_time = next_time

        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_ac1_2.rowCount()
            self.ui.tableWidget_ac1_2.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_ac1_2.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_ac1_2.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_ac1_2.setItem(row_position, 2, item_next_data_time)     
    def fecth_and_popula_data_ac2_2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucoac245"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, voltage_ac2, dienapac_low, dienapac_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND voltage_ac2 IS NOT NULL;"
            
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()

            self.populate_temperature_table_ac2_2(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as error:
            print("Error fetching data from MySQL:", error)
    def populate_temperature_table_ac2_2(self, data):
        self.ui.tableWidget_ac2_2.clearContents()
        self.ui.tableWidget_ac2_2.setRowCount(0)
        next_alert_type = None 
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None
        
        for row_idx, (time, voltage_ac2, dienapac_low, dienapac_high) in enumerate(data):
            if time is None or voltage_ac2 is None or dienapac_low is None or dienapac_high is None:
                continue
            
            
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")

            if float(voltage_ac2) == float(dienapac_low):
                alert_type = "Sự cố AC2 mất"
            elif float(voltage_ac2) == float(dienapac_high):
                alert_type = None
            
            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_ac2_2.rowCount()
                    self.ui.tableWidget_ac2_2.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_ac2_2.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_ac2_2.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_ac2_2.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if str(next_voltage_ac) == str(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif str(next_voltage_ac) == str(next_voltage_ac_high):
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if str(next_voltage_ac) == str(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif str(next_voltage_ac) == str(next_voltage_ac_high):
                        next_alert_type = None
                    if next_alert_type is not None:
                        next_data_time = next_time

        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_ac2_2.rowCount()
            self.ui.tableWidget_ac2_2.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_ac2_2.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_ac2_2.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_ac2_2.setItem(row_position, 2, item_next_data_time)
    def fecth_and_popula_data_dc1_2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodc145"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, voltage_dc1,dienap_low,dienap_low1,dienap_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND voltage_dc1 IS NOT NULL;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            self.populate_temperature_table_dc1_2(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as error:
            print("Error fetching data from MySQL:", error)
    def populate_temperature_table_dc1_2(self, data):
        self.ui.tableWidget_dc1_3.clearContents()
        self.ui.tableWidget_dc1_3.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, voltage_dc1, dienap_low,dienap_low1, dienap_high ) in enumerate(data):
            if time is None or voltage_dc1 is None or dienap_low is None or dienap_low1 is None or dienap_high is None:
                continue
    
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            if dienap_low is None or dienap_low1 is None or dienap_high is None:
                dienap_low = self.dienap_low  
                dienap_low1 = self.dienap_low1
                dienap_high = self.dienap_high 
            print(dienap_low, dienap_low1, dienap_high)
            if float(dienap_low) <= float(voltage_dc1) < float(dienap_low1):
                alert_type = "Sự cố điện áp DC1 thấp mức 1"
            elif float(voltage_dc1) < float(dienap_low):
                alert_type = "Sự cố điện áp DC1 thấp mức 2"
            elif float(voltage_dc1) > float(dienap_high):
                alert_type = "Sự cố điện áp DC1 cao"
            else:
                alert_type = None

            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_dc1_3.rowCount()
                    self.ui.tableWidget_dc1_3.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_dc1_3.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_dc1_3.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_dc1_3.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_voltage_dc1, next_dienap_low1, next_dienap_low2, next_dienap_high = next_row

                    if float(next_dienap_low1) <= float(next_voltage_dc1) < float(next_dienap_low2):
                        next_alert_type = "Sự cố điện áp DC1 mức 1"
                    elif float(next_voltage_dc1) < float(next_dienap_low1):
                        next_alert_type = "Sự cố điện áp DC1 mức 2"
                    elif float(next_voltage_dc1) > float(next_dienap_high):
                        next_alert_type = "Sự cố điện áp DC1 cao"
                    else:
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_dc1, next_dienap_low1, next_dienap_low2, next_dienap_high = next_row

                    if float(next_dienap_low1) <= float(next_voltage_dc1) < float(next_dienap_low2):
                        next_alert_type = "Sự cố điện áp DC1 mức 1"
                    elif float(next_voltage_dc1) < float(next_dienap_low1):
                        next_alert_type = "Sự cố điện áp DC1 mức 2"
                    elif float(next_voltage_dc1) > float(next_dienap_high):
                        next_alert_type = "Sự cố điện áp DC1 cao"
                    else:
                        next_alert_type = None
                    if next_alert_type is not None:
                        next_data_time = next_time

        # Adding the last row if there's an ongoing alert
        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_dc1_3.rowCount()
            self.ui.tableWidget_dc1_3.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_dc1_3.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_dc1_3.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_dc1_3.setItem(row_position, 2, item_next_data_time)
            
            # Check if the last data entry is None and add its time to column 3
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_dc1_3.rowCount()
                        self.ui.tableWidget_dc1_3.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_dc1_3.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_dc1_3.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_dc1_3.setItem(row_position, 2, item_next_data_time) 
    def fecth_and_popula_data_dc2_2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodc245"
        )
            mycursor = mydb.cursor()
            from_date = self.problem.dateEdit.date().toString("yyyy-MM-dd")
            to_date = self.problem.dateEdit_2.date().toString("yyyy-MM-dd")
            from_date_with_time = from_date + " 00:00:00"
            to_date_with_time = to_date + " 23:59:59"
            query = "SELECT time, voltage_dc2, dienap_low,dienap_low1, dienap_high FROM new_table WHERE DATE(time) BETWEEN %s AND %s AND voltage_dc2 IS NOT NULL;"
            mycursor.execute(query,(from_date_with_time, to_date_with_time))
            result = mycursor.fetchall()
            self.populate_temperature_table_dc2_2(result)
            mycursor.close()
            mydb.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")      
    def populate_temperature_table_dc2_2(self, data):
        self.ui.tableWidget_dc2_3.clearContents()
        self.ui.tableWidget_dc2_3.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, voltage_dc2, dienap_low,dienap_low1, dienap_high ) in enumerate(data):
            if time is None or voltage_dc2 is None or dienap_low is None or dienap_low1 is None or dienap_high is None:
                continue
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            
            dienap_low = self.dienap_low  
            dienap_low1 = self.dienap_low1
            dienap_high = self.dienap_high 
            if float(dienap_low) <= float(voltage_dc2) < float(dienap_low1):
                alert_type = "Sự cố điện áp DC1 mức 1"
            elif float(voltage_dc2) < float(dienap_low1):
                alert_type = "Sự cố điện áp DC1 mức 2"
            elif float(voltage_dc2) > float(dienap_high):
                alert_type = "Sự cố điện áp DC1 cao"
            else:
                alert_type = None

            if alert_type != previous_alert_type:
                if previous_alert_type is not None:
                    row_position = self.ui.tableWidget_dc2_3.rowCount()
                    self.ui.tableWidget_dc2_3.insertRow(row_position)

                    item_alert_type = QTableWidgetItem(previous_alert_type)
                    item_alert_time = QTableWidgetItem(previous_alert_time)

                    if next_data_time:
                        item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        item_next_data_time = QTableWidgetItem()

                    item_alert_type.setForeground(QColor(0, 0, 0))  
                    item_alert_time.setForeground(QColor(0, 0, 0))
                    item_next_data_time.setForeground(QColor(0, 0, 0))
                    self.ui.tableWidget_dc2_3.setItem(row_position, 0, item_alert_type)
                    self.ui.tableWidget_dc2_3.setItem(row_position, 1, item_alert_time)
                    self.ui.tableWidget_dc2_3.setItem(row_position, 2, item_next_data_time)

                previous_alert_type = alert_type
                previous_alert_time = time_str
                next_alert_row_idx = None
                next_data_time = None

                for next_idx, next_row in enumerate(data[row_idx + 1:], start=row_idx + 1):
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) < float(next_dienap_low1):
                        next_alert_type = "Sự cố điện áp DC1 mức 1"
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = "Sự cố điện áp DC1 mức 2"
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = "Sự cố điện áp DC1 cao"
                    else:
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) < float(next_dienap_low1):
                        next_alert_type = "Sự cố điện áp DC1 mức 1"
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = "Sự cố điện áp DC1 mức 2"
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = "Sự cố điện áp DC1 cao"
                    else:
                        next_alert_type = None
                    if next_alert_type is not None:
                        next_data_time = next_time

        # Adding the last row if there's an ongoing alert
        if previous_alert_type is not None:
            row_position = self.ui.tableWidget_dc2_3.rowCount()
            self.ui.tableWidget_dc2_3.insertRow(row_position)

            item_alert_type = QTableWidgetItem(previous_alert_type)
            item_alert_time = QTableWidgetItem(previous_alert_time)

            if next_data_time:
                item_next_data_time = QTableWidgetItem(next_data_time.strftime("%Y-%m-%d %H:%M:%S"))
                item_next_data_time.setForeground(QColor(255, 0, 0))
            else:
                item_next_data_time = QTableWidgetItem()

            item_alert_type.setForeground(QColor(0, 0, 0))  
            item_alert_time.setForeground(QColor(0, 0, 0))
            item_next_data_time.setForeground(QColor(0, 0, 0))
            self.ui.tableWidget_dc2_3.setItem(row_position, 0, item_alert_type)
            self.ui.tableWidget_dc2_3.setItem(row_position, 1, item_alert_time)
            self.ui.tableWidget_dc2_3.setItem(row_position, 2, item_next_data_time)
            
            # Check if the last data entry is None and add its time to column 3
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_dc2_3.rowCount()
                        self.ui.tableWidget_dc2_3.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_dc2_3.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_dc2_3.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_dc2_3.setItem(row_position, 2, item_next_data_time) 
    def export_to_exceltemp_2(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_nhietdo_3.rowCount()):
                        temperature_item = self.ui.tableWidget_nhietdo_3.item(row, 0)
                        time_item = self.ui.tableWidget_nhietdo_3.item(row, 1)
                        time_end = self.ui.tableWidget_nhietdo_3.item(row,2)
                        if temperature_item and time_item:
                            temperature = temperature_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([temperature, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.") 
    def export_to_excelhum_2(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_doam_3.rowCount()):
                        humidity_item = self.ui.tableWidget_doam_3.item(row, 0)
                        time_item = self.ui.tableWidget_doam_3.item(row, 1)
                        time_end = self.ui.tableWidget_doam_3.item(row,2)
                        if humidity_item and time_item:
                            humidity = humidity_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([humidity, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.") 
    def export_to_exceldc1_2(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_dc1_3.rowCount()):
                        temperature_item = self.ui.tableWidget_dc1_3.item(row, 0)
                        time_item = self.ui.tableWidget_dc1_3.item(row, 1)
                        time_end = self.ui.tableWidget_dc1_3.item(row,2)
                        if temperature_item and time_item:
                            temperature = temperature_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([temperature, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.")
    def export_to_exceldc2_2(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_dc2_3.rowCount()):
                        voltage_dc2_item = self.ui.tableWidget_dc2_3.item(row, 0)
                        time_item = self.ui.tableWidget_dc2_3.item(row, 1)
                        time_end = self.ui.tableWidget_dc2_3.item(row,2)
                        if voltage_dc2_item and time_item:
                            voltage_dc2 = voltage_dc2_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([voltage_dc2, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.") 
    def export_to_excelac1_2(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_ac1_2.rowCount()):
                        voltage_ac_item = self.ui.tableWidget_ac1_2.item(row, 0)
                        time_item = self.ui.tableWidget_ac1_2.item(row, 1)
                        time_end = self.ui.tableWidget_ac1_2.item(row,2)
                        if voltage_ac_item and time_item:
                            voltage_ac = voltage_ac_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([voltage_ac, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.")  
    def export_to_excelac2_2(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
            # Get data from the table widget
            data = []
            for row in range(self.ui.tableWidget_ac2_2.rowCount()):
                        voltage_ac2_item = self.ui.tableWidget_ac2_2.item(row, 0)
                        time_item = self.ui.tableWidget_ac2_2.item(row, 1)
                        time_end = self.ui.tableWidget_ac2_2.item(row,2)
                        if voltage_ac2_item and time_item:
                            voltage_ac2 = voltage_ac2_item.text()
                            time = time_item.text()
                            time2 = time_end.text()
                            data.append([voltage_ac2, time,time2])
            
                    # Convert data to a Pandas DataFrame
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])

                    # Save the DataFrame to Excel
            df.to_excel(file_path, index=False)
