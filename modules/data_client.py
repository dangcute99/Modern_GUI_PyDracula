import sys
import os
import datetime
from datetime import timedelta
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
from Client import *
tram70 ="172.20.10.48"
tram45 ="172.20.10.01"
tram01 ="172.20.10.02"
tram48="172.20.10.4"
tram71="172.20.10.71"
tram76="172.20.10.76"

class SensorDataReceiverClient(QObject):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    alertSignal = Signal(str, str,bool)
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.server_ip = socket.gethostname()
        self.server_port = 8234
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.last_entry_times = {}
        # Lock for thread safety
        self.lock = threading.Lock()
        # Timer for checking missing entries
        self.check_timer = QTimer(self)
        self.check_timer.timeout.connect(self.check_missing_entries)
        self.check_timer.start(1000)  
    def connect_to_server(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            threading.Thread(target=self.receive_data, args=(self.client_socket,)).start()
            print(f"Connected to server {self.server_ip}:{self.server_port}")
        except ConnectionRefusedError:
            print(f"Failed to connect to server {self.server_ip}:{self.server_port}")
    
    def receive_data(self, client_socket):
        try:
            
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                self.last_data_time = datetime.datetime.now()
                parts = data.split(',')
                if len(parts) % 3 != 0:
                    print("Invalid data format")
                    continue

                with self.lock:
                    for i in range(0, len(parts), 3):
                        client_address = parts[i]
                        param_name = parts[i + 1]
                        param_value = parts[i + 2]
                        current_time = datetime.datetime.now()
                        self.process_data(client_address, param_name, param_value, current_time,client_socket,parts)
            # print(current_time)
            

        except socket.error as e:
            print(f"Socket error during data reception: {e}")
        finally:
            with self.lock:
                self.clients.remove(client_socket)
            client_socket.close()
    def process_data(self, client_address, param_name, param_value, current_time,client_socket,parts):
                    try:
                        param_value = float(param_value)
                    except ValueError:
                        print(f"Invalid value for {param_name}: {param_value}")
                        return
                    self.last_entry_times[(client_address, param_name)] = current_time
                    temperature = None
                    humidity = None
                    light = None
                    voltage_dc1 = None
                    voltage_dc2 = None
                    voltage_ac = None
                    voltage_ac2 = None
                    nhietdo_lower = None
                    nhietdo_high = None
                    doam_low = None
                    doam_high = None
                    dienap_low = None
                    dienap_low1 = None
                    dienap_high = None
                    dienapac_low = None
                    dienapac_high = None
                    current_time = None
                    if param_name == "temperature":
                        try:
                            temperature = float(param_value)
                        except ValueError:
                            print(f"Invalid value for temperature: {param_value}")
                    elif param_name == "humidity":
                        try:
                            humidity = float(param_value)
                        except ValueError:
                            print(f"Invalid value for humidity: {param_value}")
                    elif param_name == "light":
                        try:
                            light = float(param_value)
                        except ValueError:
                            print(f"Invalid value for light: {param_value}")
                    elif param_name == "voltage_dc1":
                        try:
                            voltage_dc1 = float(param_value)
                        except ValueError:
                            print(f"Invalid value for voltage_dc1: {param_value}")
                    elif param_name == "voltage_dc2":
                        try:
                            voltage_dc2 = float(param_value)
                        except ValueError:
                            print(f"Invalid value for voltage_dc2: {param_value}")
                    elif param_name == "voltage_ac":
                        try:
                            voltage_ac = float(param_value)
                        except ValueError:
                            print(f"Invalid value for voltage_ac: {param_value}")
                    elif param_name == "voltage_ac2":
                        try:
                            voltage_ac2 = float(param_value)
                        except ValueError:
                            print(f"Invalid value for voltage_ac2: {param_value}")
                    elif param_name == "nhietdo_lower":
                        try:
                                nhietdo_lower = float(param_value)
                        except ValueError:
                                print(f"Invalid value for voltage_ac2: {param_value}")
                    elif param_name == "nhietdo_high":
                       
                                nhietdo_high = float(param_value)
                     
                    elif param_name == "doam_low":
                       
                                doam_low = float(param_value)
                  
                    elif param_name == "doam_high":
                        
                                doam_high = float(param_value)
                        
                    elif param_name == "dienap_low":
                      
                                dienap_low = float(param_value)
                      
                    elif param_name == "dienap_low1":
                        try:
                                dienap_low1 = float(param_value)
                        except ValueError:
                                print(f"Invalid value for voltage_ac2: {param_value}")
                    elif param_name == "dienap_high":
                        try:
                                dienap_high = float(param_value)
                        except ValueError:
                                print(f"Invalid value for voltage_ac2: {param_value}")
                    elif param_name == "dienapac_low":
                        try:
                                dienapac_low = float(param_value)
                        except ValueError:
                                print(f"Invalid value for voltage_ac2: {param_value}")
                    elif param_name == "dienapac_high":
                        try:
                                dienapac_high = float(param_value)
                        except ValueError:
                                print(f"Invalid value for voltage_ac2: {param_value}")
                    current_time = datetime.datetime.now()

                    # self.process_received_data(client_address, temperature, humidity, light,fire, voltage_dc1, voltage_dc2,voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,dienap_low,dienap_low1, dienap_high, current_time)
                    self.dataReceived.emit(client_address, temperature, humidity, light, voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high, current_time)
                    self.send_data_temperature(client_address, temperature,nhietdo_lower, nhietdo_high,current_time)
                    self.send_data_humidity(client_address, humidity, doam_low, doam_high,current_time)
                    self.send_data_dc1(client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_dc2(client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_ac1(client_address, voltage_ac, dienapac_low, dienapac_high,current_time)
                    self.send_data_ac2(client_address, voltage_ac2, dienapac_low, dienapac_high,current_time)
                    self.send_data_temperature_2(client_address, temperature,nhietdo_lower, nhietdo_high,current_time)
                    self.send_data_humidity_2(client_address, humidity, doam_low, doam_high,current_time)
                    self.send_data_dc1_2(client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_dc2_2(client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_ac1_2(client_address, voltage_ac, dienapac_low, dienapac_high,current_time)
                    self.send_data_ac2_2(client_address, voltage_ac2, dienapac_low, dienapac_high,current_time)

                    self.send_data_temperature_tram01(client_address, temperature,nhietdo_lower, nhietdo_high,current_time)
                    self.send_data_humidity_tram01(client_address, humidity, doam_low, doam_high,current_time)
                    self.send_data_dc1_tram01(client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_dc2_tram01(client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_ac1_tram01(client_address, voltage_ac, dienapac_low, dienapac_high,current_time)
                    self.send_data_ac2_tram01(client_address, voltage_ac2, dienapac_low, dienapac_high,current_time)

                    self.send_data_temperature_tram48(client_address, temperature,nhietdo_lower, nhietdo_high,current_time)
                    self.send_data_humidity_tram48(client_address, humidity, doam_low, doam_high,current_time)
                    self.send_data_dc1_tram48(client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_dc2_tram48(client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_ac1_tram48(client_address, voltage_ac, dienapac_low, dienapac_high,current_time)
                    self.send_data_ac2_tram48(client_address, voltage_ac2, dienapac_low, dienapac_high,current_time)

                    self.send_data_temperature_tram71(client_address, temperature,nhietdo_lower, nhietdo_high,current_time)
                    self.send_data_humidity_tram71(client_address, humidity, doam_low, doam_high,current_time)
                    self.send_data_dc1_tram71(client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_dc2_tram71(client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_ac1_tram71(client_address, voltage_ac, dienapac_low, dienapac_high,current_time)
                    self.send_data_ac2_tram71(client_address, voltage_ac2, dienapac_low, dienapac_high,current_time)

                    self.send_data_temperature_tram76(client_address, temperature,nhietdo_lower, nhietdo_high,current_time)
                    self.send_data_humidity_tram76(client_address, humidity, doam_low, doam_high,current_time)
                    self.send_data_dc1_tram76(client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_dc2_tram76(client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time)
                    self.send_data_ac1_tram76(client_address, voltage_ac, dienapac_low, dienapac_high,current_time)
                    self.send_data_ac2_tram76(client_address, voltage_ac2, dienapac_low, dienapac_high,current_time)

    def check_missing_entries(self):
        # Check for missing entries and raise alert if necessary
        current_time = datetime.datetime.now()
        for (client_address, param_name), last_entry_time in self.last_entry_times.items():
            if last_entry_time is not None:
                time_since_entry = (current_time - last_entry_time).total_seconds()
                # print(time_since_entry)
                if time_since_entry > 900:
                    alert_flag = True
                    # print(f"Alert: No data received for {param_name} from {client_address} in the last 10 seconds!")
                    self.alertSignal.emit(client_address, param_name, alert_flag)
                else:  
                    alert_flag =False
                    self.alertSignal.emit(client_address, param_name,alert_flag)
    def send_data_temperature(self, client_address, temperature, nhietdo_lower, nhietdo_high, current_time):
        if client_address == tram70:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="suconhietdo_tram70"
                )
                nhietdo_lower_default = 20 
                nhietdo_high_default = 25
                mycursor = mydb.cursor()
                if temperature is not None:
                    query = "INSERT INTO new_table (client_address, temperature, nhietdo_lower, nhietdo_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, temperature, nhietdo_lower_default, nhietdo_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully nhietdo.")
                mydb.commit()
               
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_humidity(self,client_address, humidity, doam_low, doam_high,current_time):
        if client_address == tram70:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodoam_tram70"
                )
                doam_lower_default = 40  
                doam_high_default = 70
                mycursor = mydb.cursor()
                if humidity is not None:
                    query = "INSERT INTO new_table (client_address, humidity, doam_low, doam_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, humidity, doam_lower_default, doam_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. doam")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc1(self,client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram70:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc1_tram70"
                )
                dc1_lower_default = 47
                dc1_lower_default2 =48  # Giá trị ngưỡng nhiệt độ thấp mặc định
                dc1_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc1 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc1, dc1_lower_default, dc1_lower_default2,dc1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc1")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc2(self,client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram70:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc2_tram70"
                )
                dc2_lower_default = 47
                dc2_lower_default2 =48  
                dc2_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc2, dc2_lower_default, dc2_lower_default2,dc2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc2")
                mydb.commit()
              
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac1(self,client_address, voltage_ac, dienapac_low,dienapac_high,current_time):
        if client_address == tram70:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac1_tram70"
                )
                ac1_lower_default = 1
                ac1_high_default = 220
                
                
                mycursor = mydb.cursor()
                if voltage_ac is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac1, dienapac_low, dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac, ac1_lower_default, ac1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. ac")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac2(self,client_address, voltage_ac2, dienapac_low,dienapac_high,current_time):
        if client_address == tram70:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac2_tram70"
                )
                ac2_lower_default = 1
                ac2_high_default =220
                mycursor = mydb.cursor()
                if voltage_ac2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac2, dienapac_low,dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac2, ac2_lower_default, ac2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully.")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    
    def send_data_temperature_2(self, client_address, temperature, nhietdo_lower, nhietdo_high, current_time):
        if client_address == tram45:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="suconhietdo_tram45"
                )
                nhietdo_lower_default = 20  # Giá trị ngưỡng nhiệt độ thấp mặc định
                nhietdo_high_default = 25
                mycursor = mydb.cursor()
                if temperature is not None:
                    query = "INSERT INTO new_table (client_address, temperature, nhietdo_lower, nhietdo_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, temperature, nhietdo_lower_default, nhietdo_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully nhietdo.")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_humidity_2(self,client_address, humidity, doam_low, doam_high,current_time):
        if client_address == tram45:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodoam_tram45"
                )
                doam_lower_default = 40  
                doam_high_default = 70
                mycursor = mydb.cursor()
                if humidity is not None:
                    query = "INSERT INTO new_table (client_address, humidity, doam_low, doam_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, humidity, doam_lower_default, doam_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. doam")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc1_2(self,client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram45:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc1_tram45"
                )
                dc1_lower_default = 47
                dc1_lower_default2 =48  
                dc1_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc1 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc1, dc1_lower_default, dc1_lower_default2,dc1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc1")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc2_2(self,client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram45:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc2_tram45"
                )
                dc2_lower_default = 47
                dc2_lower_default2 =48  
                dc2_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc2, dc2_lower_default, dc2_lower_default2,dc2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc2")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac1_2(self,client_address, voltage_ac, dienapac_low,dienapac_high,current_time):
        if client_address == tram45:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac1_tram45"
                )
                ac1_lower_default = 1
                ac1_high_default = 220
                
                
                mycursor = mydb.cursor()
                if voltage_ac is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac1, dienapac_low, dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac, ac1_lower_default, ac1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. ac1")
                mydb.commit()
               
            except mysql.connector.Error as error: 
                print("Error inserting data into MySQL:", error)
    def send_data_ac2_2(self,client_address, voltage_ac2, dienapac_low,dienapac_high,current_time):
        if client_address == tram45:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac2_tram45"
                )
                ac2_lower_default = 1
                ac2_high_default =220
                mycursor = mydb.cursor()
                if voltage_ac2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac2, dienapac_low,dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac2, ac2_lower_default, ac2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. ac2")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)

    def send_data_temperature_tram01(self, client_address, temperature, nhietdo_lower, nhietdo_high, current_time):
        if client_address == tram01:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="suconhietdo_tram01"
                )
                nhietdo_lower_default = 20  # Giá trị ngưỡng nhiệt độ thấp mặc định
                nhietdo_high_default = 25
                mycursor = mydb.cursor()
                if temperature is not None:
                    query = "INSERT INTO new_table (client_address, temperature, nhietdo_lower, nhietdo_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, temperature, nhietdo_lower_default, nhietdo_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully nhietdo.")
                mydb.commit()
               
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_humidity_tram01(self,client_address, humidity, doam_low, doam_high,current_time):
        if client_address == tram01:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodoam_tram01"
                )
                doam_lower_default = 40  
                doam_high_default = 70
                mycursor = mydb.cursor()
                if humidity is not None:
                    query = "INSERT INTO new_table (client_address, humidity, doam_low, doam_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, humidity, doam_lower_default, doam_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. doam")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc1_tram01(self,client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram01:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc1_tram01"
                )
                dc1_lower_default = 47
                dc1_lower_default2 =48  # Giá trị ngưỡng nhiệt độ thấp mặc định
                dc1_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc1 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc1, dc1_lower_default, dc1_lower_default2,dc1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc1")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc2_tram01(self,client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram01:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc2_tram01"
                )
                dc2_lower_default = 47
                dc2_lower_default2 =48  
                dc2_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc2, dc2_lower_default, dc2_lower_default2,dc2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc2")
                mydb.commit()
              
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac1_tram01(self,client_address, voltage_ac, dienapac_low,dienapac_high,current_time):
        if client_address == tram01:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac1_tram01"
                )
                ac1_lower_default = 1
                ac1_high_default = 220
                
                
                mycursor = mydb.cursor()
                if voltage_ac is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac1, dienapac_low, dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac, ac1_lower_default, ac1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. ac")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac2_tram01(self,client_address, voltage_ac2, dienapac_low,dienapac_high,current_time):
        if client_address == tram01:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac2_tram01"
                )
                ac2_lower_default = 1
                ac2_high_default =220
                mycursor = mydb.cursor()
                if voltage_ac2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac2, dienapac_low,dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac2, ac2_lower_default, ac2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully.")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)

    def send_data_temperature_tram48(self, client_address, temperature, nhietdo_lower, nhietdo_high, current_time):
        if client_address == tram48:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="suconhietdo_tram48"
                )
                nhietdo_lower_default = 20  # Giá trị ngưỡng nhiệt độ thấp mặc định
                nhietdo_high_default = 25
                mycursor = mydb.cursor()
                if temperature is not None:
                    query = "INSERT INTO new_table (client_address, temperature, nhietdo_lower, nhietdo_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, temperature, nhietdo_lower_default, nhietdo_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully nhietdo.")
                mydb.commit()
               
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_humidity_tram48(self,client_address, humidity, doam_low, doam_high,current_time):
        if client_address == tram48:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodoam_tram48"
                )
                doam_lower_default = 40  
                doam_high_default = 70
                mycursor = mydb.cursor()
                if humidity is not None:
                    query = "INSERT INTO new_table (client_address, humidity, doam_low, doam_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, humidity, doam_lower_default, doam_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. doam")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc1_tram48(self,client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram48:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc1_tram48"
                )
                dc1_lower_default = 47
                dc1_lower_default2 =48  # Giá trị ngưỡng nhiệt độ thấp mặc định
                dc1_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc1 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc1, dc1_lower_default, dc1_lower_default2,dc1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc1")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc2_tram48(self,client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram48:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc2_tram48"
                )
                dc2_lower_default = 47
                dc2_lower_default2 =48  
                dc2_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc2, dc2_lower_default, dc2_lower_default2,dc2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc2")
                mydb.commit()
              
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac1_tram48(self,client_address, voltage_ac, dienapac_low,dienapac_high,current_time):
        if client_address == tram48:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac1_tram48"
                )
                ac1_lower_default = 1
                ac1_high_default = 220
                
                
                mycursor = mydb.cursor()
                if voltage_ac is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac1, dienapac_low, dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac, ac1_lower_default, ac1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. ac")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac2_tram48(self,client_address, voltage_ac2, dienapac_low,dienapac_high,current_time):
        if client_address == tram48:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac2_tram48"
                )
                ac2_lower_default = 1
                ac2_high_default =220
                mycursor = mydb.cursor()
                if voltage_ac2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac2, dienapac_low,dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac2, ac2_lower_default, ac2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully.")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    
    def send_data_temperature_tram71(self, client_address, temperature, nhietdo_lower, nhietdo_high, current_time):
        if client_address == tram71:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="suconhietdo_tram71"
                )
                nhietdo_lower_default = 20  # Giá trị ngưỡng nhiệt độ thấp mặc định
                nhietdo_high_default = 25
                mycursor = mydb.cursor()
                if temperature is not None:
                    query = "INSERT INTO new_table (client_address, temperature, nhietdo_lower, nhietdo_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, temperature, nhietdo_lower_default, nhietdo_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully nhietdo.")
                mydb.commit()
               
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_humidity_tram71(self,client_address, humidity, doam_low, doam_high,current_time):
        if client_address == tram71:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodoam_tram71"
                )
                doam_lower_default = 40  
                doam_high_default = 70
                mycursor = mydb.cursor()
                if humidity is not None:
                    query = "INSERT INTO new_table (client_address, humidity, doam_low, doam_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, humidity, doam_lower_default, doam_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. doam")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc1_tram71(self,client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram71:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc1_tram71"
                )
                dc1_lower_default = 47
                dc1_lower_default2 =48  # Giá trị ngưỡng nhiệt độ thấp mặc định
                dc1_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc1 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc1, dc1_lower_default, dc1_lower_default2,dc1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc1")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc2_tram71(self,client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram71:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc2_tram71"
                )
                dc2_lower_default = 47
                dc2_lower_default2 =48 
                dc2_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc2, dc2_lower_default, dc2_lower_default2,dc2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc2")
                mydb.commit()
              
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac1_tram71(self,client_address, voltage_ac, dienapac_low,dienapac_high,current_time):
        if client_address == tram71:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac1_tram71"
                )
                ac1_lower_default = 1
                ac1_high_default = 220
                
                
                mycursor = mydb.cursor()
                if voltage_ac is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac1, dienapac_low, dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac, ac1_lower_default, ac1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. ac")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac2_tram71(self,client_address, voltage_ac2, dienapac_low,dienapac_high,current_time):
        if client_address == tram71:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac2_tram71"
                )
                ac2_lower_default = 1
                ac2_high_default =220
                mycursor = mydb.cursor()
                if voltage_ac2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac2, dienapac_low,dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac2, ac2_lower_default, ac2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully.")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)

    def send_data_temperature_tram76(self, client_address, temperature, nhietdo_lower, nhietdo_high, current_time):
        if client_address == tram76:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="suconhietdo_tram76"
                )
                nhietdo_lower_default = 20  # Giá trị ngưỡng nhiệt độ thấp mặc định
                nhietdo_high_default = 25
                mycursor = mydb.cursor()
                if temperature is not None:
                    query = "INSERT INTO new_table (client_address, temperature, nhietdo_lower, nhietdo_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, temperature, nhietdo_lower_default, nhietdo_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully nhietdo.")
                mydb.commit()
               
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_humidity_tram76(self,client_address, humidity, doam_low, doam_high,current_time):
        if client_address == tram76:    
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodoam_tram76"
                )
                doam_lower_default = 40  
                doam_high_default = 70
                mycursor = mydb.cursor()
                if humidity is not None:
                    query = "INSERT INTO new_table (client_address, humidity, doam_low, doam_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, humidity, doam_lower_default, doam_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. doam")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc1_tram76(self,client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram76:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc1_tram76"
                )
                dc1_lower_default = 47
                dc1_lower_default2 =48  # Giá trị ngưỡng nhiệt độ thấp mặc định
                dc1_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc1 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc1, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc1, dc1_lower_default, dc1_lower_default2,dc1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc1")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_dc2_tram76(self,client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high,current_time):
        if client_address == tram76:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucodc2_tram76"
                )
                dc2_lower_default = 47
                dc2_lower_default2 =48 
                dc2_high_default = 58.5
                
                mycursor = mydb.cursor()
                if voltage_dc2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_dc2, dienap_low, dienap_low1,dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc2, dc2_lower_default, dc2_lower_default2,dc2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc2")
                mydb.commit()
              
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac1_tram76(self,client_address, voltage_ac, dienapac_low,dienapac_high,current_time):
        if client_address == tram76:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac1_tram76"
                )
                ac1_lower_default = 1
                ac1_high_default = 220
                
                
                mycursor = mydb.cursor()
                if voltage_ac is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac1, dienapac_low, dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac, ac1_lower_default, ac1_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. ac")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    def send_data_ac2_tram76(self,client_address, voltage_ac2, dienapac_low,dienapac_high,current_time):
        if client_address == tram76:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="123456789",
                    database="sucoac2_tram76"
                )
                ac2_lower_default = 1
                ac2_high_default =220
                mycursor = mydb.cursor()
                if voltage_ac2 is not None:
                    query = "INSERT INTO new_table (client_address, voltage_ac2, dienapac_low,dienapac_high, time) VALUES (%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_ac2, ac2_lower_default, ac2_high_default,current_time)
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully.")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
    