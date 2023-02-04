from Ui_SubjectsList import Ui_SubjectsList
from PyQt5.QtWidgets import *
class SubjectsListView(QWidget):
    def __init__(self, prologInterface, close_function):
        super(QWidget, self).__init__()

        self.ListView = Ui_SubjectsList()
        self.ListView.setupUi(self, prologInterface)
        self.close_function = close_function

    def show_subject_list_view(self):
        self.show()
        self.update()

    def closeEvent(self, QCloseEvent):
        self.close_function()
