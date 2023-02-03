﻿from PrologInterface import PrologInterface
from PyQt6.QtWidgets import QApplication
import sys
from ScheduleView import ScheduleView

if __name__ == "__main__":
	file_name = "knowledge_base.pl"
	prologInterface = PrologInterface(file_name)
	possible_schedules = prologInterface.create_semester_schedule("Ingegneria Informatica", 1, 1)
	app = QApplication(sys.argv)
	view = ScheduleView()
	view.show()
	app.exec_()
	possible_schedules[0].print_schedule()
	prologInterface.quit()