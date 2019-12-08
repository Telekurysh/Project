from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import ui_designer1


class WidgetWinner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('widgetWinner.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.next_window = ui_designer1.WidgetNumbSize()
        self.next_window.show()
        self.hide()
