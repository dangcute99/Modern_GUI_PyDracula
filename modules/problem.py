from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from server import *
class Problem(QDialog):
    switch_to_suco_signal = Signal()
    switch_to_suco_signal1 = Signal()
    selected_date_range_signal = Signal(QDate, QDate) 
    def setupUi(self, dialog,):
        if not dialog.objectName():
            dialog.setObjectName(u"Problem")
        dialog.resize(400, 184)

        # Create the widgets for the dialog
        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 14pt \"Times New Roman\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Chọn ngày xem sảy ra sự cố")

        self.dateEdit = QDateEdit(dialog)
        self.dateEdit.setObjectName(u"dateEdit")

        self.dateEdit_2 = QDateEdit(dialog)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.pushButton = QPushButton(dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setText("Xem sự cố")

        # Create the layout for the dialog
        layout = QVBoxLayout(dialog)
        layout.addWidget(self.label)
        layout.addWidget(self.dateEdit)
        layout.addWidget(self.dateEdit_2)
        layout.addWidget(self.pushButton)

        # Connect the button click to a function (if needed)
        # self.pushButton.clicked.connect(self.some_function)
        self.pushButton.clicked.connect(self.on_push_button_clicked_and_switch)
      
    
        # Set the layout for the dialog
        dialog.setLayout(layout)
    def on_push_button_clicked_and_switch(self):
        select_start_date = self.dateEdit.date()
        select_end_date = self.dateEdit_2.date()
        self.selected_date_range_signal.emit(select_start_date, select_end_date)
        self.switch_to_suco_signal.emit()
        self.switch_to_suco_signal1.emit()
        self.accept()

   
     
