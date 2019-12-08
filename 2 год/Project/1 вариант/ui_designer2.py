from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import randint
import ui_designer3


class WidgetGuess(QMainWindow):
    def __init__(self, num_len=randint(5, 10)):
        super().__init__()
        uic.loadUi('widgetGuess.ui', self)
        self.pushButton.clicked.connect(self.ok)
        self.lineEdit.textChanged[str].connect(self.set_value)
        self.value = []
        self.number = dict()
        self.num_len = num_len
        for i in range(num_len):
            char = randint(0, 9)
            while self.number.get(char) is not None:
                char = randint(0, 9)
            self.number[char] = i

    def set_value(self, text):
        self.info.setText('')
        self.value = list(map(int, list(text)))

    def countBC(self, input_number):
        countSameNumbers = 0
        rightPositions = 0
        n = 0
        # input_number - список цифр
        for i in range(self.num_len):
            n += 1
            if i == self.number.get(input_number[i]):
                rightPositions += 1
            if self.number.get(input_number[i]) is not None:
                countSameNumbers += 1
        # cows and bulls
        return countSameNumbers, rightPositions

    def check(self, input_number):
        if len(input_number) != self.num_len:
            return 'Length is wrong\nEnter new number'
        numbs = {x for x in input_number}
        if len(numbs) != self.num_len:
            return 'Wrong Number\nEnter new number'
        return 'OK'

    def ok(self):
        value = self.value.copy()
        info = self.check(value)
        if info != 'OK':
            self.info.setText(info)
            return
        cows, bulls = self.countBC(value)
        if bulls == self.num_len:
            self.new_window = ui_designer3.WidgetWinner()
            self.new_window.show()
            self.hide()
        self.info.setText('cows: {}\nbulls: {}'.format(cows, bulls))
