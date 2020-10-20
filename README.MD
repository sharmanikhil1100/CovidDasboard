django-admin startproject dashboard
python manage.py startapp covid

sudo docker run --name postgres_d -d -p 5432:5432 -e POSTGRES_USER=nik -e POSTGRES_PASSWORD=nikgreat -e POSTGRES_DB=covidDb postgres

python3 manage.py makemigrations
python3 manage.py makemigrations covid
python3 manage.py migrate
python3 manage.py runserver
