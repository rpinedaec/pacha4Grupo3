python -m venv venv
. venv/Scripts/activate
pip install -r requirements.txt
django-admin startproject ecommprj .   ---> Ya esta creada
py manage.py startapp ecommapp     ---> Ya esta creada
py manage.py migrate
py manage.py createsuperuser
python manage.py collectstatic

-----------PASOS PARA HEROKU---------------
-heroku login
-heroku create
-git push heroku "master" ---> depende la rama en la que estes localmente
-heroku ps:scale web=1
-heroku addons
-heroku addons:open (salty-ravine-56416)-----> depende el nobre que se asigno la db en el heroku, tambien aparece el nombre cuando se hizo (heroku create)
-heroku run python manage.py migrate
-heroku run python manage.py createsuperuser