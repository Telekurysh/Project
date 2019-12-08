from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import ui_designer1
import sys

app = QApplication(sys.argv)
ex = ui_designer1.WidgetNumbSize()
ex.show()
sys.exit(app.exec_())
