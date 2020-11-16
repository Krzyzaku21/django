#connect virtual django venv - (virtual_django_venv)
# ? cd C:\Users\Krzyz\Desktop\Radek Python\Django_Folder\virtual_django_venv\Scripts>activate
#go to git folder
# ? cd C:\Users\Krzyz\Desktop\Radek Python\Git_Folder\_python_base_code\django
#create project
# ? django-admin.exe startproject my_site_name .
# ! edycja settings.py w pliku my_site_name/settings.py
"""
TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'pl-pl'
import os
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage' #na dole kodu
#inicjalizacja bazy danych sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
#inicjalizacja bazy danych
# ? python manage.py migrate
#uruchomienie projektu // przerwanie ctrl+break+fn guzik
# ? python manage.py runserver
#tworzenie aplikacji
# ? python manage.py startapp my_project_name
# ! dodajemy aplikacje w pliku my_site_name/settings.py INSTALLED_APPS
"""
INSTALLED_APPS = [
    'my_project_name',
]
"""
#tworzymy model w my_project_name/models.py
# ? piszemy model w my_project_name/models.py
# !wywołujemy makemigrations i migrate za każdym razem gdy tworzymy model
#tworymy tabele dla modeli w bazie danych
# ? python manage.py makemigrations my_project_name
# ? python manage.py migrate my_project_name
#tworzymy panel administracji dla utworzonego modelu my_project_name w pliku my_project_name/admin.py
"""
from django.contrib import admin
from .models import NazwaKlasyModelu

admin.site.register(NazwaKlasyModelu)
"""
# tworzenie konta administratora
# ? python manage.py createsuperuser
# logowanie do servera
# ? python manage.py runserver
# adres administratora strony
# todo http://127.0.0.1:8000/admin/.
# wdrażanie 
