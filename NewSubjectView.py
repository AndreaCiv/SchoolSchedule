from Ui_NewSubject import Ui_NewSubject
from PyQt5.QtWidgets import *
class NewSubjectView(QWidget):
    def __init__(self, prologInterface):
        super(QWidget, self).__init__()

        self.newSubjet = Ui_NewSubject()
        self.ListView.setupUi(self, prologInterface)

    def show_new_subject_view(self):
        self.show()
        self.update()
