import sys
import os
import datetime
from datetime import timedelta
import time
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
tram01 ="172.20.10.02"
tram48="172.20.10.4"
tram71="172.20.10.71"
tram76="172.20.10.76"

class SensorDataReceiver(QObject):
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    alertSignal = Signal(str, str,bool,int)
    global host,user,password
    def __init__(self, host, port):
        super().__init__()
        self.nhietdo_lower_default = float(20)
        self.nhietdo_high_default = float(25)
        self.nhietdo_lower = self.nhietdo_lower_default
        self.nhietdo_high = self.nhietdo_high_default
        self.mutex = threading.Lock()
        self.doam_low_default = float(40)  
        self.doam_high_default = float(70)
        self.doam_low = self.doam_low_default
        self.doam_high = self.doam_high_default
        self.mutex_doam = threading.Lock()
        self.dienap_low_default =float(47)
        self.dienap_low1_default =float(48)
        self.dienap_high_default =float(58.5)
        self.dienap_low = self.dienap_low_default
        self.dienap_low1 = self.dienap_low1_default
        self.dienap_high = self.dienap_high_default
        self.mutex_dienap = threading.Lock()

       
        self.host = host
        self.port = port
        self.clients = []
        self.lock = threading.Lock()
        self.last_entry_times = {}

        # Timer for checking missing entries
        self.check_timer = QTimer(self)
        self.check_timer.timeout.connect(self.check_missing_entries)
        self.check_timer.start(1000)  # Set the timer interval to 5 minutes (300,000 milliseconds)

    def start_listening(self):
        threading.Thread(target=self.accept_connections).start()

    def accept_connections(self):
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.bind((self.host, self.port))
            socket_server.listen(6)
            print(f"Server listening on {self.host}:{self.port}")

            while True:
                connection, client_address = socket_server.accept()
                client_socket = connection
                print(f"Accepted connection from client: {client_address[0]}:{client_address[1]}")
                self.clients.append(client_socket)
                # threading.Thread(target=self.handle_client, args=(client_socket,)).start()
                threading.Thread(target=self.receive_data, args=(client_socket,)).start()
                
        except socket.error as e:
            print(f"Socket error during connection acceptance: {e}")

    def authenticate_user(self, username, password):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="login"
            )
            mycursor = mydb.cursor()
            query = "SELECT * FROM new_table WHERE username = %s AND password = %s"
            mycursor.execute(query, (username, password))
            result = mycursor.fetchone()
            mycursor.close()
            mydb.close()
            return result is not None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def receive_data(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024).decode()
            
                if not data:
                    break
                self.last_data_time = datetime.datetime.now()
                parts = data.split(',')
                if len(parts) % 3 != 0:
                    if len(parts) == 2:
                        # Xử lý dữ liệu chỉ có 2 phần tử ở đây
                        username = parts[0]
                        password = parts[1]
                        current_time = datetime.datetime.now()

                        # Thực hiện xử lý dữ liệu ở đây
                        self.handle_data(username, password, client_socket)
                    else:
                        print("Invalid data format")
                    continue
                
                with self.lock:
                    for i in range(0, len(parts), 3):
                        client_address = parts[i]
                        param_name = parts[i + 1]
                        param_value = parts[i + 2]
                        current_time = datetime.datetime.now()
                        self.process_data(client_address, param_name, param_value, current_time,client_socket,parts)
                    
        except socket.error as e:
            print(f"Socket error during data reception: {e}")
        finally:
            with self.lock:
                self.clients.remove(client_socket)
            client_socket.close()
  
    def handle_data(self, username, password, client_socket):
        try:
            # Kiểm tra xác thực
            if self.authenticate_user(username, password):
                client_socket.send("1".encode())
            else:
                client_socket.send("0".encode())
        except Exception as e:
            print(f"Error handling data: {e}")
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
                            if temperature ==0:
                                temperature += 0.1
                        except ValueError:
                            print(f"Invalid value for temperature: {param_value}")
                    elif param_name == "humidity":
                        try:
                            humidity = float(param_value)
                            if humidity ==0:
                                humidity += 0.1
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
                            if voltage_dc1 == 0 :
                                voltage_dc1 += 0.1
                        except ValueError:
                            print(f"Invalid value for voltage_dc1: {param_value}")
                    elif param_name == "voltage_dc2":
                        try:
                            voltage_dc2 = float(param_value)
                            if voltage_dc2 == 0 :
                                voltage_dc2 += 0.1
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
                        try:
                                nhietdo_high = float(param_value)
                        except ValueError:
                                print(f"Invalid value for voltage_ac2: {param_value}")
                    elif param_name == "doam_low":
                        try:
                                doam_low = float(param_value)
                        except ValueError:
                                print(f"Invalid value for voltage_ac2: {param_value}")
                  
                    elif param_name == "doam_high":
                        try:
                            doam_high = float(param_value)
                        except ValueError:
                            print("Error: doam_high is not a valid number")   
                    elif param_name == "dienap_low":
                        try:
                                dienap_low = float(param_value)
                        except ValueError:
                                print(f"Invalid value for voltage_ac2: {param_value}")
                        
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

                
                # Send data to other connected clients
                    self.send_data_to_clients(parts, client_socket)
                    
    def check_missing_entries(self):
        # Check for missing entries and raise alert if necessary
        current_time = datetime.datetime.now()
        
        for (client_address, param_name), last_entry_time in self.last_entry_times.items():
            time_since_entry = (current_time - last_entry_time).total_seconds()
            
            if time_since_entry > 5:
                # Nếu quá thời gian, đặt alert_flag là True để báo lỗi
                alert_flag = True
                # Đồng thời đặt bit còi là 1
                bit_canh_bao_tram = 1
            else:
                # Nếu không, alert_flag là False và bit còi là 0
                alert_flag = False
                bit_canh_bao_tram = 0
            
            # Gửi tín hiệu báo lỗi và bit còi
            self.alertSignal.emit(client_address, param_name, alert_flag, bit_canh_bao_tram)
    def send_data_to_clients(self, data, source_client_socket):
        data_str = ','.join(data)
        print(f"Sending data to clients: {data_str}")
        
        for client in self.clients:
            if client != source_client_socket:
                if isinstance(client, socket.socket):
                        client.sendall(data_str.encode())
                else:
                    print("Invalid socket found in the clients list. Skipping it.")

    def send_data_temperature(self, client_address, temperature, nhietdo_lower, nhietdo_high, current_time):
            if client_address == tram70:    
                try:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="123456789",
                        database="suconhietdo_tram70"
                    )
                    
                    mycursor = mydb.cursor()
                    
                    # Kiểm tra xem có giá trị ngưỡng mới không
                    if nhietdo_lower is not None or nhietdo_high is not None:
                        new_nhietdo_lower = self.nhietdo_lower if nhietdo_lower is None else nhietdo_lower
                        new_nhietdo_high = self.nhietdo_high if nhietdo_high is None else nhietdo_high

                        # Xây dựng câu lệnh SQL cập nhật giá trị ngưỡng
                        query = "UPDATE new_table SET nhietdo_lower = %s, nhietdo_high = %s WHERE client_address = %s ORDER BY time DESC LIMIT 1"
                        # Thực hiện câu lệnh SQL cập nhật giá trị ngưỡng
                        self.mutex.acquire()
                        mycursor.execute(query, (new_nhietdo_lower, new_nhietdo_high, client_address))
                        print("Threshold values updated in MySQL.")
                        self.mutex.release()

                        # Cập nhật giá trị ngưỡng mới
                        self.nhietdo_lower = new_nhietdo_lower
                        self.nhietdo_high = new_nhietdo_high

                    if temperature is not None:
                        # Thêm dữ liệu vào bảng new_table
                        query = "INSERT INTO new_table (client_address, temperature, nhietdo_lower, nhietdo_high, time) VALUES (%s,%s,%s,%s,%s);"
                        values = (client_address, temperature, self.nhietdo_lower, self.nhietdo_high, current_time)
                        self.mutex.acquire()
                        mycursor.execute(query, values)
                        print("Data sent to MySQL successfully. nhietdo_tram70")
                        self.mutex.release()

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
                    
                    mycursor = mydb.cursor()
                    
                    # Kiểm tra xem có giá trị ngưỡng mới không
                    if doam_low is not None or doam_high is not None:
                        new_doam_lower = self.doam_low if doam_low is None else doam_low
                        new_doam_high = self.doam_high if doam_high is None else doam_high

                        # Xây dựng câu lệnh SQL cập nhật giá trị ngưỡng
                        query = "UPDATE new_table SET doam_low = %s, doam_high = %s WHERE client_address = %s ORDER BY time DESC LIMIT 1"
                        # Thực hiện câu lệnh SQL cập nhật giá trị ngưỡng
                        self.mutex_doam.acquire()
                        mycursor.execute(query, (new_doam_lower, new_doam_high, client_address))
                        print("Threshold values updated in MySQL.")
                        self.mutex_doam.release()

                        # Cập nhật giá trị ngưỡng mới
                        self.doam_low = new_doam_lower
                        self.doam_high = new_doam_high

                    if humidity is not None:
                        # Thêm dữ liệu vào bảng new_table
                        query = "INSERT INTO new_table (client_address, humidity, doam_low, doam_high, time) VALUES (%s,%s,%s,%s,%s);"
                        values = (client_address, humidity, self.doam_low, self.doam_high, current_time)
                        self.mutex_doam.acquire()
                        mycursor.execute(query, values)
                        print("Data sent to MySQL successfully. doam_tram70")
                        self.mutex_doam.release()

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
                
                
                mycursor = mydb.cursor()
                
                # Kiểm tra xem có giá trị ngưỡng mới không
                if dienap_low is not None or dienap_high is not None or dienap_low1 is not None:
                    new_dienap_low = self.dienap_low if dienap_low is None else dienap_low
                    new_dienap_low1 = self.dienap_low1 if dienap_low1 is None else dienap_low1
                    new_dienap_high = self.dienap_high if dienap_high is None else dienap_high

                    # Xây dựng câu lệnh SQL cập nhật giá trị ngưỡng
                    query = "UPDATE new_table SET dienap_low = %s, dienap_low1 = %s, dienap_high = %s WHERE client_address = %s ORDER BY time DESC LIMIT 1"
                    
                    # Thực hiện câu lệnh SQL cập nhật giá trị ngưỡng
                    self.mutex_dienap.acquire()
                    mycursor.execute(query, (new_dienap_low, new_dienap_low1, new_dienap_high, client_address))
                    print("Threshold values updated in MySQL.")
                    self.mutex_dienap.release()
                    self.dienap_low = new_dienap_low
                    self.dienap_low1 = new_dienap_low1
                    self.dienap_high = new_dienap_high
                if voltage_dc1 is not None:
                    # Thêm dữ liệu vào bảng new_table
                    query = "INSERT INTO new_table (client_address, voltage_dc1, dienap_low, dienap_low1, dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc1, self.dienap_low, self.dienap_low1,  self.dienap_high, current_time)
                    self.mutex_dienap.acquire()
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc1")
                    self.mutex_dienap.release()

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
                
                
                mycursor = mydb.cursor()
                
                # Kiểm tra xem có giá trị ngưỡng mới không
                if dienap_low is not None or dienap_high is not None or dienap_low1 is not None:
                    new_dienap_low = self.dienap_low if dienap_low is None else dienap_low
                    new_dienap_low1 = self.dienap_low1 if dienap_low1 is None else dienap_low1
                    new_dienap_high = self.dienap_high if dienap_high is None else dienap_high

                    # Xây dựng câu lệnh SQL cập nhật giá trị ngưỡng
                    query = "UPDATE new_table SET dienap_low = %s, dienap_low1 = %s, dienap_high = %s WHERE client_address = %s ORDER BY time DESC LIMIT 1"
                    
                    # Thực hiện câu lệnh SQL cập nhật giá trị ngưỡng
                    self.mutex_dienap.acquire()
                    mycursor.execute(query, (new_dienap_low, new_dienap_low1, new_dienap_high, client_address))
                    print("Threshold values updated in MySQL.")
                    self.mutex_dienap.release()
                     # Cập nhật giá trị ngưỡng mới
                    self.dienap_low = new_dienap_low
                    self.dienap_low1 = new_dienap_low1
                    self.dienap_high = new_dienap_high
                      

                if voltage_dc2 is not None:
                    # Thêm dữ liệu vào bảng new_table
                    query = "INSERT INTO new_table (client_address, voltage_dc2, dienap_low, dienap_low1, dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc2, self.dienap_low, self.dienap_low1,  self.dienap_high, current_time)
                    self.mutex_dienap.acquire()
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc2_tram70")
                    self.mutex_dienap.release()

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
                    print("Data sent to MySQL successfully. ac_tram70")
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
                    print("Data sent to MySQL successfully. ac2_tram70")
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
                    
                    mycursor = mydb.cursor()
                    
                    # Kiểm tra xem có giá trị ngưỡng mới không
                    if nhietdo_lower is not None or nhietdo_high is not None:
                        new_nhietdo_lower = self.nhietdo_lower if nhietdo_lower is None else nhietdo_lower
                        new_nhietdo_high = self.nhietdo_high if nhietdo_high is None else nhietdo_high

                        # Xây dựng câu lệnh SQL cập nhật giá trị ngưỡng
                        query = "UPDATE new_table SET nhietdo_lower = %s, nhietdo_high = %s WHERE client_address = %s ORDER BY time DESC LIMIT 1"
                        # Thực hiện câu lệnh SQL cập nhật giá trị ngưỡng
                        self.mutex.acquire()
                        mycursor.execute(query, (new_nhietdo_lower, new_nhietdo_high, client_address))
                        print("Threshold values updated in MySQL.")
                        self.mutex.release()

                        # Cập nhật giá trị ngưỡng mới
                        self.nhietdo_lower = new_nhietdo_lower
                        self.nhietdo_high = new_nhietdo_high

                    if temperature is not None:
                        # Thêm dữ liệu vào bảng new_table
                        query = "INSERT INTO new_table (client_address, temperature, nhietdo_lower, nhietdo_high, time) VALUES (%s,%s,%s,%s,%s);"
                        values = (client_address, temperature, self.nhietdo_lower, self.nhietdo_high, current_time)
                        self.mutex.acquire()
                        mycursor.execute(query, values)
                        print("Data sent to MySQL successfully. nhietdo")
                        self.mutex.release()

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
                    
                    mycursor = mydb.cursor()
                    
                    # Kiểm tra xem có giá trị ngưỡng mới không
                    if doam_low is not None or doam_high is not None:
                        new_doam_lower = self.doam_low if doam_low is None else doam_low
                        new_doam_high = self.doam_high if doam_high is None else doam_high

                        # Xây dựng câu lệnh SQL cập nhật giá trị ngưỡng
                        query = "UPDATE new_table SET doam_low = %s, doam_high = %s WHERE client_address = %s ORDER BY time DESC LIMIT 1"
                        # Thực hiện câu lệnh SQL cập nhật giá trị ngưỡng
                        self.mutex_doam.acquire()
                        mycursor.execute(query, (new_doam_lower, new_doam_high, client_address))
                        print("Threshold values updated in MySQL.")
                        self.mutex_doam.release()

                        # Cập nhật giá trị ngưỡng mới
                        self.doam_low = new_doam_lower
                        self.doam_high = new_doam_high

                    if humidity is not None:
                        # Thêm dữ liệu vào bảng new_table
                        query = "INSERT INTO new_table (client_address, humidity, doam_low, doam_high, time) VALUES (%s,%s,%s,%s,%s);"
                        values = (client_address, humidity, self.doam_low, self.doam_high, current_time)
                        self.mutex_doam.acquire()
                        mycursor.execute(query, values)
                        print("Data sent to MySQL successfully. doam")
                        self.mutex_doam.release()

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
        
                mycursor = mydb.cursor()
                
                # Kiểm tra xem có giá trị ngưỡng mới không
                if dienap_low is not None or dienap_high is not None or dienap_low1 is not None:
                    new_dienap_low = self.dienap_low if dienap_low is None else dienap_low
                    new_dienap_low1 = self.dienap_low1 if dienap_low1 is None else dienap_low1
                    new_dienap_high = self.dienap_high if dienap_high is None else dienap_high

                    # Xây dựng câu lệnh SQL cập nhật giá trị ngưỡng
                    query = "UPDATE new_table SET dienap_low = %s, dienap_low1 = %s, dienap_high = %s WHERE client_address = %s ORDER BY time DESC LIMIT 1"
                    
                    # Thực hiện câu lệnh SQL cập nhật giá trị ngưỡng
                    self.mutex_dienap.acquire()
                    mycursor.execute(query, (new_dienap_low, new_dienap_low1, new_dienap_high, client_address))
                    print("Threshold values updated in MySQL.")
                    self.mutex_dienap.release()
                    self.dienap_low = new_dienap_low
                    self.dienap_low1 = new_dienap_low1
                    self.dienap_high = new_dienap_high
                      

                if voltage_dc1 is not None:
                    # Thêm dữ liệu vào bảng new_table
                    query = "INSERT INTO new_table (client_address, voltage_dc1, dienap_low, dienap_low1, dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                    values = (client_address, voltage_dc1, self.dienap_low, self.dienap_low1,  self.dienap_high, current_time)
                    self.mutex_dienap.acquire()
                    mycursor.execute(query, values)
                    print("Data sent to MySQL successfully. dc1")
                    self.mutex_dienap.release()

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
               
                    mycursor = mydb.cursor()
                    
                    # Kiểm tra xem có giá trị ngưỡng mới không
                    if dienap_low is not None or dienap_high is not None or dienap_low1 is not None:
                        new_dienap_low = self.dienap_low if dienap_low is None else dienap_low
                        new_dienap_low1 = self.dienap_low1 if dienap_low1 is None else dienap_low1
                        new_dienap_high = self.dienap_high if dienap_high is None else dienap_high

                        # Xây dựng câu lệnh SQL cập nhật giá trị ngưỡng
                        query = "UPDATE new_table SET dienap_low = %s, dienap_low1 = %s, dienap_high = %s WHERE client_address = %s ORDER BY time DESC LIMIT 1"
                        
                        # Thực hiện câu lệnh SQL cập nhật giá trị ngưỡng
                        self.mutex_dienap.acquire()
                        mycursor.execute(query, (new_dienap_low, new_dienap_low1, new_dienap_high, client_address))
                        print("Threshold values updated in MySQL.")
                        self.mutex_dienap.release()
                        self.dienap_low = new_dienap_low
                        self.dienap_low1 = new_dienap_low1
                        self.dienap_high = new_dienap_high
                      

                    if voltage_dc2 is not None:
                        # Thêm dữ liệu vào bảng new_table
                        query = "INSERT INTO new_table (client_address, voltage_dc2, dienap_low, dienap_low1, dienap_high, time) VALUES (%s,%s,%s,%s,%s,%s);"
                        values = (client_address, voltage_dc2, self.dienap_low, self.dienap_low1,  self.dienap_high, current_time)
                        self.mutex_dienap.acquire()
                        mycursor.execute(query, values)
                        print("Data sent to MySQL successfully. dc2")
                        self.mutex_dienap.release()

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
                    print("Data sent to MySQL successfully. ac1_tram45")
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
                    print("Data sent to MySQL successfully. ac2_tram45")
                mydb.commit()
                
            except mysql.connector.Error as error:
                print("Error inserting data into MySQL:", error)
