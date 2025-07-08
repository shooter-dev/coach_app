VENV_NAME?=.venv
PYTHON=${VENV_NAME}/bin/python3


freeze:
	${PYTHON} -m pip freeze > requirements.txt

run:
	${PYTHON} manage.py runserver

database:
	${PYTHON} manage.py makemigrations
	${PYTHON} manage.py migrate
