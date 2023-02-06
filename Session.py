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

    def get_coordinates(self):
        coordinates = []

        if self.startHour == "8:30":
            coordinates.append(0)
        elif self.startHour == "10:30":
            coordinates.append(1)
        elif self.startHour == "14:30":
            coordinates.append(2)
        elif self.startHour == "16:30":
            coordinates.append(3)

        if self.day == "Monday":
            coordinates.append(0)
        elif self.day == "Thursday":
            coordinates.append(1)
        elif self.day == "Wednesday":
            coordinates.append(2)
        elif self.day == "Tuesday":
            coordinates.append(3)
        elif self.day == "Friday":
            coordinates.append(4)

        return coordinates