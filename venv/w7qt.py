# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w7qt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(696, 450)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 661, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 20, 81, 20))
        self.label.setObjectName("label")
        self.pushButton_show_msg = QtWidgets.QPushButton(Form)
        self.pushButton_show_msg.setGeometry(QtCore.QRect(240, 10, 114, 32))
        self.pushButton_show_msg.setObjectName("pushButton_show_msg")
        self.pushButton_quit = QtWidgets.QPushButton(Form)
        self.pushButton_quit.setGeometry(QtCore.QRect(30, 400, 114, 32))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.pushButton_refresh = QtWidgets.QPushButton(Form)
        self.pushButton_refresh.setGeometry(QtCore.QRect(190, 400, 114, 32))
        self.pushButton_refresh.setObjectName("pushButton_refresh")

        self.retranslateUi(Form)
        self.pushButton_quit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "stock code :"))
        self.pushButton_show_msg.setText(_translate("Form", "show msg"))
        self.pushButton_quit.setText(_translate("Form", "quit"))
        self.pushButton_refresh.setText(_translate("Form", "refresh"))

