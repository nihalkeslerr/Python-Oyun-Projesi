import subprocess
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


import sqlite3


class Ui_Log(object):


    def login(self):
        print('login button clicked')
        mail = self.mailLine.text()
        password = self.passLine.text()

        connection = sqlite3.connect('database.db')
        result = connection.execute(''' SELECT * FROM gamers WHERE mail = ? AND password = ? ''',(mail, password))
        if (self.mailLine.text()) != "" and (self.passLine.text()) != "":
            if len(result.fetchall()) > 0:
                print('user found')
                connection.execute('''INSERT INTO login(mail) VALUES(?)''', (mail,))
                connection.commit()
                self.mailLine.setText("")
                self.passLine.setText("")
                self.wronglbl.setText("")
                subprocess.call([sys.executable, 'ghostfield.py'])


            else:
                print('user not found')
                self.wronglbl.setText("*Wrong password or username")


        else:
            self.wronglbl.setText("*Please Fill in the Fields")


    def signin(self):
        from sign import Ui_Sign
        print('signupcheck button clicked')
        self.sign = QtWidgets.QMainWindow()
        self.Ui = Ui_Sign()
        self.Ui.setupUi(self.sign)
        self.sign.show()

    def main(self):
        from main import Ui_Main
        print('main button clicked')
        self.main = QtWidgets.QMainWindow()
        self.Ui = Ui_Main()
        self.Ui.setupUi(self.main)
        self.main.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 490)
        Form.setStyleSheet("*{\n"
"background-color: #f5b15d;\n"
"\n"
"}\n"
"\n"
"#gm_nm{\n"
"font:45px \"Marker Felt\";\n"
"color:#2a1f91;\n"
"\n"
"}")
        self.gm_nm = QtWidgets.QLabel(Form)
        self.gm_nm.setGeometry(QtCore.QRect(48, 50, 251, 51))
        self.gm_nm.setObjectName("gm_nm")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(68, 170, 191, 191))
        self.toolButton.setStyleSheet("border-image: url(:/Ghost/Sprites/logghost.png);")
        self.toolButton.setText("")
        self.toolButton.setIconSize(QtCore.QSize(100, 100))
        self.toolButton.setAutoRepeat(False)
        self.toolButton.setObjectName("toolButton")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(320, 60, 311, 361))
        self.frame.setStyleSheet("QFrame{\n"
"border:none;\n"
"background:#fdc47e;\n"
"}\n"
"\n"
"#log_lbl{\n"
"color:#2a1f91;\n"
"font: 23pt \"Marker Felt\";\n"
"}\n"
"\n"
"#wronglbl{\n"
"color:#2a1f91;\n"
"font: 14pt \"Marker Felt\";\n"
"}\n"
"\n"                             
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:#5371fd;\n"
"border-bottom: 1px solid #858587;\n"
"text-align:center;\n"
"    font: italic 15pt \"Marker Felt\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background: #2a1f91;\n"
"color: white;\n"
"border-radius:15px;\n"
"    font: 15pt \"Marker Felt\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"border-radius: 15px;\n"
"background: #756add;\n"
"cursor: point;\n"
"    font: 15pt \"Marker Felt\";\n"
"}\n"
"\n"
"QRadioButton{\n"
"color: #6577cd;\n"
"background: transparent;\n"
"font: 13pt \"Marker Felt\";\n"
"}\n"
"\n"
"#regbutton{\n"
"background: transparent;\n"
"color: #2a1f91;\n"
"font: 12pt \"Marker Felt\";\n"
"text-decoration: 2px underline;\n"
"}\n"
"#regbutton:hover{\n"
"background: transparent;\n"
"color: #756add;\n"
"font: 12pt \"Marker Felt\";\n"
"text-decoration: 2px underline;\n"
"}\n"
"\n"
"#signlbl{\n"
"font: 12pt \"Marker Felt\";\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mailLine = QtWidgets.QLineEdit(self.frame)
        self.mailLine.setGeometry(QtCore.QRect(50, 80, 211, 31))
        self.mailLine.setObjectName("mailLine")
        self.passLine = QtWidgets.QLineEdit(self.frame)
        self.passLine.setGeometry(QtCore.QRect(50, 120, 211, 31))
        self.passLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passLine.setObjectName("passLine")
        self.log_lbl = QtWidgets.QLabel(self.frame)
        self.log_lbl.setGeometry(QtCore.QRect(120, 20, 81, 31))
        self.log_lbl.setObjectName("log_lbl")
        self.signlbl = QtWidgets.QLabel(self.frame)
        self.signlbl.setGeometry(QtCore.QRect(70, 280, 151, 16))
        self.signlbl.setObjectName("signlbl")
        self.regbutton = QtWidgets.QPushButton(self.frame)
        self.regbutton.setGeometry(QtCore.QRect(210, 280, 41, 16))
        self.regbutton.setObjectName("regbutton")
        self.regbutton.clicked.connect(self.signin)
        self.regbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logButton_2 = QtWidgets.QPushButton(self.frame)
        self.logButton_2.setGeometry(QtCore.QRect(90, 190, 113, 32))
        self.logButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logButton_2.setObjectName("logButton_2")
        self.logButton_2.clicked.connect(self.login)
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(280, -10, 61, 61))
        self.toolButton_3.setStyleSheet("border-image: url(:/prt/icons8-party-64.png);\n"
"background:transparent;")
        self.toolButton_3.setText("")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.frame)
        self.toolButton_4.setGeometry(QtCore.QRect(250, 30, 61, 51))
        self.toolButton_4.setStyleSheet("border-image: url(:/prt/icons8-party-64.png);\n"
"background:transparent;")
        self.toolButton_4.setText("")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(self.frame)
        self.toolButton_5.setGeometry(QtCore.QRect(220, -10, 61, 51))
        self.toolButton_5.setStyleSheet("border-image: url(:/prt/icons8-party-64.png);\n"
"background:transparent;")
        self.toolButton_5.setText("")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.frame)
        self.toolButton_6.setGeometry(QtCore.QRect(280, 70, 61, 51))
        self.toolButton_6.setStyleSheet("border-image: url(:/prt/icons8-party-64.png);\n"
"background:transparent;")
        self.toolButton_6.setText("")
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.frame)
        self.toolButton_7.setGeometry(QtCore.QRect(180, -40, 61, 51))
        self.toolButton_7.setStyleSheet("border-image: url(:/prt/icons8-party-64.png);\n"
"background:transparent;")
        self.toolButton_7.setText("")
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_8 = QtWidgets.QToolButton(self.frame)
        self.toolButton_8.setGeometry(QtCore.QRect(290, 110, 61, 51))
        self.toolButton_8.setStyleSheet("border-image: url(:/prt/icons8-party-64.png);\n"
"background:transparent;")
        self.toolButton_8.setText("")
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_9 = QtWidgets.QToolButton(self.frame)
        self.toolButton_9.setGeometry(QtCore.QRect(300, 140, 61, 51))
        self.toolButton_9.setStyleSheet("border-image: url(:/prt/icons8-party-64.png);\n"
"background:transparent;")
        self.toolButton_9.setText("")
        self.toolButton_9.setObjectName("toolButton_9")
        self.mainbtn = QtWidgets.QToolButton(Form)
        self.mainbtn.setGeometry(QtCore.QRect(10, 430, 51, 51))
        self.mainbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainbtn.setStyleSheet("border-image: url(:/main/Sprites/mainpage.png);")
        self.mainbtn.setText("")
        self.mainbtn.setObjectName("mainbtn")
        self.mainbtn.clicked.connect(self.main)

        self.wronglbl = QtWidgets.QLabel(self.frame)
        self.wronglbl.setGeometry(QtCore.QRect(65, 240, 211, 31))
        self.wronglbl.setObjectName("wronglbl")

        self.toolButton_14 = QtWidgets.QToolButton(self.frame)
        self.toolButton_14.setGeometry(QtCore.QRect(80, 17, 31, 31))
        self.toolButton_14.setStyleSheet("border-image: url(:/Ghost/Sprites/logghost.png);\n"
                                         "background:transparent;")
        self.toolButton_14.setText("")
        self.toolButton_14.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_14.setAutoRepeat(False)
        self.toolButton_14.setObjectName("toolButton_14")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LOG IN"))
        self.gm_nm.setText(_translate("Form", "GHOSTFIELD"))
        self.mailLine.setPlaceholderText(_translate("Form", "E-MAIL"))
        self.passLine.setPlaceholderText(_translate("Form", "PASSWORD"))
        self.log_lbl.setText(_translate("Form", "LOG IN"))
        self.signlbl.setText(_translate("Form", "Don\'t have an account yet?"))
        self.regbutton.setText(_translate("Form", "Sign in"))
        self.logButton_2.setText(_translate("Form", "LOG IN"))
        self.wronglbl.setText(_translate("Form", " "))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Log()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
