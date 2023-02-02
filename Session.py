class Session:
    def __init__(self, session):
        self.day = session[0]
        self.startHour = session[1]
        self.finishHour = session[2]
        self.subject = session[3]
        self.professor = session[4]
        self.course = session[5]
        self.year = session[6]
        self.semester = session[7]
        self.weeklyLessons = session[8]

    def print_session(self):
        print(self.day + " " + self.startHour + " " + self.finishHour + " " + self.subject + " " + self.professor + " " + self.course)
