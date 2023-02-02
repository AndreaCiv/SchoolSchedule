from swiplserver import *

with PrologMQI() as mqi:
	with mqi.create_thread() as prolog_thread:
		result = prolog_thread.query("set_prolog_flag(encoding,utf8).")
		print(result)
		result = prolog_thread.query("consult(\"knowledge_base.pl\").")
		print(result)
		result = prolog_thread.query("create_semester_schedule(\"Ingegneria Informatica\", 1, 1, X)")
		print(result[1])