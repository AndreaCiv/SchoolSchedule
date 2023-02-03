from swiplserver import *
from Schedule import Schedule
class PrologInterface:

    def __init__(self, file_name):
        self.mqi = PrologMQI(prolog_path="c:/program files/swipl/bin")
        self.prolog_thread = self.mqi.create_thread()
        self.prolog_thread.query("set_prolog_flag(encoding,utf8).")
        self.prolog_thread.query("consult(\""+ file_name +"\").")

    # Funzione che ritorna tutti i corsi presenti nella knowledge base di prolog in una lista contenente, per ogni
    # corso, una lista contenente il nome del corso, l'anno e il semestre
    def get_courses(self):
        corsi = self.prolog_thread.query("get_courses(Bag).")
        return corsi[0]['Bag']

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

