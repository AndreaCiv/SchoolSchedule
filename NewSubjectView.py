from Ui_NewSubject import Ui_NewSubject
from PyQt5.QtWidgets import *
class NewSubjectView(QWidget):
    def __init__(self, prologInterface, popola_materie):
        super(QWidget, self).__init__()

        self.newSubjet = Ui_NewSubject()
        self.newSubjet.setupUi(self, prologInterface, self.close_function)
        self.popola_materie = popola_materie

    def show_new_subject_view(self):
        self.show()
        self.update()

    def close_function(self):
        self.popola_materie()
        self.close()


