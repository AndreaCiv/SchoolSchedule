from swiplserver import *
from Schedule import *
class PrologInterface:

    def __init__(self, file_name):
        # tendenzialmente il prolog path per windows è questo, per altri sistemi operativi (MacOS) potrebbe non essere necessario specificarlo
        # nel caso di errore verificare che siano scaricati swiplserver (e verificare path del file eseguibile swipl) e PyQt5
        self.mqi = PrologMQI(prolog_path="c:/program files/swipl/bin")
        self.prolog_thread = self.mqi.create_thread()
        self.prolog_thread.query("set_prolog_flag(encoding,utf8).")
        self.prolog_thread.query("consult(\""+ file_name +"\").")

    # Funzione che ritorna tutti i corsi presenti nella knowledge base di prolog in una lista contenente, per ogni
    # corso, una lista contenente il nome del corso, l'anno e il semestre
    def get_courses(self):
        corsi = self.prolog_thread.query("get_all_courses(Bag).")
        courses = corsi[0]['Bag']
        return courses

    def get_years_by_course(self, course):
        anni = self.prolog_thread.query("get_all_years_by_course(\""+ course +"\", Years).")
        years = anni[0]['Years']
        return years

    def get_semesters_by_course_and_year(self, course, year):
        semestri = self.prolog_thread.query("get_all_semesters_by_course_and_year(\""+course+"\","+year+", Semesters).")
        semesters = semestri[0]['Semesters']
        return semesters

    def insert_subject(self, subject, professor, course, year, semester, weeklyLessons):
        query = "assertz(subject(\"" + subject + "\",\"" + professor + "\",\"" + course + "\"," + str(year) + "," \
                + str(semester) + ","+ str(weeklyLessons) + "))."
        self.prolog_thread.query(query)
        return True

    def insert_availability(self, subject, day, startHour):
        query = "assertz(availability(\"" + subject + "\",\"" + day + "\",\"" + startHour + "\"))."
        self.prolog_thread.query(query)
        return True

    def insert_subject_and_availability(self, subject, professor, course, year, semester, weeklyLessons, availabilities):
        self.insert_subject(subject, professor, course, year, semester, weeklyLessons)
        for availability in availabilities:
            self.insert_availability(subject, availability[0], availability[1])
        return True

    def delete_subject(self, subject):
        query1 = "retractall(subject(\""+subject+"\",_,_,_,_,_))."
        query2 = "retractall(availability(\""+subject+"\",_,_))."
        self.prolog_thread.query(query1)
        self.prolog_thread.query(query2)
        return True


    # Funzione che ritorna la lista contenente tutti i possibili orari del corso selezionato, di quell'anno
    # e di quel semestre
    def create_semester_schedule(self, course, year, semester):
        result = self.prolog_thread.query("limit(200,create_semester_schedule(\""+ course +"\","+ str(year) +","+ str(semester) +",X)).")
        if result==False:
            return False
        possible_schedules = []
        for item in result:
            raw_schedule = item['X']
            schedule = Schedule(raw_schedule)
            possible_schedules.append(schedule)
        return possible_schedules

    def get_subjects(self):
        query = "get_subjects(Bag)."
        subjects = self.prolog_thread.query(query)
        return subjects[0]['Bag']

    # Funzione da richiamare per bloccare i thread di swiplserver e uscire dal programma
    def quit(self):
        self.mqi.stop()