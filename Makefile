.SILENT:
.PHONY: all update_pip init_db serve


all:
	echo ""
	echo "  init_db      Init project database"
	echo "  clean        Removes all temporary files"
	echo "  serve        Runs the Django development server on port 8000"
	echo "  prod_serve   Runs Daphne server on port 8000"
	echo "  freeze       save package versions in requirments.txt"
	echo ""


# deletes all temporary files created by Django
clean:
	find . -iname "*.pyc" -delete
	find . -iname "__pycache__" -delete


prod_serve:
	daphne example.asgi:application

serve:
	./manage.py runserver

freeze:
	pip freeze > ./requirements.txt

init_db:
	./manage.py migrate
	./manage.py loaddata scores

update_pip:
	pip install -r ./requirements.txt

