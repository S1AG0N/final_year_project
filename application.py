# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created: Sun Apr 23 19:17:30 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from keras.models import Sequential
from keras.layers import Dense
from results import *
import numpy
import csv

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):


    def textt(self):
        amount = self.lineEdit.text()
        duration = self.lineEdit_2.text()
        credit = self.lineEdit_3.text()
        purpose = self.lineEdit_4.text()
        balance = self.lineEdit_5.text()
        value = self.lineEdit_6.text()
        apartment = self.lineEdit_7.text()
        occupation = self.lineEdit_8.text()
        length = self.lineEdit_9.text()
        status = self.lineEdit_10.text()
        phone_exp = self.lineEdit_11.text()
        age = self.lineEdit_12.text()
        marital = self.lineEdit_13.text()
        work_location = self.lineEdit_14.text()
        duration_on_add = self.lineEdit_15.text()
        dependencies = self.lineEdit_16.text()
        savings = self.lineEdit_17.text()

        with open("scores.csv", "w") as scoreFile:
            scoreFileWriter = csv.writer(scoreFile)
            scoreFileWriter.writerow(
                [amount, duration, credit, purpose, balance, value, apartment, occupation, length, status,
                 phone_exp, age, marital, work_location, duration_on_add, dependencies, savings])

        scoreFile.close()

        print('textt method called')



    def cal(self):


        self.welcomeWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()
        return self.welcomeWindow


    def test(self):
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textt)
        #self.pushButton.clicked.connect(self.textt)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.neural)
        #self.pushButton.clicked.connect(self.neural())
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cal)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calll())
        #self.pushButton.clicked.connect(self.call)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.assign)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.lower)





    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(2251, 867)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 161, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 121, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 141, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 161, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 68, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 280, 121, 19))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 330, 191, 19))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 390, 161, 19))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 440, 161, 19))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(40, 540, 231, 19))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 600, 191, 19))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(770, 20, 181, 19))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(780, 70, 68, 19))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(780, 130, 131, 19))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(40, 490, 141, 19))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(780, 200, 121, 19))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(780, 330, 201, 19))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(780, 260, 211, 19))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_20 = QtGui.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(40, 660, 231, 19))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 780, 112, 71))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 780, 112, 71))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(330, 80, 113, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 130, 113, 25))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 180, 113, 25))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 230, 113, 25))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 280, 113, 25))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(330, 390, 113, 25))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(330, 440, 113, 25))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(330, 480, 113, 25))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(330, 540, 113, 25))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(330, 600, 113, 25))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(330, 650, 113, 25))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(1020, 60, 113, 25))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(1020, 130, 113, 25))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(Dialog)
        self.lineEdit_14.setGeometry(QtCore.QRect(1020, 200, 113, 25))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.lineEdit_15 = QtGui.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(1020, 260, 113, 25))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(Dialog)
        self.lineEdit_16.setGeometry(QtCore.QRect(1020, 330, 113, 25))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.lineEdit_17 = QtGui.QLineEdit(Dialog)
        self.lineEdit_17.setGeometry(QtCore.QRect(330, 720, 113, 25))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.label_19 = QtGui.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(40, 730, 181, 19))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_21 = QtGui.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(780, 410, 131, 19))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(780, 490, 211, 19))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(780, 550, 151, 19))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.lineEdit_18 = QtGui.QLineEdit(Dialog)
        self.lineEdit_18.setGeometry(QtCore.QRect(1020, 400, 113, 25))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_19 = QtGui.QLineEdit(Dialog)
        self.lineEdit_19.setGeometry(QtCore.QRect(1020, 480, 113, 25))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.lineEdit_20 = QtGui.QLineEdit(Dialog)
        self.lineEdit_20.setGeometry(QtCore.QRect(1020, 550, 113, 25))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.test)
        #self.pushButton.clicked.connect(self.test)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_4.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_5.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_6.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_7.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_8.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_9.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_10.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_11.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_17.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_12.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_13.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_14.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_15.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_16.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "APPLICATION FORM", None))
        self.label.setText(_translate("Dialog", "LOAN DETAILS:", None))
        self.label_2.setText(_translate("Dialog", "Credit Amount:", None))
        self.label_3.setText(_translate("Dialog", "Duration of Credit:", None))
        self.label_4.setText(_translate("Dialog", "Number of Credits:", None))
        self.label_5.setText(_translate("Dialog", "Purpose:", None))
        self.label_6.setText(_translate("Dialog", "Account Balance:", None))
        self.label_7.setText(_translate("Dialog", "COLLETERAL DETAILS:", None))
        self.label_8.setText(_translate("Dialog", "Highest Valued Asset:", None))
        self.label_9.setText(_translate("Dialog", "Type of Apartment:", None))
        self.label_10.setText(_translate("Dialog", "Length of current Employment:", None))
        self.label_11.setText(_translate("Dialog", "Previous Payment Status:", None))
        self.label_12.setText(_translate("Dialog", "PERSONAL DETAILS:", None))
        self.label_13.setText(_translate("Dialog", "Age(yrs):", None))
        self.label_14.setText(_translate("Dialog", "Marital Status:", None))
        self.label_15.setText(_translate("Dialog", "Occupation:", None))
        self.label_16.setText(_translate("Dialog", "Work Location:", None))
        self.label_17.setText(_translate("Dialog", "Number of Dependencies:", None))
        self.label_18.setText(_translate("Dialog", "Duration at Current Address:", None))
        self.label_20.setText(_translate("Dialog", "Telephone Expenses/month:", None))
        self.pushButton.setText(_translate("Dialog", "RUN", None))
        self.pushButton_2.setText(_translate("Dialog", "CLEAR", None))
        self.label_19.setText(_translate("Dialog", "Value Savings/Stock:", None))
        self.label_21.setText(_translate("Dialog", "Guarantors", None))
        self.label_22.setText(_translate("Dialog", "Concurrent Credits", None))
        self.label_23.setText(_translate("Dialog", "Instalment percent", None))




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

