from Ui_Schedule import Ui_Schedule
from PyQt5.QtWidgets import *
class ScheduleView(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.ScheduleView = Ui_Schedule()
        self.ScheduleView.setupUi(self)

    def show_schedule(self):
        self.ScheduleView.setupUi(self)
        self.show()

