from Ui_Schedule import Ui_Schedule
from PyQt5.QtWidgets import *
class ScheduleView(QMainWindow):
    def __init__(self, prologInterface):
        super(QMainWindow, self).__init__()

        self.ScheduleView = Ui_Schedule()
        self.ScheduleView.setupUi(self, prologInterface)

    def show_schedule(self, prologInterface):
        self.ScheduleView.setupUi(self, prologInterface)
        self.show()

