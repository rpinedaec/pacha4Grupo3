python -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt
django-admin startproject ecommprj .
python manage.py startapp ecommapp
python manage.py migrate
python manage.py collectstatic
python manage.py runserver

#Para actualizar instalaciones en requirements.txt
pip freeze > requirements.txt
