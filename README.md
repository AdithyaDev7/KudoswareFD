# KudoswareFD

#Follow these Steps before starting the project:

pip install virtualenvwrapper-win
mkvirtualenv myenv
pip install Django
django-admin startproject FullStack
cd FullStack
python manage.py startapp app1


#in settings.py
INSTALLED_APPS=['app1]


#To execute
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py runserver