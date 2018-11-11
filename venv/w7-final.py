import re
import requests
import w7-qt

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


data = retrieve_dji_list()
print(data)



if __name__=="__main__":

    import sys

    app=QtWidgets.QApplication(sys.argv)

    widget=QtWidgets.QWidget()

    ui=Ui_Form()#这里改成你自己的项目名称，如果你没特意改过，就默认就行

    ui.setupUi(widget)

    widget.show()

    sys.exit(app.exec_())

