import json
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog,QWidget


# Для локального сохранения в папке проекта
FILE_NAME = 'option.json'


class OptionMenu(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("property.ui", self)

        self.save.clicked.connect(self.save_file)
        self.load.clicked.connect(self.load_file)
        self.exit.clicked.connect(self.exit_button)
        self.setWindowTitle('Вводи параметров')


        try:
            self.load_file_locale()
        except:
            pass

        self.show()

    def save_file(self):

        data = {'login': self.login.text(),
                'password': self.password.text(),
                'ip': self.ip.text(),
                'api': self.api.text()
                }

        filename, _ = QFileDialog.getSaveFileName(self, "Выберите папку для сохранения настроек", "property.json",
                                                  'json (*.json)')
        if filename:
            with open(filename, 'w') as f:
                json.dump(data, f)
                self.save_property_local(data)

    def load_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Выберите папку для сохранения настроек", "property.json",
                                                  'json (*.json)')

        if filename:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.login.setText(data.get('login'))
                self.password.setText(data.get('password'))
                self.api.setText(data.get('api'))
                self.ip.setText(data.get('ip'))
                # Для записи данного файла в локальный каталог проекта
                self.save_property_local(data)

    def exit_button(self):
        self.close()

    @classmethod
    def get_property(cls,FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            data = json.load(f)
            return data

    def save_property_local(self, data):
        with open(FILE_NAME, 'w') as f:
            json.dump(data, f)



    def load_file_locale(self):

        with open(FILE_NAME, 'r') as f:
            data = json.load(f)
            self.login.setText(data.get('login'))
            self.password.setText(data.get('password'))
            self.api.setText(data.get('api'))
            self.ip.setText(data.get('ip'))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = OptionMenu()
    ex.show()
    sys.exit(app.exec())
