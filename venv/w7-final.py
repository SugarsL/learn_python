import re
import requests

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

sys.path.append(r'/Users/lingjiajun/PycharmProjects/learn_python/venv')
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






if __name__=="__main__":

    app=QtWidgets.QApplication(sys.argv)

    widget=QtWidgets.QWidget()

    ui=Ui_Form()#这里改成你自己的项目名称，如果你没特意改过，就默认就行

    ui.setupUi(widget)

    '''add item'''
    data = retrieve_dji_list()
    #print(data[0]['code'])
    #print(data[1])
    ui.tableWidget.setColumnCount(3)
    # 设置表格列数
    ui.tableWidget.setRowCount(30)
    # 设置表格行数

    for i in range(len(data)):
        newitem0 = QTableWidgetItem(str(data[i]['code']))
        newitem1 = QTableWidgetItem(str(data[i]['name']))
        newitem2 = QTableWidgetItem(str(data[i]['price']))

        ui.tableWidget.setItem(i, 0, newitem0)
        ui.tableWidget.setItem(i, 1, newitem1)
        ui.tableWidget.setItem(i, 2, newitem2)


    widget.show()

    sys.exit(app.exec_())

