from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from data_manage import get_data, get_first_last_date
from graphs_manage import update_graph
from matlab_generate import create_mlb_txt
from mplwidget import MplWidget
from ohata import OhataWindow
import sys


class MainWidget(QWidget):
    def __init__(self, width: int, height: int, parent=None):
        QWidget.__init__(self, parent)
        designer_file = QFile("mainWin.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        loader.registerCustomWidget(MplWidget)
        self.ui = loader.load(designer_file, self)
        designer_file.close()

        # self.width = width
        # self.height = height

        self.colorbar = None

        self.setMinimumSize(width // 2, height // 2)
        self.setWindowTitle("Хуй с другим графиком")

        # Создаю layout и добавляю в него фреймы c объектами
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.ui.buttonsFrame)
        main_layout.addWidget(self.ui.frame_2)

        if width >= 1920:
            self.ui.buttonsFrame.setStyleSheet("QWidget {font-size: 20px}")

        # Подключаем кнопки
        self.ui.ohataButton.clicked.connect(lambda: self.open_ohata(width, height))
        self.ui.updateButton.clicked.connect(lambda: update_graph(self))

        self.dates = tuple  # Создаем пустой кортеж для хранения первой и последней даты
        get_first_last_date(self)
        self.ui.timeEdit.setDateRange(self.dates[0], self.dates[1])
        self.ui.timeEdit.setDisplayFormat("yyyy-MM-dd")

        self.width = width
        self.height = height
        self.data = get_data("./data_files/", "./data.txt")
        update_graph(self)
        create_mlb_txt()

    def open_ohata(self, width, height):
        self.win = OhataWindow(width, height)
        self.win.ui.setStyleSheet("QWidget {font-size: 20px}")
        self.win.show()


def start_program():
    app = QApplication(sys.argv)
    screen_rect = app.primaryScreen().availableGeometry()
    mainwin = MainWidget(screen_rect.width(), screen_rect.height())
    mainwin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_program()
