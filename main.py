import sys
import sqlite3
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.label.setText('')
        self.pushButton.setText('Ok')
        self.pushButton.clicked.connect(self.run)

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT название_сорта FROM кофе""").fetchall()
        self.sp = []
        for elem in result:
            self.sp.append(elem[0])
        self.comboBox.addItems(self.sp)
        con.close()

    def run(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result2 = cur.execute("""SELECT * FROM кофе
        WHERE название_сорта = ?""", (self.comboBox.currentText(),)).fetchall()
        self.text = ''

        for elem in result2:
            self.text += 'название: ' + str(elem[1])
            self.text += '\n'
            self.text += 'степень обжарки: ' + str(elem[2])
            self.text += '\n'
            self.text += 'вид помола: ' + str(elem[3])
            self.text += '\n'
            self.text += 'описание вкуса: ' + str(elem[4])
            self.text += '\n'
            self.text += 'цена: ' + str(elem[5])
            self.text += '\n'
            self.text += 'объём упаковки: ' + str(elem[6])
            self.text += '\n'
        con.close()
        self.label.setText(self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())