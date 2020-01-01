from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(586, 143)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(20, 40, 541, 71))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.A = QtWidgets.QPushButton(self.splitter)
        self.A.setObjectName("A")
        self.B = QtWidgets.QPushButton(self.splitter)
        self.B.setObjectName("B")
        self.C = QtWidgets.QPushButton(self.splitter)
        self.C.setObjectName("C")
        self.D = QtWidgets.QPushButton(self.splitter)
        self.D.setObjectName("D")
        self.E = QtWidgets.QPushButton(self.splitter)
        self.E.setObjectName("E")
        self.F = QtWidgets.QPushButton(self.splitter)
        self.F.setObjectName("F")
        self.G = QtWidgets.QPushButton(self.splitter)
        self.G.setObjectName("G")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(translate("Form", "Пианино"))
        self.A.setText(translate("Form", "До"))
        self.B.setText(translate("Form", "Ре"))
        self.C.setText(translate("Form", "Ми"))
        self.D.setText(translate("Form", "Фа"))
        self.E.setText(translate("Form", "Соль"))
        self.F.setText(translate("Form", "Ля"))
        self.G.setText(translate("Form", "Си"))

