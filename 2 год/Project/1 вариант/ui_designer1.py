from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import ui_designer2


class WidgetNumbSize(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('widgetNumbSize.ui', self)
        self.pushButton2.clicked.connect(self.runSize2)
        self.pushButton3.clicked.connect(self.runSize3)
        self.pushButton4.clicked.connect(self.runSize4)
        self.pushButtonOther.clicked.connect(self.runSizeOther)

    def runSize2(self):
        self.next_window = ui_designer2.WidgetGuess(num_len=2)
        self.next_window.show()
        self.hide()

    def runSize3(self):
        self.next_window = ui_designer2.WidgetGuess(num_len=3)
        self.next_window.show()
        self.hide()

    def runSize4(self):
        self.next_window = ui_designer2.WidgetGuess(num_len=4)
        self.next_window.show()
        self.hide()

    def runSizeOther(self):
        self.next_window = ui_designer2.WidgetGuess()
        self.next_window.show()
        self.hide()
