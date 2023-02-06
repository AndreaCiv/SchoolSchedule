from PrologInterface import PrologInterface
from PyQt5.QtWidgets import *
import sys
from ScheduleView import ScheduleView

if __name__ == "__main__":
	file_name = "knowledge_base.pl"
	prologInterface = PrologInterface(file_name)
	prologInterface.get_courses()
	app = QApplication(sys.argv)
	view = ScheduleView(prologInterface)
	view.show()
	app.exec_()
	prologInterface.quit()