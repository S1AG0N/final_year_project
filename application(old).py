# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interf.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from keras.models import Sequential
from keras.layers import Dense
import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from PyQt4 import QtCore, QtGui
from int_2 import Ui_MainWindow


class Ui_Dialog(object):

    def call(self):
        self.welcomeWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()


    def neural(self):
        seed = 5000
        numpy.random.seed(seed)

        # load Training500 dataset
        dataset = numpy.loadtxt("Training500.csv", delimiter=",", skiprows=1, ndmin=2)

        # split into input (X) and output (Y) variables
        X = dataset[:, 0:17]
        Y = dataset[:, 17]

        # create model
        model = Sequential()
        model.add(Dense(12, input_dim=17, kernel_initializer='uniform', activation='relu'))
        model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
        model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

        # Compile model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        # Fit the model
        model.fit(X, Y, nb_epoch=10, batch_size=50)
        # evaluate the model
        scores = model.evaluate(X, Y)
        print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

        # calculate predictions
        dataset = numpy.loadtxt("scores.csv", delimiter=",", ndmin=2)
        Z = dataset[:, 0:17]
        predictions = model.predict(Z)

        # round predictions
        rounded = [round(x[0]) for x in predictions]
        print(rounded)

        return rounded

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

    def test(self):
        self.pushButton.clicked.connect(self.textt)
        self.pushButton.clicked.connect(self.neural())
        self.pushButton.clicked.connect(self.call())

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1307, 867)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 161, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 121, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 141, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 161, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 68, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 280, 121, 19))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 330, 191, 19))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 390, 161, 19))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(40, 440, 161, 19))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(40, 540, 231, 19))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(40, 600, 191, 19))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(770, 20, 181, 19))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(780, 70, 68, 19))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(780, 130, 131, 19))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(40, 490, 141, 19))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(780, 200, 121, 19))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(780, 330, 201, 19))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(780, 260, 211, 19))
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(40, 660, 231, 19))
        self.label_20.setObjectName("label_20")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 780, 112, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 780, 112, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(330, 80, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 130, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 180, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 230, 113, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 280, 113, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(330, 390, 113, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(330, 440, 113, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(330, 480, 113, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(330, 540, 113, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(330, 600, 113, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(330, 650, 113, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(1020, 60, 113, 25))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(1020, 130, 113, 25))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_14.setGeometry(QtCore.QRect(1020, 200, 113, 25))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(1020, 260, 113, 25))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_16.setGeometry(QtCore.QRect(1020, 330, 113, 25))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_17.setGeometry(QtCore.QRect(330, 720, 113, 25))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(40, 730, 181, 19))
        self.label_19.setObjectName("label_19")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.test)
        # self.pushButton.clicked.connect(self.textt)

        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_3.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_4.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_5.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_6.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_7.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_8.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_9.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_10.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_11.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_17.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_12.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_13.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_14.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_15.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_16.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "APPLICATION FORM"))
        self.label.setText(_translate("Dialog", "LOAN DETAILS:"))
        self.label_2.setText(_translate("Dialog", "Credit Amount:"))
        self.label_3.setText(_translate("Dialog", "Duration of Credit:"))
        self.label_4.setText(_translate("Dialog", "Number of Credits:"))
        self.label_5.setText(_translate("Dialog", "Purpose:"))
        self.label_6.setText(_translate("Dialog", "Account Balance:"))
        self.label_7.setText(_translate("Dialog", "COLLETERAL DETAILS:"))
        self.label_8.setText(_translate("Dialog", "Highest Valued Asset:"))
        self.label_9.setText(_translate("Dialog", "Type of Apartment:"))
        self.label_10.setText(_translate("Dialog", "Length of current Employment:"))
        self.label_11.setText(_translate("Dialog", "Previous Payment Status:"))
        self.label_12.setText(_translate("Dialog", "PERSONAL DETAILS:"))
        self.label_13.setText(_translate("Dialog", "Age(yrs):"))
        self.label_14.setText(_translate("Dialog", "Marital Status:"))
        self.label_15.setText(_translate("Dialog", "Occupation:"))
        self.label_16.setText(_translate("Dialog", "Work Location:"))
        self.label_17.setText(_translate("Dialog", "Number of Dependencies:"))
        self.label_18.setText(_translate("Dialog", "Duration at Current Address:"))
        self.label_20.setText(_translate("Dialog", "Telephone Expenses/month:"))
        self.pushButton.setText(_translate("Dialog", "RUN"))
        self.pushButton_2.setText(_translate("Dialog", "CLEAR"))
        self.label_19.setText(_translate("Dialog", "Value Savings/Stock:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

