.PHONY: lint

lint: 
	black . --exclude=venv

run:
	python myproject/manage.py runserver
