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

# python shell
python manage.py shell

# get all the objects of a model
Model.objects.all()
Model.objects.all().values()   # print out the details of each objects

# CRUD operation
# Create a object of a model (C)
Model.objects.create(name = "name_of_task", desceription="description of task", status=True, field = ".....",....)
Todolist.objects.create(name = "name_of_task", desceription="description of task", status=True)

# fetch single data (R)
a = Model.objects.get(id = 1)   # any field that is unique can be used instead of id
a = Todolist.objects.get(id = 1)

a.model_ma_vako_field   # the values of that field
a.status
a.name

# Update a the data (U)
a.model_ma_vako_field = "new_value"
a.save()   # save the changes

a.status = True
a.save()

# Delete a data (D)
a.delete()

# Fiter the data
Model.objects.filter(field1 = "values",field2 = "values")
Todolist.objects.filter(name = "Task", status = True)