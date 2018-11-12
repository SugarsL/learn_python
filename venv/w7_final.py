import re
import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
import datetime as dt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from w7qt import Ui_Form


def retrieve_dji_list():
    try:
        r = requests.get('http://money.cnn.com/data/dow30/')
    except ConnectionError as err:
        print(err)
    search_pattern = re.compile(r'class="wsod_symbol">(.*?)</a>.*?<span.*?">(.*?)</span>.*?\n.*?'
                                r'class="wsod_stream">(.*?)</span>.*?\n.*?'
                                r'<span class=.*?>(.*?)</span>.*?\n.*?'
                                r'<span class=.*?>(.*?)</span>.*?\n.*?'
                                r'<td class="wsod_aRight">(.*?)</td>.*?')
    dji_list_in_text = re.findall(search_pattern, r.text)
    print(dji_list_in_text)
    dji_list = []
    for item in dji_list_in_text:
        #print(item[0],item[1],item[2])
        dji_list.append({'code': item[0], 'name': item[1], 'price': float(item[2]), 'change': float(item[3]),
                         'change_pct':item[4], 'volume':item[5]})
    print(len(dji_list))
    return dji_list


def update_item(ui,first = False):

    #ui.tableWidget.clearContents()
    '''add item'''
    data = retrieve_dji_list()
    #print(data[0]['code'])
    #print(data[1])


    if first:
        header = ["code", "name", "price", "change", "change_pct", "volume"]

        ui.tableWidget.setColumnCount(len(header))
        # 设置表格列数
        ui.tableWidget.setRowCount(30)
        # 设置表格行数

        ui.tableWidget.setHorizontalHeaderLabels(header)

    for i in range(len(data)):
        newitem0 = QTableWidgetItem(str(data[i]['code']))
        newitem1 = QTableWidgetItem(str(data[i]['name']))
        newitem2 = QTableWidgetItem(str(data[i]['price']))
        newitem3 = QTableWidgetItem(str(data[i]['change']))
        newitem4 = QTableWidgetItem(str(data[i]['change_pct']))
        newitem5 = QTableWidgetItem(str(data[i]['volume']))

        ui.tableWidget.setItem(i, 0, newitem0)  #code
        ui.tableWidget.setItem(i, 1, newitem1)  #name
        ui.tableWidget.setItem(i, 2, newitem2)  #price
        if data[i]['change'] > 0:
            newitem3.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
        else:
            newitem3.setForeground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        ui.tableWidget.setItem(i, 3, newitem3)  #change             +-

        if data[i]['change_pct'][0] == '+':
            newitem4.setForeground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))
        else:
            newitem4.setForeground(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
        ui.tableWidget.setItem(i, 4, newitem4)  #change_pct         +-

        ui.tableWidget.setItem(i, 5, newitem5)  #volume

    print('-------------update_item-------------\n')







def retrieve_quotes_historical(stock_code, start='', end=''):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)

    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
    quotes = quotes[::-1]
    return [item for item in quotes if 'type' not in item]


def show_plot(ui):
    code = str(ui.lineEdit.text())
    print(code)
    quotes = retrieve_quotes_historical(code)
    fields = ['date', 'open', 'close', 'high', 'low', 'volume']
    dates = []
    for i in range(0, len(quotes)):
        x = dt.datetime.utcfromtimestamp(int(quotes[i]['date']))
        y = dt.datetime.strftime(x, '%Y-%m-%d')
        dates.append(y)

    quotesdf = pd.DataFrame(quotes, index=dates, columns=fields)
    # remove unchecked fields fields_to_drop = ['date']
    fields_to_drop = ['date']
    #for key, value in self.option_list.items():
    #    if not value:
    #        fields_to_drop.append(key)
    quotesdf = quotesdf.drop(fields_to_drop, axis=1)
    quotesdf.plot()
    plt.show()
    print('-----------show_plot------------\n')

if __name__=="__main__":

    app = QtWidgets.QApplication(sys.argv)

    widget = QtWidgets.QWidget()

    ui = Ui_Form()

    ui.setupUi(widget)

    ui.pushButton_refresh.clicked.connect(lambda :update_item(ui, False)) #使用lambda做槽函数传参调用
    ui.pushButton_show_msg.clicked.connect(lambda:show_plot(ui))

    update_item(ui, True)

    widget.show()

    sys.exit(app.exec_())
