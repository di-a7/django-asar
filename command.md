# install virtual environment
pip install virtualenv

# create virtual environment
virtualenv env (or)
python -m venv env

# activate virtual environment
env\Scripts\activate(pw, cmd)
source env\Scripts\activate (mac)
source env/bin/activate  (linux)

# install django
pip install django

# start project 
django-admin startproject project  .  (. is optional)

# server start
python manage.py runserver

# create app
python manage.py startapp app_name

# migrations file
python manage.py makemigrations

# migrate the table
python manage.py migrate