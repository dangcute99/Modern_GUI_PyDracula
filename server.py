import sys
import os
from datetime import datetime, timedelta
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
# IMPORT / GUI AND MODULES AND WIDGETS
from modules import *
from login import Ui_Form
from singin import Ui_Form_Singin
from problem import Problem
from connectMysql import Connect_MySql
from modules.app_functions import AppFunctions
os.environ["QT_FONT_DPI"] = "96" 
# SET AS GLOBAL WIDGETS
tram70 ="172.20.10.48"
tram45 ="172.20.10.01"
tram01 ="172.20.10.02"
tram48="172.20.10.4"
tram71="172.20.10.71"
tram76="172.20.10.76"
bit_humi_a70=None
bit_temp_a70=None
bit_light_70=None
bit_ac1_a70=None
bit_ac2_a70=None
bit_dc1_a70=None
bit_dc2_a70=None
bit_humi_a45=None
bit_temp_a45=None
bit_light_45 = None
bit_ac1_a45=None
bit_ac2_a45=None
bit_dc1_a45=None
bit_dc2_a45=None
bit_humi_a48=None
bit_temp_a48=None
bit_ac1_a48=None
bit_ac2_a48=None
bit_dc1_a48=None
bit_dc2_a48=None
bit_humi_a01=None
bit_temp_a01=None
bit_ac1_a01=None
bit_ac2_a01=None
bit_dc1_a01=None
bit_dc2_a01=None
bit_humi_a71=None
bit_temp_a71=None
bit_ac1_a71=None
bit_ac2_a71=None
bit_dc1_a71=None
bit_dc2_a71=None
bit_humi_a76=None
bit_temp_a76=None
bit_ac1_a76=None
bit_ac2_a76=None
bit_dc1_a76=None
bit_dc2_a76=None
bit_canh_bao_a70 =None
bit_canh_bao_a45 =None
bit_canh_bao_a01 = None
bit_canh_bao=None
bit_coi=None
host=None
user=None
password=None

# ///////////////////////////////////////////////////////////////
widgets = None
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
pygame.mixer.init()
pygame.mixer.music.load(resource_path('images/sound/Tieng-bip-bao-dong-www_tiengdong_com.mp3'))
plt.rcParams['figure.max_open_warning'] = 50

class MainWindow(QMainWindow): 
    dataReceived = Signal(str,float,float,float,float,float,float,float,float,float,float,float,float,float,float,datetime.datetime)
    alertSignal = Signal(str, str,bool,int)
    global bit_canh_bao_a01,bit_light_70,bit_light_45,bit_canh_bao_a45,bit_canh_bao_a70,bit_humi_a70,bit_temp_a70,bit_ac1_a70,bit_ac2_a70,bit_dc1_a70,bit_dc2_a70,bit_humi_a45,bit_temp_a45,bit_ac1_a45,bit_ac2_a45,bit_dc1_a45,bit_dc2_a45,bit_humi_a48,bit_temp_a48,bit_ac1_a48,bit_ac2_a48,bit_dc1_a48,bit_dc2_a48,bit_humi_a01,bit_temp_a01,bit_ac1_a01,bit_ac2_a01,bit_dc1_a01,bit_dc2_a01,bit_humi_a71,bit_temp_a71,bit_ac1_a71,bit_ac2_a71,bit_dc1_a71,bit_dc2_a71,bit_humi_a76,bit_temp_a76,bit_ac1_a76,bit_ac2_a76,bit_dc1_a76,bit_dc2_a76,bit_canh_bao,bit_coi
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # self.problem = None 
        # self.problem = Problem() 
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        global widgets
        widgets = self.ui
        self.current_widget = None
        self.problem_dialog = None
        self.problem_dialog_2 =None
        self.mysql_dialog = None
        self.selected_start_date = None
        self.selected_end_date = None
        self.active_button = None  
        self.ui.widget_99.setVisible(False)
        self.ui.widget_101.setVisible(False)
        self.ui.widget_102.setVisible(False)
        self.old_alert_flag =False
        self.alert_flag = False
       
        self.sound_thread = SoundThread()
        self.sound_thread.finished.connect(self.handleSoundFinished)

        # CHỨC NĂNG 
        self.sensor_receiver = SensorDataReceiver(socket.gethostname(),8234)
        # Start listening for connections
        self.sensor_receiver.start_listening()
        
        # self.sensor_receiver.alertSignal.connect(self.change_led_color_noReceivedata)
        self.canvas = MatplotlibCanvasNhietdo()
        self.canvasNhietdo = MatplotlibCanvasNhietdo2()
        self.canvasdoam = MatplotlibCanvasDoam()
        self.canvasdoam_2 = MatplotlibCanvasDoam2()
        self.canvasdienap = MatplotlibCanvasDienap()
        self.canvasdienap2 =MatplotlibCanvasDienap2()
        self.canvasdienap3 = MatplotlibCanvasDienap3()
        self.canvasdienap4 =MatplotlibCanvasDienap4()
        self.canvasnhietdo01 = MatplotlibCanvasNhietdo01()
        self.canvasdoam01 = MatplotlibCanvasDoam01()
        self.canvasdienap01_1 = MatplotlibCanvasDienap011()
        self.canvasdienap01_2=MatplotlibCanvasDienap012()
        self.canvasnhietdo48 = MatplotlibCanvasNhietdo48()
        self.canvasdoam48 = MatplotlibCanvasDoam48()
        self.canvasdienap48_1 = MatplotlibCanvasDienap148()
        self.canvasdienap48_2 =  MatplotlibCanvasDienap248()
        self.canvasnhietdo71 = MatplotlibCanvasNhietdo71()
        self.canvasdoam71 = MatplotlibCanvasDoam71()
        self.canvasdienap71_1 = MatplotlibCanvasDienap171()
        self.canvasdienap71_2 =  MatplotlibCanvasDienap271()
        self.canvasnhietdo76 = MatplotlibCanvasNhietdo76()
        self.canvasdoam76 = MatplotlibCanvasDoam76()
        self.canvasdienap76_1 = MatplotlibCanvasDienap176()
        self.canvasdienap76_2 =  MatplotlibCanvasDienap276()
        self.sensor_receiver.dataReceived.connect(self.canvas.update_figureNhietdo)
        self.sensor_receiver.dataReceived.connect(self.canvasNhietdo.update_figureNhietdo2)
        self.sensor_receiver.dataReceived.connect(self.canvasdoam.update_figureDoam)
        self.sensor_receiver.dataReceived.connect(self.canvasdoam_2.update_figureDoam2)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap.update_figureDienap)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap2.update_figureDienap2)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap3.update_figureDienap3)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap4.update_figureDienap4)
        self.sensor_receiver.dataReceived.connect(self.canvasnhietdo01.update_figureNhietdo01)
        self.sensor_receiver.dataReceived.connect(self.canvasdoam01.update_figureDoam01)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap01_1.update_figureDienap011)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap01_2.update_figureDienap012)
        self.sensor_receiver.dataReceived.connect(self.canvasnhietdo48.update_figureNhietdo48)
        self.sensor_receiver.dataReceived.connect(self.canvasdoam48.update_figureDoam48)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap48_1.update_figureDienap148)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap48_2.update_figureDienap248)
        self.sensor_receiver.dataReceived.connect(self.canvasnhietdo71.update_figureNhietd71)
        self.sensor_receiver.dataReceived.connect(self.canvasdoam71.update_figureDoam71)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap71_1.update_figureDienap171)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap71_2.update_figureDienap271)
        self.sensor_receiver.dataReceived.connect(self.canvasnhietdo76.update_figureNhietdo76)
        self.sensor_receiver.dataReceived.connect(self.canvasdoam76.update_figureDoam76)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap76_1.update_figureDienap176)
        self.sensor_receiver.dataReceived.connect(self.canvasdienap76_2.update_figureDienap276)

        self.ui.screen_nhietdo.addWidget(self.canvas)
        self.ui.screen_nhietdo_2.addWidget(self.canvasNhietdo)
        self.ui.screen_doam.addWidget(self.canvasdoam)
        self.ui.screen_doam_2.addWidget(self.canvasdoam_2)
        self.ui.screen_dienap.addWidget(self.canvasdienap)
        self.ui.screen_dienap_2.addWidget(self.canvasdienap2)
        self.ui.screen_dienap_3.addWidget(self.canvasdienap3)
        self.ui.screen_dienap_4.addWidget(self.canvasdienap4)
        self.ui.screen_nhietdo_3.addWidget(self.canvasnhietdo01)
        self.ui.screen_doam_5.addWidget(self.canvasdoam01)
        self.ui.screen_dienap_5.addWidget(self.canvasdienap01_1)
        self.ui.screen_dienap_6.addWidget(self.canvasdienap01_2)

        self.ui.screen_nhietdo_4.addWidget(self.canvasnhietdo48)
        self.ui.screen_doam_6.addWidget(self.canvasdoam48)
        self.ui.screen_dienap_11.addWidget(self.canvasdienap48_1)
        self.ui.screen_dienap_12.addWidget(self.canvasdienap48_2)

        self.ui.screen_nhietdo_5.addWidget(self.canvasnhietdo71)
        self.ui.screen_doam_4.addWidget(self.canvasdoam71)
        self.ui.screen_dienap_7.addWidget(self.canvasdienap71_1)
        self.ui.screen_dienap_8.addWidget(self.canvasdienap71_2)

        self.ui.screen_nhietdo_11.addWidget(self.canvasnhietdo76)
        self.ui.screen_doam_3.addWidget(self.canvasdoam76)
        self.ui.screen_dienap_9.addWidget(self.canvasdienap76_1)
        self.ui.screen_dienap_10.addWidget(self.canvasdienap76_2)

        # button connect option account mysql
        # self.ui.pushButton_3.clicked.connect(self.openChoiceConnectionMysql)

        
        # self.setup_toolbox()
        widgets.pushButton_suco_tram70.clicked.connect(self.show_problem_dock)
        widgets.pushButton_suco_tram45.clicked.connect(self.show_problem_dock2)
        widgets.pushButton_suco_tram01.clicked.connect(self.show_problem_dock01)
        widgets.pushButton_155.clicked.connect(self.show_problem_dock_48)
        widgets.pushButton_150.clicked.connect(self.show_problem_dock_71)
        widgets.pushButton_145.clicked.connect(self.show_problem_dock_76)

        widgets.pushButton_exportTem_3.clicked.connect(self.export_to_exceltemp)
        widgets.pushButton_exportTem_11.clicked.connect(self.export_to_excelhum)
        widgets.pushButton_exportTem_9.clicked.connect(self.export_to_exceldc1)
        widgets.pushButton_exportTem_14.clicked.connect(self.export_to_exceldc2)
        widgets.pushButton_exportTem_10.clicked.connect(self.export_to_excelac1)
        widgets.pushButton_exportTem_15.clicked.connect(self.export_to_excelac2)

        widgets.pushButton_exportTem_2.clicked.connect(self.export_to_exceltemp_2)
        widgets.pushButton_exportTem_8.clicked.connect(self.export_to_excelhum_2)
        widgets.pushButton_exportTem_6.clicked.connect(self.export_to_exceldc1_2)
        widgets.pushButton_exportTem_12.clicked.connect(self.export_to_exceldc2_2)
        widgets.pushButton_exportTem_7.clicked.connect(self.export_to_excelac1_2)
        widgets.pushButton_exportTem_13.clicked.connect(self.export_to_excelac2_2)

  
        
        widgets.pushButton_157.clicked.connect(self.close_socket_and_app)
        widgets.pushButton_156.clicked.connect(self.tat_canh_bao)
        widgets.pushButton_163.clicked.connect(self.tat_canh_bao)
        widgets.pushButton_199.clicked.connect(self.tat_canh_bao)
        # self.sensor_receiver.dataReceived.connect(self.update_thresholds)

        # self.sensor_receiver.alertSignal.connect(self.check_condition_tram)
        self.sensor_receiver.dataReceived.connect(self.update_label)
        self.sensor_receiver.dataReceived.connect(self.update_label_tram45)
        

        self.nhietdo_lower = float(20)
        self.nhietdo_high = float(25)
        self.doam_low = float(40)  
        self.doam_high = float(70)
        self.dienap_low =float(47)
        self.dienap_low1 =float(48)
        self.dienap_high =float(58.5)

        self.nhietdo_lower_tram45 = float(20)
        self.nhietdo_high_tram45 = float(25)
        self.doam_low_tram45 = float(40)  
        self.doam_high_tram45 = float(80)
        self.dienap_low_tram45 =float(47)
        self.dienap_low1_tram45 =float(48)
        self.dienap_high_tram45 =float(58.5)

        self.start_time = datetime.datetime.now()
        self.last_entry_times = {}
        # Timer for checking missing entries
        self.check_timer = QTimer(self)
        # self.check_timer.timeout.connect(self.canh_Bao_Tram01)
        self.check_timer.start(1000) 
        self.sound_enabled = True
       
        
        self.button_widget_map = {
            "pushButton_17": widgets.page,

            "pushButton_tram_45": widgets.page_2,
            "pushButton_tram_01": widgets.page_3,
            "pushButton_tram_48": widgets.page_4,
            "pushButton_tram_71": widgets.page_5,
            "pushButton_tram_76": widgets.page_6,

           

            "pushButton_tram45_home":widgets.home,
            "pushButton_tram01_home":widgets.home,
            "pushButton_tram48_home":widgets.home,
            "pushButton_tram71_home":widgets.home,
            "pushButton_tram76_home":widgets.home,
            
            "pushButton_nhietdo_tram70": widgets.Nhietdo,
            "pushButton_161": widgets.home,
            "pushButton_doam_tram70": widgets.Doam,
            "pushButton_dienap_tram70": widgets.Dienap,

            "pushButton_162": widgets.page,
            "pushButton_tram70_doam": widgets.page,
            "pushButton_tram70_dienap": widgets.page,
            "pushButton_tram70_suco": widgets.page,
            "pushButton_suco_tram70":widgets.suco,

            "pushButton_168": widgets.page_2,
            "pushButton_tram01_doam_45": widgets.page_2,
            "pushButton_tram45_dienap_45": widgets.page_2,
            "pushButton_tram70_suco_2": widgets.page_2,
            "pushButton_suco_tram45":widgets.suco_2,
            
            "pushButton_tram01_nhietdo_01": widgets.page_3,
            "pushButton_tram01_doam_01": widgets.page_3,
            "pushButton_tram01_dienap_01": widgets.page_3,
            "pushButton_tram01_suco_3": widgets.page_3,
            "pushButton_suco_tram01":widgets.suco_3,

            "pushButton_tram48_nhietdo_48": widgets.page_4,
            "pushButton_tram48_doam_48": widgets.page_4,
            "pushButton_tram48_dienap_48": widgets.page_4,
            "pushButton_tram48_suco_4": widgets.page_4,
            "pushButton_155":widgets.suco_4,

            "pushButton_tram71_nhietdo_71": widgets.page_5,
            "pushButton_tram71_doam_71": widgets.page_5,
            "pushButton_tram71_dienap_71": widgets.page_5,
            "pushButton_tram71_suco_5": widgets.page_5,
            "pushButton_150":widgets.suco_5,

            "pushButton_tram76_nhietdo_76": widgets.page_6,
            "pushButton_tram76_doam_76": widgets.page_6,
            "pushButton_tram76_dienap_76": widgets.page_6,
            "pushButton_tram76_suco_6": widgets.page_6,
            "pushButton_145":widgets.suco_6,
            
            #############################################

            "pushButton_nhietdo_tram45": widgets.Nhietdo_2,
            "pushButton_doam_tram45": widgets.Doam_2,
            "pushButton_dienap_tram45": widgets.Dienap_2,
            "pushButton_suco_tram45":widgets.suco_2,
           
            "pushButton_nhietdo_tram01": widgets.nhietdo_3,
            "pushButton_doam_tram01": widgets.doam_3,
            "pushButton_dienap_tram01": widgets.dienap_3,
            "pushButton_suco_tram01": widgets.suco_3,
            
            "pushButton_152": widgets.nhietdo_4,
            "pushButton_153": widgets.doam_4,
            "pushButton_154": widgets.dienap_4,
            "pushButton_155": widgets.suco_4,

            "pushButton_147": widgets.nhietdo_5,
            "pushButton_148": widgets.doam_5,
            "pushButton_149": widgets.dienap_5,
            "pushButton_150": widgets.suco_5,
            
            "pushButton_142": widgets.nhietdo_6,
            "pushButton_143": widgets.doam_6,
            "pushButton_144": widgets.dienap_6,
            "pushButton_145": widgets.suco_6,
            "pushButton_HDSD_4":widgets.huondansd,
            "pushButton_HDSD_5":widgets.huondansd,
            "pushButton_tram76_home_2": widgets.page,
        }
        self.menu_layout = QVBoxLayout()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label_datetime)
        self.timer.start(1000)
        # Connect the buttonClick function to all buttons
        for button_name in self.button_widget_map.keys():
            button = getattr(widgets, button_name)
            button.clicked.connect(self.buttonClick)

        self.show()
    def tat_canh_bao(self):
        global bit_coi,bit_canh_bao
        
        bit_coi=0
    def handleSoundFinished(self):
        self.sound_thread.sound_enabled = False
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        # Set the current widget based on the button clicked
        if btnName in self.button_widget_map:
            widgets.stackedWidget.setCurrentWidget(self.button_widget_map[btnName])      
    def close_socket_and_app(self):
        try:
            self.sensor_receiver.socket_server.close()
            print("Socket closed.")
        except Exception as e:
            print("Error closing socket:", str(e))

        sys.exit()        
    def update_label_datetime(self):
        current_datetime = QDateTime.currentDateTime()
        formatted_datetime = current_datetime.toString("dd/MM/yyyy, hh:mm:ss")
        self.ui.label_2.setText(formatted_datetime)
        self.ui.label_3.setText(formatted_datetime)
        self.ui.label_126.setText(formatted_datetime)
        self.ui.label_128.setText(formatted_datetime)
        self.ui.thoigian_nhietdo.setText(formatted_datetime)
        self.ui.thoigian_nhietdo_2.setText(formatted_datetime)
        self.ui.label_thoigian_dienap_2.setText(formatted_datetime)
        self.ui.label_thoigian_doam.setText(formatted_datetime)
        self.ui.label_thoigian_dienap.setText(formatted_datetime)
        self.ui.label_thoigian_doam_2.setText(formatted_datetime)
    def apply_button_styles(self, button_styles):
        for button, style in button_styles.items():
            button.setStyleSheet(style)   
   
    def update_label_tram45(self,client_address, temperature, humidity, light,voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high):
            global bit_light_70,bit_light_45,bit_canh_bao_a70,bit_canh_bao_a45,bit_canh_bao,bit_humi_a70,bit_temp_a70,bit_ac1_a70,bit_ac2_a70,bit_dc1_a70,bit_dc2_a70,bit_humi_a45,bit_temp_a45,bit_ac1_a45,bit_ac2_a45,bit_dc1_a45,bit_dc2_a45,bit_humi_a01,bit_temp_a01,bit_ac1_a01,bit_ac2_a01,bit_dc1_a01,bit_dc2_a01,bit_humi_a48,bit_temp_a48,bit_ac1_a48,bit_ac2_a48,bit_dc1_a48,bit_dc2_a48,bit_humi_a01,bit_temp_a01,bit_ac1_a01,bit_ac2_a01,bit_dc1_a01,bit_dc2_a01,bit_humi_a71,bit_temp_a71,bit_ac1_a71,bit_ac2_a71,bit_dc1_a71,bit_dc2_a71,bit_humi_a76,bit_temp_a76,bit_ac1_a76,bit_ac2_a76,bit_dc1_a76,bit_dc2_a76,bit_canh_bao,bit_coi
            if client_address == tram45:
                
                if nhietdo_lower is not None and nhietdo_lower != 0  :
                        self.nhietdo_lower_tram45 = nhietdo_lower
                        if float(self.nhietdo_lower_tram45) <= float(self.temperature) <= float(self.nhietdo_high_tram45):
                            common_style = "background-color: rgb(0, 170, 0);"
                            bit_temp_a45 = 0
                           
                        else:
                            common_style = "background-color: rgb(255, 0, 0);"  # Màu đỏ
                            bit_temp_a45 = 1
                            bit_coi = 1

                        # Áp dụng màu nút
                        button_styles = {
                            self.ui.pushButton_nhietdo_2: common_style + " border-radius: 17px;",
                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                            self.ui.pushButton_188: common_style ,
                        }
                        self.apply_button_styles(button_styles)
                if nhietdo_high is not None and nhietdo_high != 0:
                            self.nhietdo_high_tram45 = nhietdo_high
                            if float(self.nhietdo_lower_tram45) <= float(self.temperature) <= float(self.nhietdo_high_tram45):
                                common_style = "background-color: rgb(0, 170, 0);"  # Màu xanh
                                bit_temp_a45 = 0
                            else:
                                common_style = "background-color: rgb(255, 0, 0);"  # Màu đỏ
                                bit_temp_a45 = 1
                                bit_coi = 1

                            # Áp dụng màu nút
                            button_styles = {
                                self.ui.pushButton_nhietdo_2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_188: common_style ,
                            }
                            self.apply_button_styles(button_styles)

                if doam_low is not None and doam_low != 0  :
                            self.doam_low_tram45 = doam_low
                            if float(self.doam_low_tram45) <= float(self.humidity) <= float(self.doam_high_tram45):
                                common_style = "background-color: rgb(0, 170, 0);"
                                bit_humi_a45 = 0
                               
                            else:
                                common_style = "background-color: rgb(255, 0, 0);"  # Màu đỏ
                                bit_humi_a45 = 1
                                bit_coi = 1

                            # Áp dụng màu nút
                            button_styles = {
                                self.ui.pushButton_doam_2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_188: common_style ,
                                }
                            self.apply_button_styles(button_styles)          
                    # Cập nhật ngưỡng nhiệt độ trên
                if doam_high is not None and doam_high != 0:
                    self.doam_high_tram45 = doam_high
                    if float(self.doam_low_tram45) <= float(self.humidity) <= float(self.doam_high_tram45):
                        common_style = "background-color: rgb(0, 170, 0);"
                        bit_humi_a45 = 0
                       
                    else:
                        common_style = "background-color: rgb(255, 0, 0);"  # Màu đỏ
                        bit_humi_a45 = 1
                        bit_coi = 1

                    # Áp dụng màu nút
                    button_styles = {
                            self.ui.pushButton_doam_2: common_style + " border-radius: 17px;",
                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                            self.ui.pushButton_188: common_style ,
                        }
                    self.apply_button_styles(button_styles)    
                
                if hasattr(self, 'voltage_dc1'):
                    if dienap_low1 is not None and dienap_low1 != 0  :
                                self.dienap_low1_tram45 = dienap_low1
                                if float(self.dienap_low1_tram45) < float(self.voltage_dc1) <= float(self.dienap_high_tram45):
                                    common_style = "background-color: rgb(0, 170, 0);"
                                    bit_dc1_a45 = 0
                                    
                                    button_styles = {
                                        self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_188: common_style ,
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                elif float(self.dienap_low_tram45) <= float(self.voltage_dc1) <= float(self.dienap_low1_tram45):
                                    common_style = "background-color: rgb(255, 255, 0);"
                                    bit_dc1_a45 = 1
                                    bit_coi=1
                                    button_styles = {
                                        self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                        self.ui.pushButton_188: "background-color: rgb(255, 0, 0);", 
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                    
                                else:
                                    common_style = "background-color: rgb(255, 0, 0);"
                                    bit_dc1_a45 = 1
                                    bit_coi=1
                                    button_styles = {
                                        self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_188: common_style ,
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                if bit_coi == 1:
                                        common_style ="background-color:rgb(255,0,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                            
                                        }
                                        self.apply_button_styles(button_styles)
                                else:
                                        common_style ="background-color:rgb(0,170,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        }
                                        self.apply_button_styles(button_styles)
                    if dienap_low is not None and dienap_low != 0:
                                self.dienap_low_tram45 = dienap_low
                                if float(self.dienap_low1_tram45) < float(self.voltage_dc1) <= float(self.dienap_high_tram45):
                                    common_style = "background-color: rgb(0, 170, 0);"
                                    bit_dc1_a45 = 0
                                    
                                    button_styles = {
                                        self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_188: common_style ,
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                elif float(self.dienap_low_tram45) <= float(self.voltage_dc1) <= float(self.dienap_low1_tram45):
                                    common_style = "background-color: rgb(255, 255, 0);"
                                    bit_dc1_a45 = 1
                                    bit_coi=1
                                    button_styles = {
                                        self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                        self.ui.pushButton_188: "background-color: rgb(255, 0, 0);", 
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                    
                                else:
                                    common_style = "background-color: rgb(255, 0, 0);"
                                    bit_dc1_a45 = 1
                                    bit_coi=1
                                    button_styles = {
                                        self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_188: common_style ,
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                if bit_coi == 1:
                                        common_style ="background-color:rgb(255,0,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                            
                                        }
                                        self.apply_button_styles(button_styles)
                                else:
                                        common_style ="background-color:rgb(0,170,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        }
                                        self.apply_button_styles(button_styles)
                    if dienap_high is not None and dienap_high != 0:
                            self.dienap_high_tram45 = dienap_high
                            if float(self.dienap_low1_tram45) < float(self.voltage_dc1) <= float(self.dienap_high_tram45):
                                common_style = "background-color: rgb(0, 170, 0);"
                                bit_dc1_a45 = 0
                                
                                button_styles = {
                                    self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_188: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            elif self.dienap_low_tram45 <= self.voltage_dc1 <= self.dienap_low1_tram45:
                                common_style = "background-color: rgb(255, 255, 0);"
                                bit_dc1_a45 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_13: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                    self.ui.pushButton_canhbao_2: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                    self.ui.pushButton_188: "background-color: rgb(255, 0, 0);", 
                                
                                }
                                self.apply_button_styles(button_styles)
                                
                            else:
                                common_style = "background-color: rgb(255, 0, 0);"
                                bit_dc1_a45 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_188: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            if bit_coi == 1:
                                    common_style ="background-color:rgb(255,0,0);"
                                    button_styles = {
                                        self.ui.pushButton_188: common_style ,
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        
                                    }
                                    self.apply_button_styles(button_styles)
                            else:
                                    common_style ="background-color:rgb(0,170,0);"
                                    button_styles = {
                                        self.ui.pushButton_188: common_style ,
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                    }
                                    self.apply_button_styles(button_styles)
                if hasattr(self,"voltage_dc2"):                    
                    if dienap_low1 is not None and dienap_low1 != 0  :
                                self.dienap_low1_tram45 = dienap_low1
                                if float(self.dienap_low1_tram45) < float(self.voltage_dc2) <= float(self.dienap_high_tram45):
                                    common_style = "background-color: rgb(0, 170, 0);"
                                    bit_dc2_a45 = 0
                                   
                                    button_styles = {
                                        self.ui.pushButton_dc2_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_188: common_style ,
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                elif float(self.dienap_low_tram45) <= float(self.voltage_dc2) <= float(self.dienap_low1_tram45):
                                    common_style = "background-color: rgb(255, 255, 0);"
                                    bit_dc2_a45 = 1
                                    bit_coi=1
                                    button_styles = {
                                        self.ui.pushButton_dc2_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                        self.ui.pushButton_188: "background-color: rgb(255, 0, 0);", 
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                    
                                else:
                                    common_style = "background-color: rgb(255, 0, 0);"
                                    bit_dc2_a45 = 1
                                    bit_coi=1
                                    button_styles = {
                                        self.ui.pushButton_dc2_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_188: common_style ,
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                if bit_coi == 1:
                                        common_style ="background-color:rgb(255,0,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                            
                                        }
                                        self.apply_button_styles(button_styles)
                                else:
                                        common_style ="background-color:rgb(0,170,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        }
                                        self.apply_button_styles(button_styles)
                    if dienap_low is not None and dienap_low != 0:
                                self.dienap_low_tram45 = dienap_low
                                if float(self.dienap_low1_tram45) < float(self.voltage_dc2) <= float(self.dienap_high_tram45):
                                    common_style = "background-color: rgb(0, 170, 0);"
                                    bit_dc2_a45 = 0
                                  
                                    button_styles = {
                                        self.ui.pushButton_dc2_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_188: common_style ,
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                elif float(self.dienap_low_tram45) <= float(self.voltage_dc2) <= float(self.dienap_low1_tram45):
                                    common_style = "background-color: rgb(255, 255, 0);"
                                    bit_dc2_a45 = 1
                                    bit_coi=1
                                    button_styles = {
                                        self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                        self.ui.pushButton_canhbao: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                        self.ui.pushButton_186: "background-color: rgb(255, 0, 0);", 
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                    
                                else:
                                    common_style = "background-color: rgb(255, 0, 0);"
                                    bit_dc2_a45 = 1
                                    bit_coi=1
                                    button_styles = {
                                        self.ui.pushButton_dc2_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_188: common_style ,
                                    
                                    }
                                    self.apply_button_styles(button_styles)
                                if bit_coi == 1:
                                        common_style ="background-color:rgb(255,0,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                            
                                        }
                                        self.apply_button_styles(button_styles)
                                else:
                                        common_style ="background-color:rgb(0,170,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        }
                                        self.apply_button_styles(button_styles)
                    if dienap_high is not None and dienap_high != 0:
                            self.dienap_high_tram45 = dienap_high
                            if float(self.dienap_low1_tram45) < float(self.voltage_dc2) <= float(self.dienap_high_tram45):
                                common_style = "background-color: rgb(0, 170, 0);"
                                bit_dc2_a45 = 0
                               
                                button_styles = {
                                    self.ui.pushButton_dc2_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_188: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            elif float(self.dienap_low_tram45) <= float(self.voltage_dc2) <= float(self.dienap_low1_tram45):
                                common_style = "background-color: rgb(255, 255, 0);"
                                bit_dc2_a45 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc2_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_13: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                    self.ui.pushButton_canhbao_2: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                    self.ui.pushButton_188: "background-color: rgb(255, 0, 0);", 
                                }
                                self.apply_button_styles(button_styles)
                                
                            else:
                                common_style = "background-color: rgb(255, 0, 0);"
                                bit_dc2_a45 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc2_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_188: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            if bit_coi == 1:
                                        common_style ="background-color:rgb(255,0,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                            
                                        }
                                        self.apply_button_styles(button_styles)
                            else:
                                        common_style ="background-color:rgb(0,170,0);"
                                        button_styles = {
                                            self.ui.pushButton_188: common_style ,
                                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                        }
                                        self.apply_button_styles(button_styles)
 
                if temperature is not None and temperature != 0: 
                        self.ui.label_nhietdo_6.setText(f" Nhiệt độ: {temperature}°C")
                        if temperature is not None:
                            self.temperature = temperature
                        if nhietdo_lower is not None and nhietdo_lower != 0:
                            self.nhietdo_lower_tram45 = nhietdo_lower
                        if nhietdo_high is not None and nhietdo_high != 0:
                            self.nhietdo_high_tram45 = nhietdo_high
                        # Kiểm tra nhiệt độ so với ngưỡng và cập nhật màu nút
                        common_style = ""
                        bit_temp_a45 = 0
                        if self.nhietdo_lower is not None and self.nhietdo_high is not None:
                            if float(self.nhietdo_lower_tram45) <= float(self.temperature) <= float(self.nhietdo_high_tram45):
                                common_style = "background-color: rgb(0, 170, 0);"
                                bit_temp_a45 = 0
                              
                            else:
                                common_style = "background-color: rgb(255, 0, 0);"
                                bit_temp_a45 = 1
                                bit_coi=1           
                            button_styles = {
                                self.ui.pushButton_nhietdo_2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_188: common_style ,
                            }
                            
                            self.apply_button_styles(button_styles)
                if humidity is not None and humidity != 0:
                    self.ui.label_doam_3.setText(f" Độ ẩm: {humidity}%")
                    if humidity is not None:
                        self.humidity = humidity
                    if doam_low is not None and doam_low != 0:
                        self.doam_low_tram45 = doam_low
                    if doam_high is not None and doam_high != 0:
                        self.doam_high_tram45 = doam_high
                    # Kiểm tra nhiệt độ so với ngưỡng và cập nhật màu nút
                    common_style = ""
                    bit_humi_a45 = 0
                   
                    if self.doam_low is not None and self.doam_high is not None:    
                        if float(self.doam_low_tram45) <= float(self.humidity) <= float(self.doam_high_tram45):
                            common_style = "background-color: rgb(0, 170, 0);" 
                            bit_humi_a45 = 0
                        else:
                            bit_humi_a45 = 1
                            bit_coi=1
                            common_style = "background-color: rgb(255, 0, 0);"
                        button_styles = {
                            self.ui.pushButton_doam_2: common_style + " border-radius: 17px;",
                            self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                            self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                            self.ui.pushButton_188: common_style ,
                            
                        }
                        self.apply_button_styles(button_styles)
                if voltage_dc1 is not None and voltage_dc1 !=0:
                    self.ui.label_dc1_2.setText(f" DC1: {voltage_dc1}V")
                    if voltage_dc1 is not None:
                        self.voltage_dc1 = voltage_dc1
                    if dienap_low1 is not None and dienap_low1 != 0:
                        self.dienap_low1_tram45 = dienap_low1
                    if dienap_low is not None and dienap_low != 0:
                        self.dienap_low_tram45 = dienap_low
                    if dienap_high is not None and dienap_high != 0:
                        self.dienap_high_tram45 = dienap_high
                    if self.dienap_low1 is not None and self.dienap_low_tram45 is not None and self.dienap_high_tram45 is not None:
                        if float(self.dienap_low1_tram45) < float(self.voltage_dc1) <= float(self.dienap_high_tram45):
                            common_style = "background-color: rgb(0, 170, 0);"
                            bit_dc1_a45 = 0
                           
                        elif float(self.dienap_low_tram45) <= float(self.voltage_dc1) <= float(self.dienap_low1_tram45):
                            common_style = "background-color: rgb(255, 255, 0);"
                            bit_dc1_a45 = 1
                            bit_coi=1
                            
                        else:
                            common_style = "background-color: rgb(255, 0, 0);"
                            bit_dc1_a45 = 1
                            bit_coi=1
                        
                        button_styles = {
                            self.ui.pushButton_dc1_2: common_style + " border-radius: 17px;",
                        
                            
                        }
                        self.apply_button_styles(button_styles)
                if voltage_dc2 is not None and voltage_dc2 !=0:
                    self.ui.label_dc2_2.setText(f" DC2: {voltage_dc2}V")
                    if voltage_dc2 is not None:
                        self.voltage_dc2 = voltage_dc2
                    if dienap_low1 is not None and dienap_low1 != 0:
                        self.dienap_low1_tram45 = dienap_low1
                    if dienap_low is not None and dienap_low != 0:
                        self.dienap_low_tram45 = dienap_low
                    if dienap_high is not None and dienap_high != 0:
                        self.dienap_high_tram45 = dienap_high
                    if self.dienap_low1_tram45 is not None and self.dienap_low_tram45 is not None and self.dienap_high_tram45 is not None:
                        if float(self.dienap_low1_tram45) < float(self.voltage_dc2) <= float(self.dienap_high_tram45):
                            common_style = "background-color: rgb(0, 170, 0);"
                            bit_dc2_a45 = 0
                            
                        elif float(self.dienap_low_tram45) <= float(self.voltage_dc2) <= float(self.dienap_low1_tram45):
                            common_style = "background-color: rgb(255, 255, 0);"
                            bit_dc2_a45 = 1
                            bit_coi=1
                            
                        else:
                            common_style = "background-color: rgb(255, 0, 0);"
                            bit_dc2_a45 = 1
                            bit_coi=1
                            
                        button_styles = {
                            self.ui.pushButton_dc2_2: common_style + " border-radius: 17px;",
                            
                        }
                        self.apply_button_styles(button_styles)
                if voltage_ac is not None and voltage_ac != 0:
                    if voltage_ac == 1:
                        common_style = "background-color: rgb(255, 0, 0);"
                        bit_ac1_a45=1
                        bit_coi=1
                    elif voltage_ac == 220:
                        common_style = "background-color: rgb(0, 170, 0);"
                        bit_ac1_a45=0
                        
                    button_styles = {
                        self.ui.pushButton_ac1_2: common_style + " border-radius: 17px;",
                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                        
                    }
                    self.apply_button_styles(button_styles)
                if voltage_ac2 is not None and voltage_ac2 != 0 :
                    if voltage_ac2 == 1:
                        common_style = "background-color: rgb(255, 0, 0);"
                        bit_ac2_a45=1
                        bit_coi=1
                       
                    elif voltage_ac2 == 220:
                        common_style = "background-color: rgb(0, 170, 0);"
                        bit_ac2_a45=0
                        
                    button_styles = {
                        self.ui.pushButton_ac2_2: common_style + " border-radius: 17px;",
                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                        
                    }
                    self.apply_button_styles(button_styles)
                if light is not None and light != 0:
                    if light == 1:
                        self.ui.label_anhsang_2.setText("Ánh sáng: Bật")
                        common_style = "background-color: rgb(0, 170, 0);"
                      
                        bit_light_45= 0
                    elif light == 2:
                        self.ui.label_anhsang_2.setText("Ánh sáng: Tắt")
                        common_style = "background-color: rgb(255, 0, 0);"
                        bit_coi=1
                        bit_light_45 =1
                    button_styles = {
                        self.ui.pushButton_anhsang_2: common_style + " border-radius: 17px;",
                        self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                        self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                        
                    }
                    self.apply_button_styles(button_styles)
                          # Màu đỏ
                if (bit_light_45 ==1 or  bit_humi_a45 == 1 or bit_temp_a45 == 1 or bit_ac1_a45 == 1 or bit_ac2_a45 == 1 or bit_dc1_a45 == 1 or bit_dc2_a45 == 1 or bit_humi_a01 == 1 or bit_temp_a01 == 1 or bit_ac1_a01 == 1 or bit_ac2_a01 == 1 or bit_dc1_a01 == 1 or bit_dc2_a01 == 1 or bit_humi_a48 == 1 or bit_temp_a48 == 1 or bit_ac1_a48 == 1 or bit_ac2_a48 == 1 or bit_dc1_a48 == 1 or bit_dc2_a48 == 1 or bit_humi_a01 == 1 or bit_temp_a01 == 1 or bit_ac1_a01 == 1 or bit_ac2_a01 == 1 or bit_dc1_a01 == 1 or bit_dc2_a01 == 1 or bit_humi_a71 == 1 or bit_temp_a71 == 1 or bit_ac1_a71 == 1 or bit_ac2_a71 == 1 or bit_dc1_a71 == 1 or bit_dc2_a71 == 1 or bit_humi_a76 == 1 or bit_temp_a76 == 1 or bit_ac1_a76 == 1 or bit_ac2_a76 == 1 or bit_dc1_a76 == 1 or bit_dc2_a76):
                    bit_coi = 1
                else:
                    bit_coi =0
                if bit_coi == 1:
                                common_style = "background-color: rgb(255, 0, 0);"
                                button_styles = {
                                    self.ui.pushButton_188: common_style ,
                                    self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                                }
                                self.apply_button_styles(button_styles)
                        
                else:
                            common_style ="background-color:rgb(0,170,0);"
                            button_styles = {
                                self.ui.pushButton_188: common_style ,
                                self.ui.pushButton_canhbao_2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_13: common_style + " border-radius: 15px;",
                            }
                            
                            # Apply styles to buttons
                            for button, style in button_styles.items():
                                button.setStyleSheet(style)
                
    def update_label(self,client_address, temperature, humidity, light,voltage_dc1, voltage_dc2,
                                        voltage_ac,voltage_ac2, nhietdo_lower, nhietdo_high, doam_low, doam_high,
                                        dienap_low,dienap_low1, dienap_high):
        global bit_light_70,bit_light_45,bit_canh_bao_a70,bit_canh_bao_a45,bit_canh_bao,bit_humi_a70,bit_temp_a70,bit_ac1_a70,bit_ac2_a70,bit_dc1_a70,bit_dc2_a70,bit_humi_a45,bit_temp_a45,bit_ac1_a45,bit_ac2_a45,bit_dc1_a45,bit_dc2_a45,bit_humi_a01,bit_temp_a01,bit_ac1_a01,bit_ac2_a01,bit_dc1_a01,bit_dc2_a01,bit_humi_a48,bit_temp_a48,bit_ac1_a48,bit_ac2_a48,bit_dc1_a48,bit_dc2_a48,bit_humi_a01,bit_temp_a01,bit_ac1_a01,bit_ac2_a01,bit_dc1_a01,bit_dc2_a01,bit_humi_a71,bit_temp_a71,bit_ac1_a71,bit_ac2_a71,bit_dc1_a71,bit_dc2_a71,bit_humi_a76,bit_temp_a76,bit_ac1_a76,bit_ac2_a76,bit_dc1_a76,bit_dc2_a76,bit_canh_bao,bit_coi
        
        if client_address == tram70 :
            # Cập nhật ngưỡng nhiệt độ dưới
            if nhietdo_lower is not None and nhietdo_lower != 0  :
                    self.nhietdo_lower = nhietdo_lower
                    if float(self.nhietdo_lower) <= float(self.temperature) <= float(self.nhietdo_high):
                        common_style = "background-color: rgb(0, 170, 0);"
                        bit_temp_a70 = 0
                       
                    else:
                        common_style = "background-color: rgb(255, 0, 0);"  # Màu đỏ
                        bit_temp_a70 = 1
                        bit_coi = 1
                    # Áp dụng màu nút
                    button_styles = {
                        self.ui.pushButton_nhietdo: common_style + " border-radius: 17px;",
                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                        self.ui.pushButton_186: common_style ,
                    }
                    self.apply_button_styles(button_styles)
        # Cập nhật ngưỡng nhiệt độ trên
            if nhietdo_high is not None and nhietdo_high != 0:
                        self.nhietdo_high = nhietdo_high
                        if float(self.nhietdo_lower) <= float(self.temperature) <= float(self.nhietdo_high):
                            common_style = "background-color: rgb(0, 170, 0);"  # Màu xanh
                            bit_temp_a70 = 0
                        else:
                            common_style = "background-color: rgb(255, 0, 0);"  # Màu đỏ
                            bit_temp_a70 = 1
                            bit_coi = 1

                        # Áp dụng màu nút
                        button_styles = {
                            self.ui.pushButton_nhietdo: common_style + " border-radius: 17px;",
                            self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                            self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                            self.ui.pushButton_186: common_style ,
                        }
                        self.apply_button_styles(button_styles)
            if doam_low is not None and doam_low != 0  :
                        self.doam_low = doam_low
                        if float(self.doam_low) <= float(self.humidity) <= float(self.doam_high):
                            common_style = "background-color: rgb(0, 170, 0);"
                            bit_humi_a70 = 0
                           
                        else:
                            common_style = "background-color: rgb(255, 0, 0);"  # Màu đỏ
                            bit_humi_a70 = 1
                            bit_coi = 1

                        # Áp dụng màu nút
                        button_styles = {
                                self.ui.pushButton_doam: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                self.ui.pushButton_186: common_style ,
                            }
                        self.apply_button_styles(button_styles)          
            # Cập nhật ngưỡng nhiệt độ trên
            if doam_high is not None and doam_high != 0:
                        self.doam_high = doam_high
                        if  float(self.doam_low) <= float(self.humidity) <= float(self.doam_high):
                            common_style = "background-color: rgb(0, 170, 0);"
                            bit_humi_a70 = 0
                        else:
                            common_style = "background-color: rgb(255, 0, 0);"  # Màu đỏ
                            bit_humi_a70 = 1
                            bit_coi = 1

                        # Áp dụng màu nút
                        button_styles = {
                                self.ui.pushButton_doam: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                self.ui.pushButton_186: common_style ,
                            }
                        self.apply_button_styles(button_styles)          
            # Kiểm tra và cập nhật ngưỡng nhiệt độ
            if hasattr(self, 'voltage_dc1'):
                if dienap_low1 is not None and dienap_low1 != 0  :
                            self.dienap_low1 = dienap_low1
                            if float(self.dienap_low1) < float(self.voltage_dc1) <= float(self.dienap_high):
                                common_style = "background-color: rgb(0, 170, 0);"
                                bit_dc1_a70 = 0
                              
                                button_styles = {
                                    self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_186: common_style ,
                                }
                                self.apply_button_styles(button_styles)
                            elif float(self.dienap_low) <= float(self.voltage_dc1) <= float(self.dienap_low1):
                                common_style = "background-color: rgb(255, 255, 0);"
                                bit_dc1_a70 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                    self.ui.pushButton_canhbao: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                    self.ui.pushButton_186: "background-color: rgb(255, 0, 0);", 
                                
                                }
                                self.apply_button_styles(button_styles)
                                
                            else:
                                common_style = "background-color: rgb(255, 0, 0);"
                                bit_dc1_a70 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_186: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            if bit_coi == 1:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(255,0,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                        
                                    }
                                    self.apply_button_styles(button_styles)
                            else:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(0,170,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    }
                                    # Apply styles to buttons
                                    for button, style in button_styles.items():
                                        button.setStyleSheet(style)
                if dienap_low is not None and dienap_low != 0:
                            self.dienap_low = dienap_low
                            if  float(self.dienap_low1) < float(self.voltage_dc1) <= float(self.dienap_high):
                                common_style = "background-color: rgb(0, 170, 0);"
                                bit_dc1_a70 = 0
                              
                                button_styles = {
                                    self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_186: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            elif float(self.dienap_low) <= float(self.voltage_dc1) <= float(self.dienap_low1):
                                common_style = "background-color: rgb(255, 255, 0);"
                                bit_dc1_a70 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                    self.ui.pushButton_canhbao: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                    self.ui.pushButton_186: "background-color: rgb(255, 0, 0);", 
                                
                                }
                                self.apply_button_styles(button_styles)
                                
                            else:
                                common_style = "background-color: rgb(255, 0, 0);"
                                bit_dc1_a70 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_186: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            if bit_coi == 1:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(255,0,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                        
                                    }
                                    self.apply_button_styles(button_styles)
                            else:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(0,170,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    }
                                    # Apply styles to buttons
                                    for button, style in button_styles.items():
                                        button.setStyleSheet(style)
                if dienap_high is not None and dienap_high != 0:
                        self.dienap_high = dienap_high
                        if  float(self.dienap_low1) < float(self.voltage_dc1) <= float(self.dienap_high):
                            common_style = "background-color: rgb(0, 170, 0);"
                            bit_dc1_a70 = 0
                          
                            button_styles = {
                                self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                self.ui.pushButton_186: common_style ,
                            
                            }
                            self.apply_button_styles(button_styles)
                        elif float(self.dienap_low) <= float(self.voltage_dc1) <= float(self.dienap_low1):
                            common_style = "background-color: rgb(255, 255, 0);"
                            bit_dc1_a70 = 1
                            bit_coi=1
                            button_styles = {
                                self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_12: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                self.ui.pushButton_canhbao: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                self.ui.pushButton_186: "background-color: rgb(255, 0, 0);", 
                            
                            }
                            self.apply_button_styles(button_styles)
                            
                        else:
                            common_style = "background-color: rgb(255, 0, 0);"
                            bit_dc1_a70 = 1
                            bit_coi=1
                            button_styles = {
                                self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                self.ui.pushButton_186: common_style ,
                            
                            }
                            self.apply_button_styles(button_styles)
                        if bit_coi == 1:
                            if client_address == tram70:
                                common_style ="background-color:rgb(255,0,0);"
                                button_styles = {
                                    self.ui.pushButton_186: common_style ,
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    
                                }
                                self.apply_button_styles(button_styles)
                        else:
                            if client_address == tram70:
                                common_style ="background-color:rgb(0,170,0);"
                                button_styles = {
                                    self.ui.pushButton_186: common_style ,
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                }
                                # Apply styles to buttons
                                for button, style in button_styles.items():
                                    button.setStyleSheet(style)
            if hasattr(self,"voltage_dc2"):                    
                if dienap_low1 is not None and dienap_low1 != 0  :
                            self.dienap_low1 = dienap_low1
                            if float(self.dienap_low1) < float(self.voltage_dc1) <= float(self.dienap_high):
                                common_style = "background-color: rgb(0, 170, 0);"
                                bit_dc2_a70 = 0
                                
                                button_styles = {
                                    self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_186: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            elif float(self.dienap_low) <= float(self.voltage_dc2) <= float(self.dienap_low1):
                                common_style = "background-color: rgb(255, 255, 0);"
                                bit_dc2_a70 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                    self.ui.pushButton_canhbao: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                    self.ui.pushButton_186: "background-color: rgb(255, 0, 0);", 
                                
                                }
                                self.apply_button_styles(button_styles)
                                
                            else:
                                common_style = "background-color: rgb(255, 0, 0);"
                                bit_dc2_a70 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_186: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            if bit_coi == 1:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(255,0,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                        
                                    }
                                    self.apply_button_styles(button_styles)
                            else:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(0,170,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    }
                                    # Apply styles to buttons
                                    for button, style in button_styles.items():
                                        button.setStyleSheet(style)
                if dienap_low is not None and dienap_low != 0:
                            self.dienap_low = dienap_low
                            if float(self.dienap_low1) < float(self.voltage_dc1) <= float(self.dienap_high):
                                common_style = "background-color: rgb(0, 170, 0);"
                                bit_dc2_a70 = 0
                                
                                button_styles = {
                                    self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_186: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            elif float(self.dienap_low) <= float(self.voltage_dc2) <= float(self.dienap_low1):
                                common_style = "background-color: rgb(255, 255, 0);"
                                bit_dc2_a70 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                    self.ui.pushButton_canhbao: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                    self.ui.pushButton_186: "background-color: rgb(255, 0, 0);", 
                                
                                }
                                self.apply_button_styles(button_styles)
                                
                            else:
                                common_style = "background-color: rgb(255, 0, 0);"
                                bit_dc2_a70 = 1
                                bit_coi=1
                                button_styles = {
                                    self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                    self.ui.pushButton_186: common_style ,
                                
                                }
                                self.apply_button_styles(button_styles)
                            if bit_coi == 1:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(255,0,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                        
                                    }
                                    self.apply_button_styles(button_styles)
                            else:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(0,170,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    }
                                    # Apply styles to buttons
                                    for button, style in button_styles.items():
                                        button.setStyleSheet(style)
                if dienap_high is not None and dienap_high != 0:
                        self.dienap_high = dienap_high
                        if float(self.dienap_low1) < float(self.voltage_dc2) <= float(self.dienap_high):
                            common_style = "background-color: rgb(0, 170, 0);"
                            bit_dc2_a70 = 0
                            
                            button_styles = {
                                self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                self.ui.pushButton_186: common_style ,
                            
                            }
                            self.apply_button_styles(button_styles)
                        elif float(self.dienap_low) <= float(self.voltage_dc2) <= float(self.dienap_low1):
                            common_style = "background-color: rgb(255, 255, 0);"
                            bit_dc2_a70 = 1
                            bit_coi=1
                            button_styles = {
                                self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_12: "background-color: rgb(255, 0, 0);  border-radius: 15px;",
                                self.ui.pushButton_canhbao: "background-color: rgb(255, 0, 0); border-radius: 17px;", 
                                self.ui.pushButton_186: "background-color: rgb(255, 0, 0);", 
                            
                            }
                            self.apply_button_styles(button_styles)
                            
                        else:
                            common_style = "background-color: rgb(255, 0, 0);"
                            bit_dc2_a70 = 1
                            bit_coi=1
                            button_styles = {
                                self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                                self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                self.ui.pushButton_186: common_style ,
                            
                            }
                            self.apply_button_styles(button_styles)
                        if bit_coi == 1:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(255,0,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                        
                                    }
                                    self.apply_button_styles(button_styles)
                        else:
                                if client_address == tram70:
                                    common_style ="background-color:rgb(0,170,0);"
                                    button_styles = {
                                        self.ui.pushButton_186: common_style ,
                                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                                    }
                                    # Apply styles to buttons
                                    for button, style in button_styles.items():
                                        button.setStyleSheet(style)

            if temperature is not None and temperature != 0:
                self.ui.label_nhietdo_5.setText(f" Nhiệt độ: {temperature}°C")
                if temperature is not None:
                    self.temperature = temperature
                if nhietdo_lower is not None and nhietdo_lower != 0:
                    self.nhietdo_lower = nhietdo_lower
                if nhietdo_high is not None and nhietdo_high != 0:
                    self.nhietdo_high = nhietdo_high
                # Kiểm tra nhiệt độ so với ngưỡng và cập nhật màu nút
                common_style = ""
                if self.nhietdo_lower is not None and self.nhietdo_high is not None:
                    if float(self.nhietdo_lower) <= float(self.temperature) <= float(self.nhietdo_high):
                        common_style = "background-color: rgb(0, 170, 0);"
                        bit_temp_a70 = 0
                    else:
                        common_style = "background-color: rgb(255, 0, 0);"
                        bit_temp_a70 = 1
                        bit_coi = 1
                    # Áp dụng màu nút
                    button_styles = {
                        self.ui.pushButton_nhietdo: common_style + " border-radius: 17px;",
                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                        self.ui.pushButton_186: common_style ,
                    }
                    self.apply_button_styles(button_styles)
            if humidity is not None and humidity != 0:
                self.ui.label_doam_2.setText(f" Độ ẩm: {humidity}%")
                if humidity is not None:
                    self.humidity = humidity
                if doam_low is not None and doam_low != 0:
                    self.doam_low = doam_low
                if doam_high is not None and doam_high != 0:
                    self.doam_high = doam_high
                if self.doam_low is not None and self.doam_high is not None:    
                    if float(self.doam_low) <= float(self.humidity) <= float(self.doam_high):
                        common_style = "background-color: rgb(0, 170, 0);"
                        bit_humi_a70 = 0
                       
                    else:
                        common_style = "background-color: rgb(255, 0, 0);"  # Màu đỏ
                        bit_humi_a70 = 1
                        bit_coi = 1

                    # Áp dụng màu nút
                    button_styles = {
                            self.ui.pushButton_doam: common_style + " border-radius: 17px;",
                            self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                            self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                            self.ui.pushButton_186: common_style ,
                        }
                    self.apply_button_styles(button_styles)  
            if voltage_dc1 is not None and voltage_dc1 !=0:
                self.ui.label_dc1.setText(f" DC1: {voltage_dc1}V")
                if voltage_dc1 is not None:
                    self.voltage_dc1 = voltage_dc1
                if dienap_low1 is not None and dienap_low1 != 0:
                    self.dienap_low1 = dienap_low1
                if dienap_low is not None and dienap_low != 0:
                    self.dienap_low = dienap_low
                if dienap_high is not None and dienap_high != 0:
                    self.dienap_high = dienap_high
                if self.dienap_low1 is not None and self.dienap_low is not None and self.dienap_high is not None:
                    if float(self.dienap_low1) < float(self.voltage_dc1) <= float(self.dienap_high):
                        common_style = "background-color: rgb(0, 170, 0);"
                        bit_dc1_a70 = 0
                        
                    elif float(self.dienap_low) <= float(self.voltage_dc1) <= float(self.dienap_low1):
                        common_style = "background-color: rgb(255, 255, 0);"
                        bit_dc1_a70 = 1
                        bit_coi=1
                        
                    else:
                        common_style = "background-color: rgb(255, 0, 0);"
                        bit_dc1_a70 = 1
                        bit_coi=1
                    button_styles = {
                            self.ui.pushButton_dc1: common_style + " border-radius: 17px;",
                            
                        }
                    self.apply_button_styles(button_styles)
            if voltage_dc2 is not None and voltage_dc2 !=0:
                self.ui.label_dc2.setText(f" DC2: {voltage_dc2}V")
                if voltage_dc2 is not None:
                    self.voltage_dc2 = voltage_dc2
                if dienap_low1 is not None and dienap_low1 != 0:
                    self.dienap_low1 = dienap_low1
                if dienap_low is not None and dienap_low != 0:
                    self.dienap_low = dienap_low
                if dienap_high is not None and dienap_high != 0:
                    self.dienap_high = dienap_high
                if self.dienap_low1 is not None and self.dienap_low is not None and self.dienap_high is not None:
                    if float(self.dienap_low1) < float(self.voltage_dc2) <= float(self.dienap_high):
                        common_style = "background-color: rgb(0, 170, 0);"
                        bit_dc2_a70 = 0
                        
                    elif float(self.dienap_low) <= float(self.voltage_dc2) <= float(self.dienap_low1):
                        common_style = "background-color: rgb(255, 255, 0);"
                        bit_dc2_a70 = 1
                        bit_coi=1
                        
                    else:
                        common_style = "background-color: rgb(255, 0, 0);"
                        bit_dc2_a70 = 1
                        bit_coi=1
                    button_styles = {
                            self.ui.pushButton_dc2: common_style + " border-radius: 17px;",
                            
                        }
                    self.apply_button_styles(button_styles)
            if voltage_ac is not None and voltage_ac != 0:
                if voltage_ac == 1:
                    common_style = "background-color: rgb(255, 0, 0);"
                    bit_ac1_a70=1
                    bit_coi=1
                elif voltage_ac == 220:
                    bit_ac1_a70=0
                    common_style = "background-color: rgb(0, 170, 0);"
                button_styles = {
                        self.ui.pushButton_ac1: common_style + " border-radius: 17px;",
                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                    }
                self.apply_button_styles(button_styles)
            if voltage_ac2 is not None and voltage_ac2 != 0 :
                if voltage_ac2 == 1:
                    common_style = "background-color: rgb(255, 0, 0);"
                    bit_ac2_a70=1
                    bit_coi=1
                elif voltage_ac2 == 220:
                    common_style = "background-color: rgb(0, 170, 0);"
                    bit_ac2_a70=0
                  
                button_styles = {
                        self.ui.pushButton_ac2: common_style + " border-radius: 17px;",
                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                    }
                self.apply_button_styles(button_styles)
            if light is not None and light != 0:
                if light == 1:
                    self.ui.label_anhsang.setText("Ánh sáng: Bật")
                    common_style = "background-color: rgb(0, 170, 0);"
                    bit_light_70=0
                elif light == 2:
                    self.ui.label_anhsang.setText("Ánh sáng: Tắt")
                    common_style = "background-color: rgb(255, 0, 0);"
                    bit_coi=1
                    bit_light_70=1  
                button_styles = {
                        self.ui.pushButton_anhsang: common_style + " border-radius: 17px;",
                        self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                        self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                    }
                self.apply_button_styles(button_styles)
        
            if ( bit_light_70 ==1 or bit_humi_a70 == 1 or bit_temp_a70 == 1 or bit_ac1_a70 == 1 or bit_ac2_a70 == 1 or bit_dc1_a70 == 1 or bit_dc2_a70 == 1 ):
                bit_coi = 1
            else:
               bit_coi = 0
            
            if bit_coi == 1:
                    if client_address == tram70:
                        common_style ="background-color:rgb(255,0,0);"
                        button_styles = {
                            self.ui.pushButton_186: common_style ,
                            self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                            self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                        }
                        self.apply_button_styles(button_styles)
            
            else:
                    if client_address == tram70:
                        common_style ="background-color:rgb(0,170,0);"
                        button_styles = {
                            self.ui.pushButton_186: common_style ,
                            self.ui.pushButton_canhbao: common_style + " border-radius: 17px;",
                            self.ui.pushButton_anhsang_12: common_style + " border-radius: 15px;",
                        }
                        # Apply styles to buttons
                        for button, style in button_styles.items():
                            button.setStyleSheet(style)
                     
  
    def show_problem_dock(self):
        self.problem_dialog = QDialog(self)
        self.problem_dialog.setWindowTitle("Sự cố")
        # Setup the Problem UI in the dialog
        self.problem = Problem()
        self.problem.setupUi(self.problem_dialog)
        self.problem.switch_to_suco_signal.connect(self.switch_to_suco_widget)
        # self.problem.selected_date_range_signal.connect(self.show_custom_data)
        # self.problem.pushButton.clicked.connect(self.show_custom_data)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_hum)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_temp)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_ac1)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_ac2)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_dc1)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_dc2)
        self.problem_dialog.exec()
    def show_problem_dock2(self):
        self.problem_dialog_2 = QDialog(self)
        self.problem_dialog_2.setWindowTitle("Sự cố")
        # Setup the Problem UI in the dialog
        self.problem = Problem()
        self.problem.setupUi(self.problem_dialog_2)
        self.problem.switch_to_suco_signal.connect(self.switch_to_suco_widget2)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_hum2)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_temp2)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_ac1_2)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_ac2_2)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_dc1_2)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_dc2_2)
        self.problem_dialog_2.exec()
    def switch_to_suco_widget2(self):
        if self.problem_dialog_2 is not None:
            self.problem_dialog_2.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.suco_2)
    def show_problem_dock01(self):
        self.problem_dialog_01 = QDialog(self)
        self.problem_dialog_01.setWindowTitle("Sự cố")
        # Setup the Problem UI in the dialog
        self.problem = Problem()
        self.problem.setupUi(self.problem_dialog_01)
        self.problem.switch_to_suco_signal.connect(self.switch_to_suco_widget_01)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_temp_tram01)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_hum_tram01)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_ac1_tram01)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_ac2_tram01)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_dc1_tram01)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_dc2_tram01)
        self.problem_dialog_01.exec()
   
    def show_problem_dock_48(self):
        self.problem_dialog_48 = QDialog(self)
        self.problem_dialog_48.setWindowTitle("Sự cố")
        # Setup the Problem UI in the dialog
        self.problem = Problem()
        self.problem.setupUi(self.problem_dialog_48)
        self.problem.switch_to_suco_signal.connect(self.switch_to_suco_widget_48)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_temp_tram48)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_hum_tram48)
        self.problem_dialog_48.exec()
    def switch_to_suco_widget_48(self):
        if self.problem_dialog_48 is not None:
            self.problem_dialog_48.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.suco_4)
    def show_problem_dock_71(self):
        self.problem_dialog_71 = QDialog(self)
        self.problem_dialog_71.setWindowTitle("Sự cố")
        # Setup the Problem UI in the dialog
        self.problem = Problem()
        self.problem.setupUi(self.problem_dialog_71)
        self.problem.switch_to_suco_signal.connect(self.switch_to_suco_widget_71)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_temp_tram71)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_hum_tram71)
        self.problem_dialog_71.exec()
    def switch_to_suco_widget_71(self):
        if self.problem_dialog_71 is not None:
            self.problem_dialog_71.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.suco_5)
    def show_problem_dock_76(self):
        self.problem_dialog_76 = QDialog(self)
        self.problem_dialog_76.setWindowTitle("Sự cố")
        # Setup the Problem UI in the dialog
        self.problem = Problem()
        self.problem.setupUi(self.problem_dialog_76)
        self.problem.switch_to_suco_signal.connect(self.switch_to_suco_widget_76)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_temp_tram76)
        self.problem.pushButton.clicked.connect(self.fecth_and_popula_data_hum_tram76)
        
        self.problem_dialog_76.exec()
    def switch_to_suco_widget_76(self):
        if self.problem_dialog_76 is not None:
            self.problem_dialog_76.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.suco_5)
    def switch_to_suco_widget(self):
        if self.problem_dialog is not None:
            self.problem_dialog.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.suco)
    def switch_to_suco_widget_01(self):
        if self.problem_dialog_01 is not None:
            self.problem_dialog_01.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.suco_3)
   
    def switch_to_suco_widget2(self):
        if self.problem_dialog_2 is not None:
            self.problem_dialog_2.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.suco)
    def switch_to_suco_widget(self):
        if self.problem_dialog is not None:
            self.problem_dialog.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.suco_2)
    #------------------------ Tram70----------------------------------------
     
    def fecth_and_popula_data_temp(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="suconhietdo_tram70"
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
        self.ui.tableWidget_nhietdo_3.clearContents()
        self.ui.tableWidget_nhietdo_3.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None
        global bit_temp_a70,bit_coi
        for row_idx, (time, temperature, nhietdo_lower, nhietdo_high ) in enumerate(data):
            if time is None or temperature is None or nhietdo_lower is None or nhietdo_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            if float(nhietdo_lower) <= float(temperature) <= float(nhietdo_high):
                alert_type = None
               
            elif float(temperature) < float(nhietdo_lower):
                alert_type = f"Sự cố nhiệt độ thấp {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"
          
            elif float(temperature) > float(nhietdo_high):
                alert_type = f"Sự cố nhiệt độ cao {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"

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
                        next_alert_type = f"Sự cố nhiệt độ thấp {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"
                    elif float(next_temp) > float(next_high):
                        next_alert_type = f"Sự cố nhiệt độ cao {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"

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
                        next_alert_type = f"Sự cố nhiệt độ thấp {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"
                    elif float(next_temp) > float(next_high):
                        next_alert_type = f"Sự cố nhiệt độ cao {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"
                    
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
    def fecth_and_popula_data_hum(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodoam_tram70"
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
        self.ui.tableWidget_doam_3.clearContents()
        self.ui.tableWidget_doam_3.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, humidity, doam_low, doam_high ) in enumerate(data):
            if time is None or humidity is None or doam_low is None or doam_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")

            if doam_low is not None and doam_low != 0:
                self.doam_low_tram45 = doam_low       
            if doam_high is not None and doam_high != 0:
                self.doam_high_tram45 = doam_high
            print( self.doam_low_tram45,self.doam_high_tram45)
            if float(doam_low) <= float(humidity) <= float(doam_high):
                alert_type = None
            elif float(humidity) < float(doam_low):
                alert_type = f"Sự cố độ ẩm thấp {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
            elif float(humidity) > float(doam_high):
                alert_type = f"Sự cố độ ẩm cao {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
    
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

                    if float(next_lower) <= float(next_temp) <= float(next_high):
                        next_alert_type = None
                    elif float(next_temp) < float(next_lower):
                        next_alert_type = f"Sự cố độ ẩm thấp {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
                    elif float(next_temp) > float(next_high):
                        next_alert_type = f"Sự cố độ ẩm cao {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "

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
                        next_alert_type = f"Sự cố độ ẩm thấp {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
                    elif float(next_temp) > float(next_high):
                        next_alert_type = f"Sự cố độ ẩm cao {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
                    # if next_alert_type is not None:
                    #     next_data_time = next_time

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
    def fecth_and_popula_data_ac1(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucoac1_tram70"
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
        self.ui.tableWidget_ac1_2.clearContents()
        self.ui.tableWidget_ac1_2.setRowCount(0)
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

                    if float(next_voltage_ac) == float(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif float(next_voltage_ac) == float(next_voltage_ac_high):
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if float(next_voltage_ac) == float(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif float(next_voltage_ac) == float(next_voltage_ac_high):
                        next_alert_type = None
                  

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
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_ac1_2.rowCount()
                        self.ui.tableWidget_ac1_2.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_ac1_2.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_ac1_2.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_ac1_2.setItem(row_position, 2, item_next_data_time)  
    def fecth_and_popula_data_ac2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucoac2_tram70"
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
        self.ui.tableWidget_ac2_2.clearContents()
        self.ui.tableWidget_ac2_2.setRowCount(0)
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

                    if float(next_voltage_ac) == float(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC2 mất"
                    elif float(next_voltage_ac) == float(next_voltage_ac_high):
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if float(next_voltage_ac) == float(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC2 mất"
                    elif float(next_voltage_ac) == float(next_voltage_ac_high):
                        next_alert_type = None
                  

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
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_ac2_2.rowCount()
                        self.ui.tableWidget_ac2_2.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_ac2_2.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_ac2_2.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_ac2_2.setItem(row_position, 2, item_next_data_time)  
    def fecth_and_popula_data_dc1(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodc1_tram70"
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
        self.ui.tableWidget_dc1_3.clearContents()
        self.ui.tableWidget_dc1_3.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, voltage_dc1, dienap_low,dienap_low1, dienap_high ) in enumerate(data):
            if time is None or voltage_dc1 is None or dienap_low is None or dienap_low1 is None or dienap_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            print(dienap_low,dienap_low1,dienap_high)
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high
            if float(dienap_low) <= float(voltage_dc1) <= float(dienap_low1):
                alert_type =f"Sự cố điện áp DC1 mức 1 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
            elif float(voltage_dc1) < float(dienap_low):
                alert_type = f"Sự cố điện áp DC1 mức 2 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
            elif float(voltage_dc1) > float(dienap_high):
                alert_type = f"Sự cố điện áp DC1 mức cao {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
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
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) <= float(next_dienap_low1):
                        next_alert_type = f"Sự cố điện áp DC1 mức 1 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = f"Sự cố điện áp DC1 mức 2 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = f"Sự cố điện áp DC1 mức cao {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    else:
                        next_alert_type = None

                    if  next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) <= float(next_dienap_low1):
                        next_alert_type = f"Sự cố điện áp DC1 mức 1 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = f"Sự cố điện áp DC1 mức 2 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = f"Sự cố điện áp DC1 mức cao {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    

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
    def fecth_and_popula_data_dc2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodc2_tram70"
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
        self.ui.tableWidget_dc2_3.clearContents()
        self.ui.tableWidget_dc2_3.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, voltage_dc2, dienap_low,dienap_low1, dienap_high ) in enumerate(data):
            if time is None or voltage_dc2 is None or dienap_low is None or dienap_low1 is None or dienap_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high
            if float(dienap_low) <= float(voltage_dc2) <= float(dienap_low1):
                alert_type = f"Sự cố điện áp DC2 mức 1 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
            elif float(voltage_dc2) < float(dienap_low):
                alert_type = f"Sự cố điện áp DC2 mức 2 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
            elif float(voltage_dc2) > float(dienap_high):
                alert_type = f"Sự cố điện áp DC2 mức cao {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
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

                    if float(next_dienap_low) <= float(next_voltage_dc2) <= float(next_dienap_low1):
                        next_alert_type = f"Sự cố điện áp DC2 mức 1 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type =  f"Sự cố điện áp DC2 mức 2 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type =  f"Sự cố điện áp DC2 mức cao {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    else:
                        next_alert_type = None

                    if  next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) <= float(next_dienap_low1):
                        next_alert_type = f"Sự cố điện áp DC2 mức 1 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type =  f"Sự cố điện áp DC2 mức 2 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type =  f"Sự cố điện áp DC2 mức cao {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    

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
    def export_to_exceltemp(self):
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
    def export_to_excelhum(self):
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
    def export_to_exceldc1(self):
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
    def export_to_exceldc2(self):
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
    def export_to_excelac1(self):
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
    def export_to_excelac2(self):
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
            print("Xuất dữ liệu ra file Excel thành công.")

    #-----------------------Tram45-----------------------------------------
    def fecth_and_popula_data_temp2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="suconhietdo_tram45"
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

            if float(nhietdo_lower) <= float(temperature) <= float(nhietdo_high):
                alert_type = None
               
            elif float(temperature) < float(nhietdo_lower):
                alert_type = f"Sự cố nhiệt độ thấp {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"
          
            elif float(temperature) > float(nhietdo_high):
                alert_type = f"Sự cố nhiệt độ cao {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"

    
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
                        next_alert_type = f"Sự cố nhiệt độ thấp {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"
                    elif float(next_temp) > float(next_high):
                        next_alert_type = f"Sự cố nhiệt độ cao {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"

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
                        next_alert_type = f"Sự cố nhiệt độ thấp {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"
                    elif float(next_temp) > float(next_high):
                        next_alert_type = f"Sự cố nhiệt độ cao {temperature}°C \n Ngưỡng: {nhietdo_lower} - {nhietdo_high}"
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
    def fecth_and_popula_data_hum2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodoam_tram45"
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
        self.ui.tableWidget_doam_2.clearContents()
        self.ui.tableWidget_doam_2.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, humidity, doam_low, doam_high ) in enumerate(data):
            if time is None or humidity is None or doam_low is None or doam_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")

            if doam_low is not None and doam_low != 0:
                self.doam_low_tram45 = doam_low       
            if doam_high is not None and doam_high != 0:
                self.doam_high_tram45 = doam_high
            print( self.doam_low_tram45,self.doam_high_tram45)
            if float(doam_low) <= float(humidity) <= float(doam_high):
                alert_type = None
            elif float(humidity) < float(doam_low):
                alert_type = f"Sự cố độ ẩm thấp {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
            elif float(humidity) > float(doam_high):
                alert_type = f"Sự cố độ ẩm cao {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
    
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

                    if float(next_lower) <= float(next_temp) <= float(next_high):
                        next_alert_type = None
                    elif float(next_temp) < float(next_lower):
                        next_alert_type = f"Sự cố độ ẩm thấp {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
                    elif float(next_temp) > float(next_high):
                        next_alert_type = f"Sự cố độ ẩm cao {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "

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
                        next_alert_type = f"Sự cố độ ẩm thấp {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
                    elif float(next_temp) > float(next_high):
                        next_alert_type = f"Sự cố độ ẩm cao {float(humidity)}°C\nNgưỡng: {float(doam_low)} - {float(doam_high)} "
                    # if next_alert_type is not None:
                    #     next_data_time = next_time

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
    def fecth_and_popula_data_ac1_2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucoac1_tram45"
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
        self.ui.tableWidget_ac1.clearContents()
        self.ui.tableWidget_ac1.setRowCount(0)
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

                    if float(next_voltage_ac) == float(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif float(next_voltage_ac) == float(next_voltage_ac_high):
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if float(next_voltage_ac) == float(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC1 mất"
                    elif float(next_voltage_ac) == float(next_voltage_ac_high):
                        next_alert_type = None
                  

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
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_ac1.rowCount()
                        self.ui.tableWidget_ac1.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_ac1.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_ac1.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_ac1.setItem(row_position, 2, item_next_data_time)  
    def fecth_and_popula_data_ac2_2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucoac2_tram45"
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
        self.ui.tableWidget_ac2.clearContents()
        self.ui.tableWidget_ac2.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None
        
        for row_idx, (time, voltage_ac, dienapac_low, dienapac_high) in enumerate(data):
            if time is None or voltage_ac is None or dienapac_low is None or dienapac_high is None:
                continue
            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            
            if float(voltage_ac) == float(dienapac_low):
                alert_type = "Sự cố AC2 mất"
            elif float(voltage_ac) == float(dienapac_high):
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

                    if float(next_voltage_ac) == float(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC2 mất"
                    elif float(next_voltage_ac) == float(next_voltage_ac_high):
                        next_alert_type = None

                    if next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_ac, next_voltage_ac_low, next_voltage_ac_high = next_row

                    if float(next_voltage_ac) == float(next_voltage_ac_low):
                        next_alert_type = "Sự cố AC2 mất"
                    elif float(next_voltage_ac) == float(next_voltage_ac_high):
                        next_alert_type = None
                  

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
            if next_data_time is None and alert_type is None:
                    if previous_alert_type is None:
                        row_position = self.ui.tableWidget_ac2.rowCount()
                        self.ui.tableWidget_ac2.insertRow(row_position)

                        item_alert_type = QTableWidgetItem()
                        item_alert_time = QTableWidgetItem()
                        item_next_data_time = QTableWidgetItem(time_str)

                        item_alert_type.setForeground(QColor(0, 0, 0))  
                        item_alert_time.setForeground(QColor(0, 0, 0))
                        item_next_data_time.setForeground(QColor(0, 0, 0))
                        self.ui.tableWidget_ac2.setItem(row_position, 0, item_alert_type)
                        self.ui.tableWidget_ac2.setItem(row_position, 1, item_alert_time)
                        self.ui.tableWidget_ac2.setItem(row_position, 2, item_next_data_time)  
    def fecth_and_popula_data_dc1_2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodc1_tram45"
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
        self.ui.tableWidget_dc1_2.clearContents()
        self.ui.tableWidget_dc1_2.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, voltage_dc1, dienap_low,dienap_low1, dienap_high ) in enumerate(data):
            if time is None or voltage_dc1 is None or dienap_low is None or dienap_low1 is None or dienap_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            print(dienap_low,dienap_low1,dienap_high)
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high
            if float(dienap_low) <= float(voltage_dc1) <= float(dienap_low1):
                alert_type =  f"Sự cố điện áp DC1 mức 1 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
            elif float(voltage_dc1) < float(dienap_low):
                alert_type = f"Sự cố điện áp DC1 mức 2 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
            elif float(voltage_dc1) > float(dienap_high):
                alert_type = f"Sự cố điện áp DC1 mức cao {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
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
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) <= float(next_dienap_low1):
                        next_alert_type = f"Sự cố điện áp DC1 mức 1 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = f"Sự cố điện áp DC1 mức 2 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = f"Sự cố điện áp DC1 mức cao {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    else:
                        next_alert_type = None

                    if  next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) <= float(next_dienap_low1):
                        next_alert_type = f"Sự cố điện áp DC1 mức 1 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = f"Sự cố điện áp DC1 mức 2 {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = f"Sự cố điện áp DC1 mức cao {float(voltage_dc1)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    

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
    def fecth_and_popula_data_dc2_2(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="sucodc2_tram45"
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
        self.ui.tableWidget_dc2_2.clearContents()
        self.ui.tableWidget_dc2_2.setRowCount(0)
        previous_alert_type = None
        previous_alert_time = None
        next_data_time = None

        for row_idx, (time, voltage_dc2, dienap_low,dienap_low1, dienap_high ) in enumerate(data):
            if time is None or voltage_dc2 is None or dienap_low is None or dienap_low1 is None or dienap_high is None:
                continue

            time_str = time.strftime("%Y-%m-%d %H:%M:%S")
            print(dienap_low,dienap_low1,dienap_high)
            if dienap_low is not None and dienap_low != 0:
                self.dienap_low = dienap_low
            if dienap_low1 is not None and dienap_low1 != 0:
                self.dienap_low1 = dienap_low1
            if dienap_high is not None and dienap_high != 0:
                self.dienap_high = dienap_high
            if float(dienap_low) <= float(voltage_dc2) <= float(dienap_low1):
                alert_type = f"Sự cố điện áp DC2 mức 1 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
            elif float(voltage_dc2) < float(dienap_low):
                alert_type = f"Sự cố điện áp DC2 mức 2 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
            elif float(voltage_dc2) > float(dienap_high):
                alert_type = f"Sự cố điện áp DC2 mức cao {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
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

                    if float(next_dienap_low) <= float(next_voltage_dc2) <= float(next_dienap_low1):
                        next_alert_type = f"Sự cố điện áp DC2 mức 1 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = f"Sự cố điện áp DC2 mức 2 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = f"Sự cố điện áp DC2 mức cao {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    else:
                        next_alert_type = None

                    if  next_alert_type != alert_type:
                        next_alert_row_idx = next_idx
                        next_data_time = next_time
                        break

                if next_alert_row_idx is None and row_idx < len(data) - 1:
                    next_row = data[row_idx + 1]
                    next_time, next_voltage_dc2, next_dienap_low, next_dienap_low1, next_dienap_high = next_row

                    if float(next_dienap_low) <= float(next_voltage_dc2) <= float(next_dienap_low1):
                        next_alert_type = f"Sự cố điện áp DC2 mức 1 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) < float(next_dienap_low):
                        next_alert_type = f"Sự cố điện áp DC2 mức 2 {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    elif float(next_voltage_dc2) > float(next_dienap_high):
                        next_alert_type = f"Sự cố điện áp DC2 mức cao {float(voltage_dc2)}°C\nNgưỡng: {float(dienap_low)} - {float(dienap_low1)} - {float(dienap_high)} "
                    

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
    def export_to_exceltemp_2(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Xuất Dữ Liệu Ra Excel", "", "Excel Files (*.xlsx)")
        if file_path:
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
            df = pd.DataFrame(data, columns=["Tên Sự Cố", "Thời Gian Bắt Đầu", "Thời Gian Kết thúc"])
            df.to_excel(file_path, index=False)
            print("Xuất dữ liệu ra file Excel thành công.") 
    def export_to_excelhum_2(self):
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
    def export_to_exceldc1_2(self):
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
    def export_to_exceldc2_2(self):
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
    def export_to_excelac1_2(self):
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
    def export_to_excelac2_2(self):
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
 
    
class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login_attempt)
        self.ui.lineEdit_2.setEchoMode(QLineEdit.Password)  
        self.ui.pushButton_3.clicked.connect(self.show_connect_mysql_dock)
        self.ui.pushButton_2.clicked.connect(self.show_singin_dock)
    def show_singin_dock(self):
        self.singin_dialog = QDialog(self)
        self.singin_dialog.setWindowTitle("Singin Accounts")
        self.singin_dock = Ui_Form_Singin()
        self.singin_dock.setupUi(self.singin_dialog)
        self.singin_dock.pushButton.clicked.connect(self.singin_accouts)
        self.singin_dialog.exec()
    def show_connect_mysql_dock(self):
        self.mysql_dialog = QDialog(self)
        self.mysql_dialog.setWindowTitle("Connect MySQL")
        self.connect_mysql_ui = Connect_MySql()
        self.connect_mysql_ui.setupUi(self.mysql_dialog)
        self.connect_mysql_ui.pushButton_ketnoi_mySql.clicked.connect(self.create_mysql_table)
        self.mysql_dialog.exec()
    def singin_accouts(self):
        try:
            # Lấy dữ liệu từ các QLineEdit
            name_val = self.singin_dock.lineEdit.text()
            username_val = self.singin_dock.lineEdit_2.text()
            password_val = self.singin_dock.lineEdit_3.text()
            mabaomat_val = self.singin_dock.lineEdit_5.text()

            # Kiểm tra xem mã bảo mật có đúng không
            if mabaomat_val == "123456":  # Thay YOUR_SECRET_CODE bằng mã bảo mật thực tế của bạn
                # Kết nối với cơ sở dữ liệu và thêm dữ liệu vào bảng
                with mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="123456789",
                        database="login"
                ) as connection:
                    cursor = connection.cursor()
                    
                    insert_query = """
                        INSERT INTO new_table (name, username, password, mabaomat_val)
                        VALUES (%s, %s, %s, %s)
                    """
                    data = (name_val, username_val, password_val, mabaomat_val)
                    cursor.execute(insert_query, data)

                    connection.commit()
                    print("Dữ liệu đã được thêm thành công vào MySQL")
                    # Hiển thị thông báo khi đăng ký thành công
                    QMessageBox.information(self, "Thành Công", "Đăng Kí Tài Khoản Thành Công")
                    
                    # Đóng cửa sổ
                    self.singin_dialog.accept()
            else:
                # Hiển thị thông báo khi mã bảo mật không đúng
                QMessageBox.warning(self, "Cảnh Báo", "Mã Bảo Mật Không Đúng")

        except mysql.connector.Error as error:
            print("Lỗi khi thêm dữ liệu vào MySQL:", error)
            # Thông báo cho người dùng về lỗi
            QMessageBox.critical(self, "Error", f"Error occurred: {error}")
            
            # Gọi hàm để prompt retry
            self.prompt_retry()

        # Đóng kết nối với cơ sở dữ liệu
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def prompt_retry(self):
        reply = QMessageBox.question(self, "Retry?", "Would you like to retry?", QMessageBox.StandardButton.Retry | QMessageBox.StandardButton.Cancel)
        if reply == QMessageBox.StandardButton.Retry:
            # Retry logic here
            print("Retrying...")
        else:
            # Close the application if Cancel is clicked
            # Hoặc thực hiện hành động khác khi người dùng cancel
            sys.exit()
    def create_mysql_table(self):
        try:
            host = self.connect_mysql_ui.lineEdit.text()
            user = self.connect_mysql_ui.lineEdit_2.text()
            password = self.connect_mysql_ui.lineEdit_3.text()
            
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
            host = host
            user = user
            password = password
            cursor = connection.cursor()
            # Kiểm tra xem cơ sở dữ liệu đã tồn tại hay chưa
                
            required_databases = [
                "suconhietdo_tram70","sucodoam_tram70","sucodc1_tram70","sucodc2_tram70",
                "sucoac1_tram70","sucoac2_tram70","suconhietdo_tram45","sucodoam_tram45",
                "sucodc1_tram45","sucodc2_tram45","sucoac1_tram45","sucoac2_tram45",
                "suconhietdo_tram01","sucodoam_tram01","sucodc1_tram01","sucodc2_tram01",
                "sucoac1_tram01","sucoac2_tram01","suconhietdo_tram48","sucodoam_tram48",
                "sucodc1_tram48","sucodc2_tram48","sucoac1_tram48","sucoac2_tram48",
                "suconhietdo_tram71","sucodoam_tram71","sucodc1_tram71","sucodc2_tram71",
                "sucoac1_tram71","sucoac2_tram71","suconhietdo_tram76","sucodoam_tram76",
                "sucodc1_tram76","sucodc2_tram76","sucoac1_tram76","sucoac2_tram76",
                "login"
            ]
            for database_name in required_databases:
                try:
                    # Kiểm tra xem cơ sở dữ liệu đã tồn tại hay chưa
                    cursor.execute("SHOW DATABASES")
                    databases = [row[0] for row in cursor.fetchall()]

                    if database_name not in databases:
                        # Tạo cơ sở dữ liệu mới nếu chưa tồn tại
                        cursor.execute(f"CREATE DATABASE {database_name}")
                      
                        print(f"Tạo cơ sở dữ liệu '{database_name}' thành công.")
                    else:
                        QMessageBox.critical(self, "Kết Nối MySQL", f"Cơ Sở Dữ Liệu Đã Tồn Tại")
                        print(f"Cơ sở dữ liệu '{database_name}' đã tồn tại.")
                        QMessageBox.close()
                    # Chuyển sang cơ sở dữ liệu đã chọn
                    cursor.execute(f"USE {database_name}")
                    # Kiểm tra xem các bảng đã tồn tại trong cơ sở dữ liệu này hay chưa
                    cursor.execute("SHOW TABLES")
                    existing_tables = [row[0] for row in cursor.fetchall()]
                    # Tạo bảng trong cơ sở dữ liệu đã chọn nếu chưa tồn tại
                    if database_name.endswith("suconhietdo_tram70") or database_name.endswith("suconhietdo_tram45")or database_name.endswith("suconhietdo_tram01")or database_name.endswith("suconhietdo_tram48") or database_name.endswith("suconhietdo_tram71")or database_name.endswith("suconhietdo_tram76"):
                        table_name = "new_table"
                        if table_name not in existing_tables:
                            create_table_query = """
                                CREATE TABLE new_table (
                                    client_address VARCHAR(45),
                                    temperature VARCHAR(45),
                                    nhietdo_lower VARCHAR(45),
                                    nhietdo_high VARCHAR(45),
                                    time DATETIME(6)
                                )
                            """
                            cursor.execute(create_table_query)
                            print(f"Tạo bảng trong cơ sở dữ liệu '{database_name}' thành công.")
                            print(f"")
                    elif database_name.endswith("sucoac1_tram70") or database_name.endswith("sucoac1_tram45")or database_name.endswith("sucoac1_tram01")or database_name.endswith("sucoac1_tram48") or database_name.endswith("sucoac1_tram71")or database_name.endswith("sucoac1_tram76"):
                        table_name = "new_table"
                        if table_name not in existing_tables:
                            create_table_query = """
                                CREATE TABLE new_table (
                                    client_address VARCHAR(45),
                                    voltage_ac1 VARCHAR(45),
                                    dienapac_low VARCHAR(45),
                                    dienapac_high VARCHAR(45),
                                    time DATETIME(6)
                                )
                            """
                            cursor.execute(create_table_query)
                            print(f"Tạo bảng trong cơ sở dữ liệu '{database_name}' thành công.")

                    elif database_name.endswith("sucoac2_tram70") or database_name.endswith("sucoac2_tram45")or database_name.endswith("sucoac2_tram01")or database_name.endswith("sucoac2_tram48") or database_name.endswith("sucoac2_tram71")or database_name.endswith("sucoac2_tram76"):
                        table_name = "new_table"
                        if table_name not in existing_tables:
                            create_table_query = """
                                CREATE TABLE new_table (
                                    client_address VARCHAR(45),
                                    voltage_ac2 VARCHAR(45),
                                    dienapac_low VARCHAR(45),
                                    dienapac_high VARCHAR(45),
                                    time DATETIME(6)
                                )
                            """
                            cursor.execute(create_table_query)
                            print(f"Tạo bảng trong cơ sở dữ liệu '{database_name}' thành công.")

                    elif database_name.endswith("sucodoam_tram70") or database_name.endswith("sucodoam_tram45")or database_name.endswith("sucodoam_tram01")or database_name.endswith("sucodoam_tram48") or database_name.endswith("sucodoam_tram71")or database_name.endswith("sucodoam_tram76"):
                        table_name = "new_table"
                        if table_name not in existing_tables:
                            create_table_query = """
                                CREATE TABLE new_table (
                                    client_address VARCHAR(45),
                                    humidity VARCHAR(45),
                                    doam_low VARCHAR(45),
                                    doam_high VARCHAR(45),
                                    time DATETIME(6)
                                )
                            """
                            cursor.execute(create_table_query)
                            print(f"Tạo bảng trong cơ sở dữ liệu '{database_name}' thành công.")

                    elif database_name.endswith("sucodc1_tram70") or database_name.endswith("sucodc1_tram45")or database_name.endswith("sucodc1_tram01")or database_name.endswith("sucodc1_tram48") or database_name.endswith("sucodc1_tram71")or database_name.endswith("sucodc1_tram76"):
                        table_name = "new_table"
                        if table_name not in existing_tables:
                            create_table_query = """
                                CREATE TABLE new_table (
                                    client_address VARCHAR(45),
                                    voltage_dc1 VARCHAR(45),
                                    dienap_low VARCHAR(45),
                                    dienap_low1 VARCHAR(45),
                                    dienap_high VARCHAR(45),
                                    time DATETIME(6)
                                )
                            """
                            cursor.execute(create_table_query)
                            print(f"Tạo bảng trong cơ sở dữ liệu '{database_name}' thành công.")

                    elif database_name.endswith("sucodc2_tram70") or database_name.endswith("sucodc2_tram45")or database_name.endswith("sucodc2_tram01")or database_name.endswith("sucodc2_tram48") or database_name.endswith("sucodc2_tram71")or database_name.endswith("sucodc2_tram76"):
                        table_name = "new_table"
                        if table_name not in existing_tables:
                            create_table_query = """
                                CREATE TABLE new_table (
                                    client_address VARCHAR(45),
                                    voltage_dc2 VARCHAR(45),
                                    dienap_low VARCHAR(45),
                                    dienap_low1 VARCHAR(45),
                                    dienap_high VARCHAR(45),
                                    time DATETIME(6)
                                )
                            """
                            cursor.execute(create_table_query)
                            print(f"Tạo bảng trong cơ sở dữ liệu '{database_name}' thành công.")
                    elif database_name.endswith("login") :
                        table_name = "new_table"
                        if table_name not in existing_tables :
                            create_table_query ="""
                             CREATE TABLE new_table (
                                    name VARCHAR(100),
                                    username VARCHAR(40),
                                    password VARCHAR(40),
                                    mabaomat_val VARCHAR(50)
                                )
                            """
                            try:
                                cursor.execute(create_table_query)
                                print(f"Tạo bảng trong cơ sở dữ liệu '{database_name}' thành công.")
                                
                                # Thêm các giá trị mặc định vào bảng
                                insert_query = """
                                    INSERT INTO new_table ( name, username, password, mabaomat_val)
                                    VALUES ( %s, %s, %s, %s)
                                """
                                default_data = [
                                    ( 'Tài Khoản Mặc Định', 'admin', '123456', '123456'),
                                  
                                ]
                                cursor.executemany(insert_query, default_data)
                                connection.commit()
                                print("Thêm dữ liệu mặc định thành công.")
                                QMessageBox.information(self, "Thành Công", "Kết Nối MySQL Thành Công")
                                self.mysql_dialog.accept()
                            except mysql.connector.Error as err:
                                print(f"Lỗi xảy ra: {err}")
                                QMessageBox.critical(self, "Error", f"Error occurred: {err}")
                            
                except mysql.connector.Error as err:
                    print(f"Lỗi xảy ra: {err}")
                    QMessageBox.critical(self, "Error", f"Error occurred: {err}")
                 

        except mysql.connector.Error as err:
            print(f"Lỗi xảy ra: {err}")
           
                          
            if "kết nối" in str(err):
                print(f"Lỗi xảy ra khi kết nối đến cơ sở dữ liệu: {err}")
                # Lưu thông tin kết nối vào LoginWindow
                self.mysql_host = host
                self.mysql_user = user
                self.mysql_password = password

                # Commit các thay đổi và đóng con trỏ và kết nối
                connection.commit()
                cursor.close()
                connection.close()

                
               
                # Quay trở lại màn hình cũ và đóng cửa sổ hiện tại
                self.show()
                  # Hiển thị thông báo khi đăng ký thành công
       
               
                self.mysql_dialog.close()
            else:
                # Hiển thị thông báo lỗi và yêu cầu người dùng thử lại
                QMessageBox.critical(self, "Error", f"Error occurred: {err}")
                
    
    def login_attempt(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        
        # Thực hiện kiểm tra thông tin đăng nhập với cơ sở dữ liệu
        if self.check_credentials(username, password):
            # Nếu đăng nhập thành công, chấp nhận dialog
            self.ui.lineEdit_2.setEchoMode(QLineEdit.Normal)
            self.ui.lineEdit_2.setText("*")
            self.accept()
        else:
            # Nếu mật khẩu không chính xác, hiển thị thông báo lỗi
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")
            self.reject()

    def check_credentials(self, username, password):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="login"
            )
            mycursor = mydb.cursor()
            
            # Thực hiện truy vấn để kiểm tra thông tin đăng nhập
            query = "SELECT * FROM new_table WHERE username = %s AND password = %s"
            mycursor.execute(query, (username, password))
            result = mycursor.fetchone()
            
            mycursor.close()
            mydb.close()
            
            # Nếu kết quả trả về không rỗng, thông tin đăng nhập hợp lệ
            return result is not None
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
   
class SoundThread(QThread):
    finished = Signal()

    def run(self):
        while self.sound_enabled:
            try:
                playsound('images\sound\Tieng-bip-bao-dong-www_tiengdong_com.mp3')
            except Exception as e:
                print(f"Error while playing sound: {e}")
        
        # Đảm bảo rằng chúng ta kết thúc khi dừng thread
        if self.playing_sound:
            self.playing_sound = False
            self.finished.emit()
 


def check_condition():
    # Thực hiện kiểm tra điều kiện ở đây
    
    global bit_canh_bao_a01,bit_canh_bao_a70,bit_canh_bao_a45,bit_humi_a70,bit_temp_a70,bit_ac1_a70,bit_ac2_a70,bit_dc1_a70,bit_dc2_a70,bit_humi_a45,bit_temp_a45,bit_ac1_a45,bit_ac2_a45,bit_dc1_a45,bit_dc2_a45,bit_humi_a01,bit_temp_a01,bit_ac1_a01,bit_ac2_a01,bit_dc1_a01,bit_dc2_a01,bit_humi_a48,bit_temp_a48,bit_ac1_a48,bit_ac2_a48,bit_dc1_a48,bit_dc2_a48,bit_humi_a01,bit_temp_a01,bit_ac1_a01,bit_ac2_a01,bit_dc1_a01,bit_dc2_a01,bit_humi_a71,bit_temp_a71,bit_ac1_a71,bit_ac2_a71,bit_dc1_a71,bit_dc2_a71,bit_humi_a76,bit_temp_a76,bit_ac1_a76,bit_ac2_a76,bit_dc1_a76,bit_dc2_a76,bit_canh_bao,bit_coi
    bit_canh_bao = bit_canh_bao_a01 or bit_canh_bao_a70 or bit_canh_bao_a45 or bit_humi_a70 or bit_temp_a70 or bit_ac1_a70 or bit_ac2_a70 or bit_dc1_a70 or bit_dc2_a70 or bit_humi_a45 or bit_temp_a45 or bit_ac1_a45 or bit_ac2_a45 or bit_dc1_a45 or bit_dc2_a45 or bit_humi_a01 or bit_temp_a01 or bit_ac1_a01 or bit_ac2_a01 or bit_dc1_a01 or bit_dc2_a01 or bit_humi_a48 or bit_temp_a48 or bit_ac1_a48 or bit_ac2_a48 or bit_dc1_a48 or bit_dc2_a48 or bit_humi_a01 or bit_temp_a01 or bit_ac1_a01 or bit_ac2_a01 or bit_dc1_a01 or bit_dc2_a01 or bit_humi_a71 or bit_temp_a71 or bit_ac1_a71 or bit_ac2_a71 or bit_dc1_a71 or bit_dc2_a71 or bit_humi_a76 or bit_temp_a76 or bit_ac1_a76 or bit_ac2_a76 or bit_dc1_a76 or bit_dc2_a76 

    if (bit_canh_bao and bit_coi):
        #playsound('images\sound\Tieng-bip-bao-dong-www_tiengdong_com.mp3')
        #thay bang ham khong bi loi
        pygame.mixer.music.play()
    else:
        #them ham tat am thanh vao day
        pygame.mixer.music.stop()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/images/images/icon-1.ico"))
    login_window = LoginWindow()
    if login_window.exec() == QDialog.Accepted:
        print("Login successful")
        timer = QTimer()
        timer.timeout.connect(check_condition)
        timer.start(1000)  
        window = MainWindow()
       
        window.show()
        sys.exit(app.exec())
        
    else:
        print("Login canceled")