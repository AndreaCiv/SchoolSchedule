from PyQt5.QtWidgets import QDialog

class ScheduleView(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()

        self.ScheduleView = Ui_Schedule()
        self.ScheduleView.setupUi(self)
