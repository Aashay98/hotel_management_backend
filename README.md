# hotel_management_backend
Steps to set up the project
Prequsite:-
1. install python > 3.9
2. install mongodb
3. Use vscode or pycharm as code editor

For windows
1. pip install virtualenv
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. to run the application:- flask --app api run --debug

Create migrations:
Note:- Migrations are needed to create data or edit or delete columns in the database
alley migrations create <name>
alley migrations create room_type
