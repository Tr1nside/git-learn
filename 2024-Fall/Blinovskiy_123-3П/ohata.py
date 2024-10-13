from PySide2.QtWidgets import QGridLayout, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from math import log10


class OhataWindow(QWidget):
    def __init__(self, width: int, height: int, parent=None):
        QWidget.__init__(self, parent)
        designer_file = QFile("ohata.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.ui = loader.load(designer_file, self)
        designer_file.close()
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)
        self.setMinimumSize(400, 250)
        self.setMaximumSize(400, 250)

        self.setWindowTitle("Модель Окамура-Хата")

        self.set_sliderLine_text()

        self.ui.Slider_freq.valueChanged.connect(self.set_sliderLine_text)
        self.ui.Slider_ht_bs.valueChanged.connect(self.set_sliderLine_text)
        self.ui.Slider_ht_ms.valueChanged.connect(self.set_sliderLine_text)
        self.ui.Slider_bs_ms.valueChanged.connect(self.set_sliderLine_text)

    def set_sliderLine_text(self):
        self.ui.lineEdit_freq.setText(str(self.ui.Slider_freq.value()))
        self.ui.lineEdit_ht_bs.setText(str(self.ui.Slider_ht_bs.value()))
        self.ui.lineEdit_ht_ms.setText(str(self.ui.Slider_ht_ms.value()))
        self.ui.lineEdit_bs_ms.setText(str(self.ui.Slider_bs_ms.value()))

        self.calculate(self.get_data())

    def get_data(self):
        data = (
            int(self.ui.lineEdit_freq.text()),
            int(self.ui.lineEdit_ht_bs.text()),
            int(self.ui.lineEdit_ht_ms.text()),
            int(self.ui.lineEdit_bs_ms.text()),
        )
        return data

    def calculate(self, data: tuple):
        pt = 47
        log_f = log10(data[0])
        log_ht = log10(data[1])
        log_r = log10(data[3])

        alpha = (1.1 * log_f - 0.7) * data[2] - (1.56 * log_f - 0.8)
        kf = 4.78 * pow(log_f, 2) - 18.33 * log_f + 40.94

        power = (
            pt
            - 69.55
            - 26.16 * log_f
            - (44.9 - 6.55 * log_ht) * log_r
            + 13.82 * log_ht
            + alpha
            + kf
        )

        self.ui.lineEdit_power.setText(str(power))
