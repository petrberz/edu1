import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QMainWindow


class Ui_MainWindow(object):
    def __init__(self):
        self.digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.operations_list = ['-', '+', 'x', '%', '÷']

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(351, 446)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

    # Описание кнопок

        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(20, 330, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.one.clicked.connect(self.digit_to_screen)

        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(110, 330, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.two.clicked.connect(self.digit_to_screen)

        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(200, 330, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.three.clicked.connect(self.digit_to_screen)

        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(20, 280, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.four.clicked.connect(self.digit_to_screen)

        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(110, 280, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.five.clicked.connect(self.digit_to_screen)

        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(200, 280, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.six.clicked.connect(self.digit_to_screen)

        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(20, 230, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.seven.clicked.connect(self.digit_to_screen)

        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(110, 230, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.eight.clicked.connect(self.digit_to_screen)

        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(200, 230, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.nine.setFont(font)
        self.nine.setStyleSheet("")
        self.nine.setObjectName("nine")
        self.nine.clicked.connect(self.digit_to_screen)

        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(20, 380, 171, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.zero.clicked.connect(self.digit_to_screen)

    # Кнопки операций

        self.cleanAll = QtWidgets.QPushButton(self.centralwidget)   # C
        self.cleanAll.setGeometry(QtCore.QRect(110, 180, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.cleanAll.setFont(font)
        self.cleanAll.setObjectName("cleanAll")
        self.cleanAll.clicked.connect(self.cleaningAll)

        self.clean = QtWidgets.QPushButton(self.centralwidget)  # CE
        self.clean.setGeometry(QtCore.QRect(20, 180, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.clean.setFont(font)
        self.clean.setObjectName("clean")
        self.clean.clicked.connect(self.clean_last_digit)

        self.addition = QtWidgets.QPushButton(self.centralwidget)   # +
        self.addition.setGeometry(QtCore.QRect(290, 330, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.addition.setFont(font)
        self.addition.setObjectName("addition")
        self.addition.clicked.connect(self.operation)

        self.subtraction = QtWidgets.QPushButton(self.centralwidget)    # -
        self.subtraction.setGeometry(QtCore.QRect(290, 280, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.subtraction.setFont(font)
        self.subtraction.setObjectName("subtraction")
        self.subtraction.clicked.connect(self.operation)

        self.multiplication = QtWidgets.QPushButton(self.centralwidget)     # * x
        self.multiplication.setGeometry(QtCore.QRect(290, 230, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.multiplication.setFont(font)
        self.multiplication.setObjectName("multiplication")
        self.multiplication.clicked.connect(self.operation)

        self.division = QtWidgets.QPushButton(self.centralwidget)   # ÷
        self.division.setGeometry(QtCore.QRect(290, 180, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.division.setFont(font)
        self.division.setObjectName("division")
        self.division.clicked.connect(self.operation)

        self.percent = QtWidgets.QPushButton(self.centralwidget)   # %
        self.percent.setGeometry(QtCore.QRect(20, 130, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.percent.setFont(font)
        self.percent.setObjectName("percent")
        self.percent.clicked.connect(self.operation)

        self.equal = QtWidgets.QPushButton(self.centralwidget)  # =
        self.equal.setGeometry(QtCore.QRect(290, 380, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.equal.setFont(font)
        self.equal.setObjectName("equal")
        self.equal.clicked.connect(self.equally)

        self.backspace = QtWidgets.QPushButton(self.centralwidget)
        self.backspace.setGeometry(QtCore.QRect(200, 180, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.backspace.setFont(font)
        self.backspace.setObjectName("backspace")
        self.backspace.clicked.connect(self.backspacing)

        self.dot = QtWidgets.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(200, 380, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.dot.setFont(font)
        self.dot.setObjectName("dot")
        self.dot.clicked.connect(self.digit_to_screen)

        self.squareRoot = QtWidgets.QPushButton(self.centralwidget)
        self.squareRoot.setGeometry(QtCore.QRect(110, 130, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.squareRoot.setFont(font)
        self.squareRoot.setObjectName("squareRoot")
        self.squareRoot.clicked.connect(self.digit_to_screen)
        self.squareRoot.clicked.connect(self.squareRooting)

        self.square = QtWidgets.QPushButton(self.centralwidget)
        self.square.setGeometry(QtCore.QRect(200, 130, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.square.setFont(font)
        self.square.setObjectName("square")
        self.square.clicked.connect(self.digit_to_screen)
        self.square.clicked.connect(self.squaring)

        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(290, 130, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.settings.setFont(font)
        self.settings.setObjectName("settings")
        self.settings.clicked.connect(self.exit)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 310, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def digit_to_screen(self):
        if MainWindow.sender().text() in self.digits_list:
            self.lineEdit.setText(self.lineEdit.text() + MainWindow.sender().text())
        if MainWindow.sender().text() == '.' and self.lineEdit.text() != '':
            self.lineEdit.setText(self.lineEdit.text() + '.')

    def operation(self):
        if self.lineEdit.text() != '':
            if self.lineEdit.text()[-1] in self.operations_list:
                self.lineEdit.setText(self.lineEdit.text()[:-1] + MainWindow.sender().text())
            else:
                oper_already = False
                st = self.lineEdit.text()
                for i in range(len(st) - 1):
                    if st[i] in self.operations_list:
                        oper_already = True
                if not oper_already:
                    self.lineEdit.setText(self.lineEdit.text() + MainWindow.sender().text())

    def equally(self):
        if len(self.lineEdit.text()) > 2:
            first = ''
            second = ''
            operation = ''
            end_of_digit = False
            st = self.lineEdit.text()
            for i in range(len(st)):
                if (st[i] in self.digits_list or st[i] == '.') and not end_of_digit:
                    first += st[i]
                elif st[i] in self.operations_list:
                    operation = st[i]
                    end_of_digit = True
                elif (st[i] in self.digits_list or st[i] == '.') and end_of_digit:
                    second += st[i]
            first_int = float(first)
            second_int = float(second)
            result = 0.0
            if operation == '+':
                result = first_int + second_int
            elif operation == '-':
                result = first_int - second_int
            elif operation == 'x':
                result = first_int * second_int
            elif operation == '÷':
                result = first_int / second_int
            elif operation == '%':
                result = (first_int / second_int) * 100
            self.lineEdit.setText(str(result))

    def squaring(self):
        if self.lineEdit.text() != '':
            digit = float(self.lineEdit.text())
            self.lineEdit.setText(str(digit ** 2))

    def squareRooting(self):
        if self.lineEdit.text() != '':
            digit = float(self.lineEdit.text())
            self.lineEdit.setText(str(digit ** 0.5))

    def cleaningAll(self):
        self.lineEdit.setText("")

    def clean_last_digit(self):
        st = self.lineEdit.text()
        for i in range(len(st)):
            if st[-1] not in self.operations_list:
                st = st[:-1]
            else:
                break
        self.lineEdit.setText(st)

    def backspacing(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])

    def exit(self):
        if __name__ == '__main__':
            sys.exit(app.exec())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.percent.setText(_translate("MainWindow", "%"))
        self.squareRoot.setText(_translate("MainWindow", "√"))
        self.square.setText(_translate("MainWindow", "x^2"))
        self.clean.setText(_translate("MainWindow", "CE"))
        self.equal.setText(_translate("MainWindow", "="))
        self.addition.setText(_translate("MainWindow", "+"))
        self.subtraction.setText(_translate("MainWindow", "-"))
        self.multiplication.setText(_translate("MainWindow", "x"))
        self.cleanAll.setText(_translate("MainWindow", "C"))
        self.backspace.setText(_translate("MainWindow", "←"))
        self.division.setText(_translate("MainWindow", "÷"))
        self.settings.setText(_translate("MainWindow", "⚙"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    text_on = []
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
