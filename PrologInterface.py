from swiplserver import *
from Schedule import *
class PrologInterface:

    def __init__(self, file_name):
        self.mqi = PrologMQI()
        self.prolog_thread = self.mqi.create_thread()
        self.prolog_thread.query("set_prolog_flag(encoding,utf8).")
        self.prolog_thread.query("consult(\""+ file_name +"\").")

    # Funzione che ritorna tutti i corsi presenti nella knowledge base di prolog in una lista contenente, per ogni
    # corso, una lista contenente il nome del corso, l'anno e il semestre
    def get_courses(self):
        corsi = self.prolog_thread.query("get_courses(Bag).")
        return corsi[0]['Bag']

    def insert_subject(self, subject, professor, course, year, semester, weeklyLessons):
        query = "assertz(subject(\"" + subject + "\",\"" + professor + "\",\"" + course + "\"," + str(year) + "," + str(semester) + ","+ str(weeklyLessons) + "))."
        print(query)
        self.prolog_thread.query(query)
        return True

    def insert_availability(self, subject, day, startHour):
        query = "assertz(availability(\"" + subject + "\",\"" + day + "\",\"" + startHour + "\"))."
        print(query)
        self.prolog_thread.query(query)
        return True

    def prova(self):
        self.insert_subject("TAR", "Ippoliti", "Ingegneria Informatica", 3,1,1)
        self.insert_subject("Basi di dati", "Diamantini", "Ingegneria Informatica", 3, 1, 1)
        self.insert_subject("Ricerca Operativa", "Marinelli", "Ingegneria Informatica", 3, 1, 1)
        self.insert_availability("TAR", "Monday", "8:30")
        self.insert_availability("Basi di dati", "Thursday", "8:30")
        self.insert_availability("Ricerca Operativa", "Wednesday", "8:30")
        possible_schedules = self.create_semester_schedule("Ingegneria Informatica", 3, 1)
        possible_schedules[0].print_schedule()


    # Funzione che ritorna la lista contenente tutti i possibili orari del corso selezionato, di quell'anno
    # e di quel semestre
    def create_semester_schedule(self, course, year, semester):
        result = self.prolog_thread.query("create_semester_schedule(\""+ course +"\","+ str(year) +","+ str(semester) +",X)")
        possible_schedules = []
        for item in result:
            raw_schedule = item['X']
            schedule = Schedule(raw_schedule)
            possible_schedules.append(schedule)
        return possible_schedules

    # Funzione da richiamare per bloccare i thread di swiplserver e uscire dal programma
    def quit(self):
        self.mqi.stop()