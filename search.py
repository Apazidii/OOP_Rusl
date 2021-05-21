import sys
from PyQt5 import QtWidgets

import design2

class ExampleApp(QtWidgets.QMainWindow, design2.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.Search.clicked.connect(self.search)

    def search(self):
        Name1 = self.Name1.text()
        Name2 = self.Name2.text()
        Age = self.Age.text()

        file = open("ankets.txt","r",encoding="utf-8")

        k = file.read()
        k = k.split("\n")
        k.pop(-1)
        for i in range(0, len(k)):
            k[i] = k[i].split("&")


        res = ""
        for i in range(0,len(k)):
            if Name1 == k[i][0]:
                if Name2 == k[i][1]:
                    if Age == k[i][3]:
                        res = "Имя: "+k[i][0]+"\n---------\n"+"Фамилия: "+k[i][1]+"\n---------\n"+"Отчество: "+k[i][2]+"\n---------\n"+"Пол: "+k[i][6]+"\n---------\n"+"Возраст: "+k[i][3]+"\n---------\n"+"Номер телефона: "+k[i][5]+"\n---------\n"+"Email: "+k[i][4]


        if res == "":
            self.textBrowser.setText("Совпадений не найдено")
        else:
            self.textBrowser.setText(res)

        file.close()






def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()