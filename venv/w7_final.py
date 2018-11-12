import re
import requests
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from w7qt import Ui_Form


def retrieve_dji_list():
    try:
        r = requests.get('http://money.cnn.com/data/dow30/')
    except ConnectionError as err:
        print(err)
    search_pattern = re.compile(r'class="wsod_symbol">(.*?)</a>.*?<span.*?">(.*?)</span>.*?\n.*?class="wsod_stream">(.*?)</span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    print(dji_list_in_text)
    dji_list = []
    for item in dji_list_in_text:
        #print(item[0],item[1],item[2])
        dji_list.append({'code': item[0], 'name': item[1], 'price': float(item[2])})
    return dji_list


def update_item(ui,first = False):

    #ui.tableWidget.clearContents()
    '''add item'''
    data = retrieve_dji_list()
    #print(data[0]['code'])
    #print(data[1])
    if first:
        ui.tableWidget.setColumnCount(3)
        # 设置表格列数
        ui.tableWidget.setRowCount(30)
        # 设置表格行数

        header = ["code", "name", "price"]
        ui.tableWidget.setHorizontalHeaderLabels(header)

    for i in range(len(data)):
        newitem0 = QTableWidgetItem(str(data[i]['code']))
        newitem1 = QTableWidgetItem(str(data[i]['name']))
        newitem2 = QTableWidgetItem(str(data[i]['price']))

        ui.tableWidget.setItem(i, 0, newitem0)
        ui.tableWidget.setItem(i, 1, newitem1)
        ui.tableWidget.setItem(i, 2, newitem2)
    print('-------------update_item-------------\n')


def show_plot():
    print('-----------show_plot------------\n')

if __name__=="__main__":

    app = QtWidgets.QApplication(sys.argv)

    widget = QtWidgets.QWidget()

    ui = Ui_Form()

    ui.setupUi(widget)

    ui.pushButton_refresh.clicked.connect(lambda :update_item(ui, False)) #使用lambda做槽函数传参调用
    ui.pushButton_show_msg.clicked.connect(show_plot)

    update_item(ui, True)

    widget.show()

    sys.exit(app.exec_())
