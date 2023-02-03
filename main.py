from PrologInterface import PrologInterface

if __name__ == "__main__":
	file_name = "knowledge_base.pl"
	prologInterface = PrologInterface(file_name)
	possible_schedules = prologInterface.create_semester_schedule("Ingegneria Informatica", 1, 1)
	possible_schedules[0].print_schedule()
	prologInterface.quit()