# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultss.ui'
#
# Created: Mon Apr 24 01:51:05 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!
import csv

from PyQt4 import QtCore, QtGui
from application import *


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

class Ui_MainWindow(object):


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
        model.fit(X, Y, epochs=10, batch_size=50)
        # evaluate the model
        scores = model.evaluate(X, Y)
        print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

        # calculate predictions
        dataset = numpy.loadtxt("scores.csv", delimiter=",", ndmin=2)
        Z = dataset[:, 0:17]
        predictions = model.predict(Z)
        #predictions = (" ".join(map(str, predict)))

        # round predictions
        rounded = [round(x[0]) for x in predictions]
        #rounded = ",".join(roun)
        # print(rounded)

        predict = (",".join(map(str, predictions)))
        roun= (",".join(map(str, rounded)))

        #print(predict,roun)

        #return predict, roun

        p = str(predict).replace('[', '').replace(']', '')
        r = str(roun).replace('[', '').replace(']', '')



        return p,r


    def assign(self):

        rou,pred = self.neural()
        #print(rou)
        #print(pred)
        #r = (" ".join(map(str, rou)))

        #pre = (" ".join(map(str, pred)))

        #p = (" ".join(map(float, pre)))
        #print(p)

        self.label_3.setText(pred)

        self.label_4.setText(rou)




    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 120, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 240, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 92, 111, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 210, 201, 71))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 342, 121, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)



        self.retranslateUi(MainWindow)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.assign)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "CLASS:", None))
        self.label_2.setText(_translate("MainWindow", "JUSTIFICATION:", None))
        self.label_3.setText(_translate("MainWindow", "label_3",None))
        self.label_4.setText(_translate("MainWindow", "label_4", None))
        self.pushButton.setText(_translate("MainWindow", "DONE", None))

        self.neural()

        self.assign()




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

