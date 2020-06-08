# team_app

A project related to Teams and Players.

Database Used: MySql

Provided: mysql wheel inside src folder.

Steps for installing the repository:-

Download the repository.

Steps:

After downloading, Goto team_app folder and run: pip3 install -r requirements.txt

After installing all the dependencies, create virtual environment called "venv".

After this, run : python manage.py migrate

Run: python manage.py runserver

open http://127.0.0.1:8000

Additional RestFul API :-

There are Two Api's in this project:

##############################################################################################

First api: http://127.0.0.1:8000/team/api/teams/list/

Request: GET

This api returns the teams list

##############################################################################################

Second api: http://127.0.0.1:8000/team/api/details/chennai-super-kings/

Request: GET

This api returns the team detail and Players list of the team

##############################################################################################
