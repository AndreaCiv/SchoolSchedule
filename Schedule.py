from Session import Session
class Schedule:

    def __init__(self, schedule):
        self.schedule = []
        for i in range(0, int(len(schedule)/9)):
            self.schedule.append(Session(schedule[0:9]))
            schedule[0:9] = []

    def print_schedule(self):
        for session in self.schedule:
            session.print_session()