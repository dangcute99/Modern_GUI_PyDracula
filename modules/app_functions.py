
from server import *
from test import *

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(QMainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """
    
    def setup_toolbox(self):
        # Tạo một danh sách các widget cần ẩn
        widgets_to_hide = [ self.ui.widget_11,self.ui.widget_13,self.ui.widget_15,self.ui.widget_20,self.ui.widget_21,self.ui.widget_22]
        # Ẩn tất cả các widget trong danh sách
        for widget in widgets_to_hide:
            widget.hide()
    def show_widget(self, widget_to_show):
        # Kiểm tra nếu widget đang hiển thị giống với widget cần hiển thị
        if self.current_widget == widget_to_show:
            return

        # Ẩn widget đang hiển thị nếu có
        if self.current_widget:
            self.current_widget.hide()

        # Hiển thị widget mới và cập nhật biến current_widget
        widget_to_show.show()
        self.current_widget = widget_to_show
    def toggle_widget(self, widget_to_show):
        for widget in self.sub_widgets:
            if widget != widget_to_show:
                widget.hide()
                self.widget_states[widget] = False

        widget_to_show.setVisible(not self.widget_states[widget_to_show])
        self.widget_states[widget_to_show] = not self.widget_states[widget_to_show]
    def show_widget_11(self):
        self.toggle_widget(self.ui.widget_11)
    def show_widget_15(self):
        self.toggle_widget(self.ui.widget_15)
    def show_widget_13(self):
        self.toggle_widget(self.ui.widget_13)
    def show_widget_20(self):
        self.toggle_widget(self.ui.widget_20)
    def show_widget_21(self):
        self.toggle_widget(self.ui.widget_21)
    def show_widget_22(self):
        self.toggle_widget(self.ui.widget_22)    
    
        
       
      