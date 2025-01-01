## Helpful Commands ## 

python manage.py runserver
#   FUNCTION: runs the server 
#   you can exit by pressing CTRL+C 


python manage.py show_urls
#   FUNCTION: see all the urls within the project
#   shows the urls. (needs extension to run though)


.\myenv\Scripts\activate
#   FUNCTION: enter django enviroment 
#   Use when need to run django commands


python manage.py migrate
#   FUNCTION: enter django enviroment
#   Use if need to make migrations



# HOW TO: start a django project
django-admin startproject NAME_OF_PROJECT
    *this must be done within the django enviroment and with it installed. 

# HOW TO: create an app within django
python manage.py startapp NAME_OF_APP
    *creates an app for django

# HOW TO: apply migrations 
python manage.py migrate
    *apply any migrations 

# HOW TO: create a super user 
python manage.py createsuperuser
    *creates a superuser
    * my account
    -Username = 
    -Password = 
