from PyQt6 import sip
import time
from threading import Lock


def clear_table(self):
    with Lock():

        time.sleep(5)

        try:
            # Очистка таблицы при срабатывании таймера
            self.verticalLayout.removeWidget(self.widget_towar)
            self.widget_towar.clear()

            # Удаление QTableWidget из QVBoxLayout и освобождение ресурсов
            sip.delete(self.widget_towar)
        except:
            pass

        self.have_towar = False
