from data_manage import check_date, refactoring_data, create_elements


def create_graph(self, temps: list, heights: list, last_temp: float):
    self.ui.graphFrame.canvas.axes.clear()
    self.ui.graphFrame.canvas.axes.plot(temps, heights, label="Фактическая")
    self.ui.graphFrame.canvas.axes.plot(
        [last_temp - 20, last_temp],
        [1000, 0],
        label="Теоретическая",
        linestyle="dashed",
    )
    self.ui.graphFrame.canvas.axes.legend()
    self.ui.graphFrame.canvas.axes.set_title(f"Температура за {self.header_date}")
    self.ui.graphFrame.canvas.draw()


def update_graph(self):
    checks = check_date(self)
    if checks:
        self.header_date = self.ui.timeEdit.dateTime().toString("dd.MM.yyyy HH:mm") 
        self.first_date = self.ui.timeEdit.dateTime().toString("dd/MM/yyyy HH:mm:ss")
        self.dt = refactoring_data(self)
        element = create_elements(self)
        create_graph(self, element[0], element[1], element[2])
    else:
        pass
