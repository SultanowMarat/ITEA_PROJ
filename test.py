import sys
import threading

from PyQt6 import uic, QtCore, sip
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QTableWidget, QTableWidgetItem
from screeninfo import get_monitors
from property import OptionMenu, FILE_NAME
from exchange import Exchange
from threadingFunction import clear_table
import db

# Получение разрешение текущего экрана
monitors = get_monitors()
main_width = monitors[0].width
main_height = monitors[0].height
op = None


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("test.ui", self)
        self.resize(main_width, main_height)
        self.barcode.setFixedWidth(main_width)
        self.barcode.editingFinished.connect(self.__edit_finished_Barcode)
        # self.create_QTableWidget()
        # Очистка имен таблиц
        # self.clear_product_roperty()
        # self.clear_product_name()
        # self.barcode.clear()
        self.have_towar = False
        self.create_menu_bar()

    def create_menu_bar(self):

        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        main_menu = QMenu('&Параметры', self)
        self.menuBar.addMenu(main_menu)

        property_menu = main_menu.addAction('Настройки соединения', self.property_click)

    def property_click(self):
        global op
        op = OptionMenu()

    def __edit_finished_Barcode(self):

        self.time_counter = False

        if self.have_towar == False:
            self.create_QTableWidget()

        barcode = self.barcode.text()
        if barcode == "":
            return

        option = OptionMenu.get_property(FILE_NAME)
        data = Exchange(option, barcode).get_barcode()

        if data == None:
            return None
        # Закоментил так как не смог скачать sql alchemy но если скачать будет работать
        # try:
        #     dbb = db.MyData()
        #     dbb.insert_data(data)
        # except:
        #     pass

        self.add_row(data)

        self.barcode.clear()

        job = threading.Thread(target=clear_table, args=(self,))
        job.start()

        self.have_towar = True

        # self.clear_timer = QtCore.QTimer(self)
        # self.clear_timer.timeout.connect(self.clear_table)
        # self.clear_timer.start(1000000)

    def add_row(self, data):

        self.widget_towar.setRowCount(1)

        product = QTableWidgetItem(data.get('product'))
        unit = QTableWidgetItem(data.get('unit'))
        price = QTableWidgetItem(data.get('price'))
        remainder = QTableWidgetItem(data.get('remainder'))

        self.widget_towar.setItem(0, 0, product)
        self.widget_towar.setItem(0, 1, unit)
        self.widget_towar.setItem(0, 2, price)
        self.widget_towar.setItem(0, 3, remainder)

    def create_QTableWidget(self):

        self.widget_towar = QTableWidget(self)
        self.widget_towar.setColumnCount(4)
        self.widget_towar.setHorizontalHeaderLabels(['Товар', "Единица измерения", "Цена", "Остаток"])
        self.verticalLayout.addWidget(self.widget_towar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
