from data_manage import check_date, refactoring_data, create_elements
import matplotlib.dates as mdates
from datetime import datetime


def create_graph(self, temps: list, heights: list, dates: float):
    dates = [datetime.strptime(ts, "%H:%M:%S") for ts in dates]
    for ax in self.ui.graphFrame.canvas.figure.get_axes():  # Исправлено на get_axes()
        self.ui.graphFrame.canvas.figure.delaxes(ax)
    self.ui.graphFrame.canvas.axes = self.ui.graphFrame.canvas.figure.add_subplot(111)
    contour = self.ui.graphFrame.canvas.axes.contourf(dates, heights, temps)
    self.ui.graphFrame.canvas.axes.set_xlabel("Дата")  # Метка по оси X
    self.ui.graphFrame.canvas.axes.set_ylabel("Высота")  # Метка по оси Y
    self.ui.graphFrame.canvas.axes.set_title("Контурный график температуры")
    self.ui.graphFrame.canvas.axes.xaxis.set_major_locator(
        mdates.HourLocator(interval=1)
    )
    self.ui.graphFrame.canvas.axes.xaxis.set_major_formatter(
        mdates.DateFormatter("%H:%M:%S")
    )
    self.colorbar = self.ui.graphFrame.canvas.figure.colorbar(contour)
    self.ui.graphFrame.canvas.draw()


def update_graph(self):
    checks = check_date(self)
    if checks:
        self.header_date = self.ui.timeEdit.dateTime().toString("dd.MM.yyyy")
        self.first_date = self.ui.timeEdit.dateTime().toString("dd/MM/yyyy")
        self.dt = refactoring_data(self)
        element = create_elements(self)
        create_graph(self, element[0], element[1], element[2])
    else:
        pass
