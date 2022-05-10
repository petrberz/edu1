import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QMainWindow


def digit_to_screen():
    if MainWindow.sender().text() in data.digits_list:
        data.lineEdit.setText(data.lineEdit.text() + MainWindow.sender().text())
    if MainWindow.sender().text() == '.' and data.lineEdit.text() != '':
        data.lineEdit.setText(data.lineEdit.text() + '.')

def operation():
    if data.lineEdit.text() != '':
        if data.lineEdit.text()[-1] in data.operations_list:
            data.lineEdit.setText(data.lineEdit.text()[:-1] + MainWindow.sender().text())
        else:
            oper_already = False
            st = data.lineEdit.text()
            for i in range(len(st) - 1):
                if st[i] in data.operations_list:
                    oper_already = True
            if not oper_already:
                data.lineEdit.setText(data.lineEdit.text() + MainWindow.sender().text())

def equally():
    if len(data.lineEdit.text()) > 2:
        first = ''
        second = ''
        operation = ''
        end_of_digit = False
        st = data.lineEdit.text()
        for i in range(len(st)):
            if (st[i] in data.digits_list or st[i] == '.') and not end_of_digit:
                first += st[i]
            elif st[i] in data.operations_list:
                operation = st[i]
                end_of_digit = True
            elif (st[i] in data.digits_list or st[i] == '.') and end_of_digit:
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
        data.lineEdit.setText(str(result))

def squaring():
    if data.lineEdit.text() != '':
        digit = float(data.lineEdit.text())
        data.lineEdit.setText(str(digit ** 2))

def squareRooting():
    if data.lineEdit.text() != '':
        digit = float(data.lineEdit.text())
        data.lineEdit.setText(str(digit ** 0.5))

def cleaningAll():
    data.lineEdit.setText("")

def clean_last_digit():
    st = data.lineEdit.text()
    for i in range(len(st)):
        if st[-1] not in data.operations_list:
            st = st[:-1]
        else:
            break
    data.lineEdit.setText(st)

def backspacing():
    data.lineEdit.setText(data.lineEdit.text()[:-1])

def retranslateUi(MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
    data.seven.setText(_translate("MainWindow", "7"))
    data.eight.setText(_translate("MainWindow", "8"))
    data.nine.setText(_translate("MainWindow", "9"))
    data.four.setText(_translate("MainWindow", "4"))
    data.five.setText(_translate("MainWindow", "5"))
    data.six.setText(_translate("MainWindow", "6"))
    data.one.setText(_translate("MainWindow", "1"))
    data.two.setText(_translate("MainWindow", "2"))
    data.three.setText(_translate("MainWindow", "3"))
    data.zero.setText(_translate("MainWindow", "0"))
    data.dot.setText(_translate("MainWindow", "."))
    data.percent.setText(_translate("MainWindow", "%"))
    data.squareRoot.setText(_translate("MainWindow", "√"))
    data.square.setText(_translate("MainWindow", "x^2"))
    data.clean.setText(_translate("MainWindow", "CE"))
    data.equal.setText(_translate("MainWindow", "="))
    data.addition.setText(_translate("MainWindow", "+"))
    data.subtraction.setText(_translate("MainWindow", "-"))
    data.multiplication.setText(_translate("MainWindow", "x"))
    data.cleanAll.setText(_translate("MainWindow", "C"))
    data.backspace.setText(_translate("MainWindow", "←"))
    data.division.setText(_translate("MainWindow", "÷"))
    data.settings.setText(_translate("MainWindow", "⚙"))


def setupUi(MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.setFixedSize(351, 446)
    MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
    data.centralwidget = QtWidgets.QWidget(MainWindow)
    data.centralwidget.setObjectName("centralwidget")

    # Описание кнопок

    data.one = QtWidgets.QPushButton(data.centralwidget)
    data.one.setGeometry(QtCore.QRect(20, 330, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.one.setFont(font)
    data.one.setObjectName("one")
    data.one.clicked.connect(data.digit_to_screen)

    data.two = QtWidgets.QPushButton(data.centralwidget)
    data.two.setGeometry(QtCore.QRect(110, 330, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.two.setFont(font)
    data.two.setObjectName("two")
    data.two.clicked.connect(data.digit_to_screen)

    data.three = QtWidgets.QPushButton(data.centralwidget)
    data.three.setGeometry(QtCore.QRect(200, 330, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.three.setFont(font)
    data.three.setObjectName("three")
    data.three.clicked.connect(data.digit_to_screen)

    data.four = QtWidgets.QPushButton(data.centralwidget)
    data.four.setGeometry(QtCore.QRect(20, 280, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.four.setFont(font)
    data.four.setObjectName("four")
    data.four.clicked.connect(data.digit_to_screen)

    data.five = QtWidgets.QPushButton(data.centralwidget)
    data.five.setGeometry(QtCore.QRect(110, 280, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.five.setFont(font)
    data.five.setObjectName("five")
    data.five.clicked.connect(data.digit_to_screen)

    data.six = QtWidgets.QPushButton(data.centralwidget)
    data.six.setGeometry(QtCore.QRect(200, 280, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.six.setFont(font)
    data.six.setObjectName("six")
    data.six.clicked.connect(data.digit_to_screen)

    data.seven = QtWidgets.QPushButton(data.centralwidget)
    data.seven.setGeometry(QtCore.QRect(20, 230, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.seven.setFont(font)
    data.seven.setObjectName("seven")
    data.seven.clicked.connect(data.digit_to_screen)

    data.eight = QtWidgets.QPushButton(data.centralwidget)
    data.eight.setGeometry(QtCore.QRect(110, 230, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.eight.setFont(font)
    data.eight.setObjectName("eight")
    data.eight.clicked.connect(data.digit_to_screen)

    data.nine = QtWidgets.QPushButton(data.centralwidget)
    data.nine.setGeometry(QtCore.QRect(200, 230, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.nine.setFont(font)
    data.nine.setStyleSheet("")
    data.nine.setObjectName("nine")
    data.nine.clicked.connect(data.digit_to_screen)

    data.zero = QtWidgets.QPushButton(data.centralwidget)
    data.zero.setGeometry(QtCore.QRect(20, 380, 171, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.zero.setFont(font)
    data.zero.setObjectName("zero")
    data.zero.clicked.connect(data.digit_to_screen)

    # Кнопки операций

    data.cleanAll = QtWidgets.QPushButton(data.centralwidget)   # C
    data.cleanAll.setGeometry(QtCore.QRect(110, 180, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.cleanAll.setFont(font)
    data.cleanAll.setObjectName("cleanAll")
    data.cleanAll.clicked.connect(data.cleaningAll)

    data.clean = QtWidgets.QPushButton(data.centralwidget)  # CE
    data.clean.setGeometry(QtCore.QRect(20, 180, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.clean.setFont(font)
    data.clean.setObjectName("clean")
    data.clean.clicked.connect(data.clean_last_digit)

    data.addition = QtWidgets.QPushButton(data.centralwidget)   # +
    data.addition.setGeometry(QtCore.QRect(290, 330, 40, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.addition.setFont(font)
    data.addition.setObjectName("addition")
    data.addition.clicked.connect(data.operation)

    data.subtraction = QtWidgets.QPushButton(data.centralwidget)    # -
    data.subtraction.setGeometry(QtCore.QRect(290, 280, 40, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.subtraction.setFont(font)
    data.subtraction.setObjectName("subtraction")
    data.subtraction.clicked.connect(data.operation)

    data.multiplication = QtWidgets.QPushButton(data.centralwidget)     # * x
    data.multiplication.setGeometry(QtCore.QRect(290, 230, 40, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.multiplication.setFont(font)
    data.multiplication.setObjectName("multiplication")
    data.multiplication.clicked.connect(data.operation)

    data.division = QtWidgets.QPushButton(data.centralwidget)   # ÷
    data.division.setGeometry(QtCore.QRect(290, 180, 40, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.division.setFont(font)
    data.division.setObjectName("division")
    data.division.clicked.connect(data.operation)

    data.percent = QtWidgets.QPushButton(data.centralwidget)   # %
    data.percent.setGeometry(QtCore.QRect(20, 130, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.percent.setFont(font)
    data.percent.setObjectName("percent")
    data.percent.clicked.connect(data.operation)

    data.equal = QtWidgets.QPushButton(data.centralwidget)  # =
    data.equal.setGeometry(QtCore.QRect(290, 380, 40, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.equal.setFont(font)
    data.equal.setObjectName("equal")
    data.equal.clicked.connect(data.equally)

    data.backspace = QtWidgets.QPushButton(data.centralwidget)
    data.backspace.setGeometry(QtCore.QRect(200, 180, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.backspace.setFont(font)
    data.backspace.setObjectName("backspace")
    data.backspace.clicked.connect(data.backspacing)

    data.dot = QtWidgets.QPushButton(data.centralwidget)
    data.dot.setGeometry(QtCore.QRect(200, 380, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.dot.setFont(font)
    data.dot.setObjectName("dot")
    data.dot.clicked.connect(data.digit_to_screen)

    data.squareRoot = QtWidgets.QPushButton(data.centralwidget)
    data.squareRoot.setGeometry(QtCore.QRect(110, 130, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.squareRoot.setFont(font)
    data.squareRoot.setObjectName("squareRoot")
    data.squareRoot.clicked.connect(data.digit_to_screen)
    data.squareRoot.clicked.connect(data.squareRooting)

    data.square = QtWidgets.QPushButton(data.centralwidget)
    data.square.setGeometry(QtCore.QRect(200, 130, 80, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.square.setFont(font)
    data.square.setObjectName("square")
    data.square.clicked.connect(data.digit_to_screen)
    data.square.clicked.connect(data.squaring)

    data.settings = QtWidgets.QPushButton(data.centralwidget)
    data.settings.setGeometry(QtCore.QRect(290, 130, 40, 40))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(10)
    data.settings.setFont(font)
    data.settings.setObjectName("settings")
    data.settings.clicked.connect(data.exit)

    data.lineEdit = QtWidgets.QLineEdit(data.centralwidget)
    data.lineEdit.setGeometry(QtCore.QRect(20, 40, 310, 60))
    font = QtGui.QFont()
    font.setFamily("Bahnschrift")
    font.setPointSize(15)
    font.setBold(True)
    font.setWeight(75)
    data.lineEdit.setFont(font)
    data.lineEdit.setAlignment(QtCore.Qt.AlignRight)
    data.lineEdit.setReadOnly(True)
    data.lineEdit.setObjectName("lineEdit")

    MainWindow.setCentralWidget(data.centralwidget)
    data.statusbar = QtWidgets.QStatusBar(MainWindow)
    data.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(data.statusbar)

    data.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    text_on = []
    data = {
        "digits_list": ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        "operations_list": ['-', '+', 'x', '%', '÷']
    }
    setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

# этот комментарий будет доступен всегда, открытые исходники жи
# самые лучшие блин
# самые самые