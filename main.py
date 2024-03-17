import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar, QMenu
from screeninfo import get_monitors
from property import OptionMenu,FILE_NAME
from exchange import Exchange


# Получение разрешение текущего экрана
monitors = get_monitors()
main_width = monitors[0].width
main_height = monitors[0].height
op = None

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.resize(main_width, main_height)
        self.barcode.setFixedWidth(main_width)
        self.barcode.editingFinished.connect(self.__edit_finished_Barcode)

        # Очистка имен таблиц
        self.clear_product_roperty()
        self.clear_product_name()
        self.barcode.clear()

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

        barcode = self.barcode.text()
        if barcode == "" :
            return

        option = OptionMenu.get_property(FILE_NAME)
        data = Exchange(option,barcode).get_barcode()


        if data == None:
            return None
        self.set_product_name()


        self.set_product_property(data)

        # Закоментил так как не смог скачать sql alchemy но если скачать будет работать
        # try:
        #     dbb = db.MyData()
        #     dbb.insert_data(data)
        # except:
        #     pass


    def set_product_property(self,data):
        self.product.setText(data.get('product'))
        self.product.adjustSize()
        self.unit.setText(data.get('unit'))
        self.unit.adjustSize()
        self.remainder.setText(str(data.get('remainder')))
        self.remainder.adjustSize()
        self.price.setText(str(data.get('price')))
        self.price.adjustSize()

        self.barcode.clear()

    def clear_product_roperty(self):
        self.product.setText('')
        self.unit.setText('')
        self.remainder.setText('')
        self.price.setText('')

    def clear_product_name(self):
        self.product_name.setText('')
        self.unit_name.setText('')
        self.remainder_name.setText('')
        self.price_name.setText('')

    def set_product_name(self):
        self.product_name.setText('Наименование товара')
        self.unit_name.setText('Единица измерения')
        self.remainder_name.setText('Остаток')
        self.price_name.setText('Цена')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
