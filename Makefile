run:
	python manage.py runserver

migrate:
	python manage.py migrate && make makemigrations

makemigrations:
	python manage.py makemigrations