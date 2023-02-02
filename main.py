from pyswip import Prolog

if __name__ == "__main__":
    prolog = Prolog()
    prolog.consult("knowledge_base_file_definitivo.pl")
    risposta = list(prolog.query("create_semester_schedule(\"Ingegneria Informatica\", 1,1,X)."))
    print(risposta)