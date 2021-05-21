import re
import sys
from PyQt5 import QtWidgets

import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.StatusLabel.setVisible(False)
        self.AddAnket.clicked.connect(self.Add)
        self.Name3checkBox.clicked.connect(self.EnabledName3)

    def EnabledName3(self):
        if self.Name3checkBox.isChecked():
            self.Name3Edit.setEnabled(False)
        else:
            self.Name3Edit.setEnabled(True)


    def Add(self):



        Name1 = self.Name1Edit.text()
        Name2 = self.Name2Edit.text()
        Name3 = self.Name3Edit.text()

        age = self.spinBox.text()
        Phone = self.PhoneEdit.text()
        Email = self.EmailEdit.text()
        if self.radioButton_Male.isChecked():
            sex = "Мужской"
        else:
            sex = "Женский"

        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if Name1 == "":
            self.StatusLabel.setText("Не введено имя")
            self.StatusLabel.setVisible(True)
        elif Name2 == "":
            self.StatusLabel.setText("Не введена фамилия")
            self.StatusLabel.setVisible(True)
        elif Name3 == "" and not self.Name3checkBox.isChecked():
            self.StatusLabel.setText("Не введено отчество")
            self.StatusLabel.setVisible(True)
        elif not (re.search(regex, Email)):
            self.StatusLabel.setText("Некорректный Email")
            self.StatusLabel.setVisible(True)
        elif not (re.search('\d{11,11}',Phone)):
            self.StatusLabel.setText("Некорректный номер телефона")
            self.StatusLabel.setVisible(True)


        elif not (self.radioButton_Male.isChecked() or self.radioButton_Female.isChecked()):
            self.StatusLabel.setText("Не выбран пол")
            self.StatusLabel.setVisible(True)
        else:


            file = open("ankets.txt","a",encoding="utf-8",)
            file.write(Name1)
            file.write("&")
            file.write(Name2)
            file.write("&")
            file.write(Name3)
            file.write("&")
            file.write(age)
            file.write("&")
            file.write(Email)
            file.write("&")
            file.write(Phone)
            file.write("&")
            file.write(sex)
            file.write("\n")
            file.close()


            self.StatusLabel.setText("Анкета добавлена")
            self.StatusLabel.setVisible(True)


















def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()