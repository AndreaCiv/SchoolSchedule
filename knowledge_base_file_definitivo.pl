% subject(Subject, Professor, Course, Year, Semester, WeeklyLessons)
% dove WeeklyLessons è il numero di lezioni, da due ore, settimanali,
% Predicati per definire le materie da inserire nell'orario
subject("Analisi 1", "Montecchiari", "Ingegneria Informatica", 1,1,3).
subject("Algebra Lineare", "Marietti", "Ingegneria Informatica", 1,1,2).
subject("Fisica 1", "Albertini", "Ingegneria Informatica", 1,1,3).
subject("Lingua Inglese", "Scott", "Ingegneria Informatica", 1,1,1).
subject("Analisi 2", "Isernia", "Ingegneria Informatica", 1,2,4).
subject("Fisica 2", "Lucchetta", "Ingegneria Informatica", 1,2,4).
subject("Fondamenti Di Informatica", "Sernani", "Ingegneria Informatica", 1,2,6).
subject("Economia", "Iacobucci", "Ingegneria Informatica", 1,2,4).

% Predicati che definiscono i giorni della settimana in cui ci possono
% essere lezioni
day("Monday").
day("Thursday").
day("Wednesday").
day("Tuesday").
day("Friday").

% after_day_1(Day1, Day2)
% Predicati per definire se Day2 è il giorno successivo a Day1
after_day_1("Monday", "Thursday").
after_day_1("Thursday", "Wednesday").
after_day_1("Wednesday", "Tuesday").
after_day_1("Tuesday", "Friday").

% after_day(Day1, Day2)
% Predicati per definire se Day2 è uno dei giorni successivi a Day1
after_day(Day1, Day2) :- after_day_1(Day1, Day2).
after_day(Day1, Day2) :- after_day_1(Day1, Day3), after_day(Day3, Day2).


% after_hour_1(StartHour1, StartHour2)
% Predicati per definire se StartHour2 è l'ora di inizio (di
% una lezione) successiva all'ora di inizio StartHour1
after_hour_1("8:30","10:30").
after_hour_1("10:30","14:30").
after_hour_1("14:30","16:30").

% after_hour(StartHour1, StartHour2).
% Predicati per definire se StartHour2 è una delle ore di inizio (di
% una lezione) successiva all'ora di inizio StartHour1
after_hour(StartHour1, StartHour2) :- after_hour_1(StartHour1, StartHour2).
after_hour(StartHour1, StartHour2) :- after_hour_1(StartHour1,StartHour3), after_hour(StartHour3, StartHour2).

% Predicati che definiscono i possibili slot orari del calendario
% slot(Day, StartHour, FinishHour).
slot(Day,"8:30","10:30"):-
    day(Day).
slot(Day,"10:30","12:30"):-
    day(Day).
slot(Day,"14:30","16:30"):-
    day(Day).
slot(Day,"16:30","18:30"):-
    day(Day).

% availability(Subject, Day, StartHour).
% Predicati che definiscono, per ogni materia, la possibilità di fare
% lezione nel giorno Day e nell'ora StartHour
% NB: Anche se è possibile fare sempre lezione per una materia, ci deve
% comunque essere il predicato availability per quella materia che sarà
% sempre vero.
availability("Analisi 1", Day, StartHour) :- Day = "Monday", StartHour = "8:30" ; Day = "Wednesday", StartHour = "8:30"; Day = "Friday", StartHour= "8:30".
availability("Fisica 1", Day, _) :- Day = "Monday"; Day = "Wednesday"; Day = "Friday".
availability("Lingua Inglese", Day, _) :- Day = "Thursday"; Day = "Tuesday".
availability("Algebra Lineare", Day, _) :- Day = "Thursday"; Day = "Tuesday".

% Predicato che definisce l'assegnamento di una lezione ad uno slot secondo le disponibilitˆ di quella materia
session(Day, StartHour, FinishHour, Subject, Professor, Course, Year, Semester, WeeklyLessons):-
    slot(Day,StartHour, FinishHour), subject(Subject, Professor, Course, Year,Semester, WeeklyLessons),
    availability(Subject, Day, StartHour).

% Predicato che controlla se la seconda session passata viene dopo la prima
no_conflict_1(Day1, StartHour1, _, _, _, Course1, Year1, Semester1, _,
    Day2, StartHour2, _, _, _, Course2, Year2, Semester2, _):-
    Semester1 =:= Semester2, Year1 =:= Year2, Course1 = Course2,Day1 = Day2 , after_hour(StartHour1,StartHour2);
    Semester1 =:= Semester2, Year1 =:= Year2, Course1 = Course2 ,after_day(Day1,Day2),!.

% Predicato che controlla che le session presenti nella lista passata alla funzione siano successive alla session passata come primo argomento
no_conflict_2(_, _, _, _, _, _, _, _, _,[]).
no_conflict_2(Day, StartHour, FinishHour,Subject, Professor, Course, Year, Semester, WeeklyLessons, Schedule):-
    Schedule = [Day1, StartHour1, FinishHour1,Subject1,Professor1, Course1, Year1, Semester1, WeeklyLessons1| Tail],
    no_conflict_1(Day, StartHour, FinishHour,Subject, Professor, Course, Year, Semester, WeeklyLessons,
                  Day1, StartHour1, FinishHour1,Subject1,Professor1, Course1, Year1, Semester1, WeeklyLessons1),
    no_conflict_2(Day, StartHour, FinishHour, Subject, Professor, Course, Year, Semester, WeeklyLessons, Tail),!.

% Predicato che prende in ingresso il vettore dello schedule di una
% singola materia e controlla che non ci siano conflitti per quella
% materia e che le session siano ordinate cronologicamente
no_conflict_3([]).
no_conflict_3(Schedule):-
    Schedule = [Day1, StartHour1, FinishHour1,Subject1,Professor1, Course1, Year1, Semester1, WeeklyLessons1| Tail],
    no_conflict_2(Day1, StartHour1, FinishHour1,Subject1,Professor1, Course1, Year1, Semester1, WeeklyLessons1, Tail),
    no_conflict_3(Tail),!.

% Predicato che verifica che non ci siano conflitti tra le due session passate per argomento
no_conflict_4(Day1, StartHour1, _, _, _, Course1, Year1, Semester1, _,
    Day2, StartHour2, _, _, _, Course2, Year2, Semester2, _):-
    Semester1 =:= Semester2, Year1 =:= Year2, Course1 = Course2,Day1 = Day2 , StartHour1 \= StartHour2;
    Semester1 =:= Semester2, Year1 =:= Year2, Course1 = Course2 ,Day1 \= Day2,!.

% Predicato che controlla che non ci siano conflitti tra la session passata come argomento e le session presenti nel vettore passato come ultimo argomento
no_conflict_5(_, _, _, _, _, _, _, _, _,[]).
no_conflict_5(Day, StartHour, FinishHour,Subject, Professor, Course, Year, Semester, WeeklyLessons, Schedule):-
    Schedule = [Day1, StartHour1, FinishHour1,Subject1,Professor1, Course1, Year1, Semester1, WeeklyLessons1| Tail],
    no_conflict_4(Day, StartHour, FinishHour,Subject, Professor, Course, Year, Semester, WeeklyLessons,
                  Day1, StartHour1, FinishHour1,Subject1,Professor1, Course1, Year1, Semester1, WeeklyLessons1),
    no_conflict_5(Day, StartHour, FinishHour, Subject, Professor, Course, Year, Semester, WeeklyLessons, Tail),!.

% Predicato che controlla che non ci siano conflitti tra le session del calendario passato come argomento
no_conflict_6([]).
no_conflict_6(Schedule):-
    Schedule = [Day1, StartHour1, FinishHour1,Subject1,Professor1, Course1, Year1, Semester1, WeeklyLessons1| Tail],
    no_conflict_5(Day1, StartHour1, FinishHour1,Subject1,Professor1, Course1, Year1, Semester1, WeeklyLessons1, Tail),
    no_conflict_6(Tail),!.


% Predicato che passato il calendario di una materia e un giorno della settimana estrae la lista delle session di quel calendario di quel giorno
get_day_schedule([],_,_).
get_day_schedule(Schedule ,Day1, DaySchedule) :-
    Schedule = [Day, StartHour, FinishHour,Subject, Professor, Course, Year, Semester, WeeklyLessons|Tail],
    Day = Day1,
    get_day_schedule(Tail, Day1, DaySchedule1),
    append(DaySchedule1, [Day, StartHour, FinishHour,Subject, Professor, Course, Year, Semester, WeeklyLessons], DaySchedule);
    Schedule = [_, _, _, _, _, _, _, _, _|Tail],
    get_day_schedule(Tail, Day1, DaySchedule).


% Predicato che verifica, dato il calendario di un corso e i giorni di lezione di quel calendario, che per ogni giorno ci sia soltanto una lezione di quella materia
verify_subject_day_chedule(_,[]).
verify_subject_day_chedule(Schedule, Days) :-
    Days = [Day|Tail],
    get_day_schedule(Schedule, Day, DaySchedule),!,
    length(DaySchedule,9),
    verify_subject_day_chedule(Schedule, Tail).

% Predicato che dato un calendario estrae i giorni di lezione di quest'ultimo
extract_days([],_).
extract_days(Schedule, Days) :-
    Schedule = [Day,_,_,_,_,_,_,_,_|Tail],
    extract_days(Tail, Days1),
    append(Days1,[Day],Days).

% Predicato che rimuove i duplicati di una lista
remove_duplicates([], []).
remove_duplicates([Head | Tail], Result) :-
    member(Head, Tail), !,
    remove_duplicates(Tail, Result).
remove_duplicates([Head | Tail], [Head | Result]) :-
    remove_duplicates(Tail, Result).

% Predicato che verifica la correttezza di un calendario
verify_schedule(Schedule) :-
    extract_days(Schedule, Days1),
    remove_duplicates(Days1, Days),!,
    verify_subject_day_chedule(Schedule, Days).

% Predicato che crea il calendario settimanale di una singola materia
create_schedule(_, _, _, _, _, _, 0, _).
create_schedule(Subject, Professor, Course, Year, Semester, WeeklyLessons, RemainingWeeklyLessons, Schedule):-
    RemainingWeeklyLessons>0,
    session(Day, StartHour, FinishHour,Subject, Professor, Course, Year, Semester, WeeklyLessons),
    RemainingWeeklyLessons1 is RemainingWeeklyLessons-1,
    create_schedule(Subject, Professor, Course, Year, Semester, WeeklyLessons, RemainingWeeklyLessons1, Schedule1),
    append([Day, StartHour, FinishHour,Subject, Professor, Course, Year, Semester, WeeklyLessons],Schedule1, Schedule).

% Predicato che crea e verifica l'orario per una singola materia
create_subject_schedule(Subject, Professor, Course, Year, Semester, WeeklyLessons, Schedule):-
    subject(Subject, Professor, Course, Year, Semester, WeeklyLessons),
    create_schedule(Subject, Professor, Course, Year, Semester, WeeklyLessons, WeeklyLessons, Schedule),
    no_conflict_3(Schedule),
    verify_schedule(Schedule),
    Listlen is WeeklyLessons*9,
    length(Schedule, Listlen).

% Predicato che crea il calendario settimanale di un corso di studi
create_course_schedule([],_).
create_course_schedule(Bag,Schedule) :-
    Bag = [[Subject,Professor,WeeklyLessons]|Tail],
    subject(Subject, Professor, Course, Year, Semester, WeeklyLessons),
    create_subject_schedule(Subject, Professor, Course, Year, Semester, WeeklyLessons,SubjectSchedule),
    create_course_schedule(Tail,SubjectSchedule1),
    append(SubjectSchedule,SubjectSchedule1,Schedule).

% Predicato che crea e verifica l'orario di un semestre
create_semester_schedule(Course, Year, Semester, SemesterSchedule) :-
    findall([Subject,Professor,WeeklyLessons],subject(Subject, Professor, Course, Year, Semester , WeeklyLessons), Bag),
    create_course_schedule(Bag, SemesterSchedule),
    no_conflict_6(SemesterSchedule),
    print(SemesterSchedule).
