
# pip install --upgrade --force-reinstall
# todo CTRL + F5- W Chrome przy update czegokolwiek bypass - odświerzanie chrome przeglądarki
# ! /////////////////////////////////////////// ODPALANIE MASZYNY WIRTUALNEJ
# konsola jeśli nie zainstalowane to środowisko wirtualne django
# ? cmd console> python3 -m venv <nazwa env>
# todo connect virtual django venv - (virtual_django_venv)
# ? cd C:\Users\Krzyz\Desktop\Radek Python\Django_Folder\virtual_django_venv\Scripts\
# ? activate
# todo leave virtual django venv - (virtual_django_venv)
# ? deactivate
# todo go to git folder
# ? cd C:\Users\Krzyz\Desktop\Radek Python\Django_Folder\django
# ! /////////////////////////////////////////// TWORZENIE DJANGO
# todo create new django project in django folder #c:\Users\Krzyz\Desktop\Radek Python\Django_Folder\django>
# ? django-admin.exe startproject <name_of_django_project>
# todo create new website aplication-project in #c:\Users\Krzyz\Desktop\Radek Python\Django_Folder\django\name_of_django_project>
# ? python manage.py startapp <name_of_app_project>
# ! /////////////////////////////////////////// ZARZĄDZANIE PRZED DODANIEM BAZY DANYCH
# ! edycja settings.py w pliku #c:\Users\Krzyz\Desktop\Radek Python\Django_Folder\django\name_of_django_project>\<name_of_django_project>\settings.py
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

"""
DATABASES connect
postgres://USER:PASSWORD@HOST:PORT/NAME, postgis://USER:PASSWORD@HOST:PORT/NAME, mssql://USER:PASSWORD@HOST:PORT/NAME, mysqlgis://USER:PASSWORD@HOST:PORT/NAME
sqlite:///PATH, spatialite:///PATH, oracle://USER:PASSWORD@HOST:PORT/NAME, oraclegis://USER:PASSWORD@HOST:PORT/NAME, redshift://USER:PASSWORD@HOST:PORT/NAME

pip install dj-database-url
import dj_database_url
DATABASES['default'] = dj_database_url.parse('mysql://root:@localhost:3306/skcms', conn_max_age=600) #mysql://USER:PASSWORD@HOST:PORT/NAME
"""
# todo inicjalizacja bazy danych in #c:\Users\Krzyz\Desktop\Radek Python\Django_Folder\django\name_of_django_project> #tam gdzie manage.py w projekcie
# ? python manage.py migrate
# uruchomienie projektu // przerwanie ctrl+break+fn guzik
# ? python manage.py runserver
# tworzenie aplikacji
# ? python manage.py startapp my_project_name
# ! dodajemy aplikacje w pliku name_of_django_project>\<name_of_django_project>/settings.py INSTALLED_APPS
"""
INSTALLED_APPS = [
    'my_project_name',
]
"""
# tworzymy model w my_project_name/models.py
# ? piszemy model w my_project_name/models.py
# !wywołujemy makemigrations i migrate za każdym razem gdy tworzymy model
# tworymy tabele dla modeli w bazie danych
# ? python manage.py makemigrations my_project_name
# ? python manage.py migrate my_project_name
# tworzymy panel administracji dla utworzonego modelu my_project_name w pliku my_project_name/admin.py
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
# ! wdrażanie respozytorium na strone www -> https://krzyzak21.pythonanywhere.com/
"""
# w katalogu Git_Folder/_python_base_code/django
Tworzenie respozytorium Git - ra tworzone na windows
"""
# ? git init
# ? git config --global user.name "Krzyzaku21"
# ? git config --global user.email krzyzak21@gmail.com
# todo Tworzneie pliku .gitignore w katalogu Git_Folder/_python_base_code/django
""".gitignore
*.pyc
*~
__pycache__
<nazwa virtualnej maszyny django> -> virtual_django_venv
<nazwa bazy danych> -> db.sqlite3
/static
.DS_Store
"""
# ? git status
# ? git add --all .
# ? git commit -m "My Django app name, first commit"
# todo Przesyłanie pliku do GitHuba
"""
-> Respository
-> Respository name <respository_git_name>
-> Create
"""
# todo wpisanie w terminalu na PC
# ? git remote add origin https://github.com/Krzyzaku21/respository_git_name.git
# ? git push -u origin master
# todo wdrażanie na pythonanywhere itd
"""
strona -> www.pythonanywhere.com
Account -> API Token -> Create API Token
consoles -> bash
odpalenie wirtualnej konsoli na stronie
"""
# ? $ pip3.6 install --user pythonanywhere
# ? $ pa_autoconfigure_django.py https://github.com/krzyzaku21/respository_git_name.git
# ? $ python manage.py createsuperuser

"""
Wysył zmian na GitHuba
git status
git add --all
git status
git commit -m "cos"
git push
Wysył zmian na pythonanywhere
cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
git pull
workon <your-pythonanywhere-domain>.pythonanywhere.com
python manage.py collectstatic
"""
# ! kopia pliku do json z danych, indent - wcięcia
# np: python manage.py dumpdata articles --indent=4 > articles.json
# ? python manage.py dumpdata appname --indent=4 > filename.json
# ! wdrażanie obiektu do bazy danych
# np: python manage.py loaddata articles.json
# ? python manage.py loaddata filename.json
