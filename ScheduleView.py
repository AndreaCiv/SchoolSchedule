from Ui_Schedule import Ui_Schedule
from PyQt6.QtWidgets import QDialog
class ScheduleView(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()

        self.ScheduleView = Ui_Schedule()
        self.ScheduleView.setupUi(self)

    def show_schedule(self):
        self.ScheduleView.setupUi(self)
        self.show()

