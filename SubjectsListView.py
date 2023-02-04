from Ui_SubjectsList import Ui_SubjectsList
from PyQt5.QtWidgets import *
class SubjectsListView(QWidget):
    def __init__(self, prologInterface):
        super(QWidget, self).__init__()

        self.ListView = Ui_SubjectsList()
        self.ListView.setupUi(self, prologInterface)

    def show_subject_list_view(self):
        self.show()
        self.update()
