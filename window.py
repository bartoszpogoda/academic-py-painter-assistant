# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(347, 247)
        self.tbHeight = QtWidgets.QLineEdit(Dialog)
        self.tbHeight.setGeometry(QtCore.QRect(170, 40, 113, 22))
        self.tbHeight.setObjectName("tbHeight")
        self.lblResult = QtWidgets.QLabel(Dialog)
        self.lblResult.setGeometry(QtCore.QRect(150, 180, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblResult.setFont(font)
        self.lblResult.setObjectName("lblResult")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 131, 31))
        self.label_4.setObjectName("label_4")
        self.tbEfficiency = QtWidgets.QLineEdit(Dialog)
        self.tbEfficiency.setGeometry(QtCore.QRect(30, 100, 71, 31))
        self.tbEfficiency.setObjectName("tbEfficiency")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(220, 190, 81, 31))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 111, 16))
        self.label_2.setObjectName("label_2")
        self.tbWidth = QtWidgets.QLineEdit(Dialog)
        self.tbWidth.setGeometry(QtCore.QRect(30, 40, 113, 22))
        self.tbWidth.setObjectName("tbWidth")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 211, 16))
        self.label_3.setObjectName("label_3")
        self.btnCalculate = QtWidgets.QPushButton(Dialog)
        self.btnCalculate.setGeometry(QtCore.QRect(30, 150, 171, 28))
        self.btnCalculate.setObjectName("btnCalculate")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblResult.setText(_translate("Dialog", "50"))
        self.label_4.setText(_translate("Dialog", "You need to buy: "))
        self.label_6.setText(_translate("Dialog", "paint cans."))
        self.label_2.setText(_translate("Dialog", "Wall height [m]"))
        self.label_3.setText(_translate("Dialog", "Paint can efficiency ( m^2 per can )"))
        self.btnCalculate.setText(_translate("Dialog", "How many do I need?"))
        self.label_7.setText(_translate("Dialog", "Wall width [m]"))

