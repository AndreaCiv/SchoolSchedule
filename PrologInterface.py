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

    # Funzione che inserisce una nuova materia nel knowledge base dinamico di prolog
    # subject, professor e course vanno passate come stringhe
    # year, semester e weeklyLesson vanno passate come interi
    # availabilty deve essere una lista di liste, sove ogni lista più interna è composta da due elementi, giorno e ora
    # e indica uno slot di disponibilità di quella materia
    def insert_subject(self, subject, professor, course, year, semester, weeklyLessons, availability):
        query = "assertz(subject(\"" + subject + "\",\"" + professor + "\",\"" + course + "\"," + str(year) + "," + str(semester) + ","+ str(weeklyLessons) + "))."
        self.prolog_thread.query(query)
        for item in availability:
            self.insert_availability(subject, item[0], item[1])
        return True

    # Funzione che inserisce una nuova disponibilità nel knowledge base dinamico di prolog
    # subject, day e startHour devono essere delle stringhe
    def insert_availability(self, subject, day, startHour):
        query = "assertz(availability(\"" + subject + "\",\"" + day + "\",\"" + startHour + "\"))."
        self.prolog_thread.query(query)
        return True

    # Funzione che rimuove dal knowledge base dinamico di prolog la materia passata come argomento e tutte le
    # disponibilità a essa riferite
    def remove_subject(self, subject):
        query1 = "retractall(subject(\""+ subject +"\",_,_,_,_,_))."
        query2 = "retractall(availability(\""+ subject +"\",_,_))."
        print(query1)
        print(query2)
        self.prolog_thread.query(query1)
        self.prolog_thread.query(query2)
        return True

    def prova(self):
        self.insert_subject("TAR", "Ippoliti", "Ingegneria Informatica", 3,1,1, [["Monday", "8:30"],["Thursday", "10:30"]])
        self.insert_subject("Basi di dati", "Diamantini", "Ingegneria Informatica", 3, 1, 1, [["Tuesday", "8:30"],["Friday", "10:30"]])
        self.insert_subject("Ricerca Operativa", "Marinelli", "Ingegneria Informatica", 3, 1, 1, [["Monday", "10:30"],["Wednesday", "10:30"]])
        self.remove_subject("TAR")
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