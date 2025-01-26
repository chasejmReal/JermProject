## SETUP DJANGO (for Windows) ##
1. Open up terminal enviroment 

2. type:
python --version
Do this because you need to ensure you have python installed on your machine

3. type: 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3. type (not needed): 
.\myenv\Scripts\activate
only needed when you need an enviroment created

4. type: 
pip install django

5. type: 
cd src

6. type: 
python manage.py migrate

7. type (if needed): 
python manage.py runserver


