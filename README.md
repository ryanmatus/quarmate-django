# Quarmate <3 Backend using Django REST Framework

# Folders/Files

-ObjectAPI: Code for the models, serializers, and views of the constructed backend.

-QuarmateAPI: Contains manage.py for the models to encapsulate entire backend project.

# Instructions

A. Setting up Python Virtual Environment and Django

1. After pulling from the main, open a command terminal into the project folder.
2. For Windows, type 'pip install -m venv' to install the virtual environment module onto your machine.
3. Create the virtual environment by typing 'virtualenv NAME'. Then, type '.\NAME\Scripts\activate' to activate it. 
4. Install Django and the REST Django component via the commands 'pip install django' and 'pip install djangorestframework'. 
5. Edit/add to the code in this environment.

B. Setting up the Server

1. Install python if you don't already have it.
2. Run `python3 manage.py migrate` to create the models.
3. Add yourself as a admin user using `python3 manage.py createsuperuser`.
4. Run `python3 manage.py runserver` to start the development server and visit http://127.0.0.1:8000/admin/. 
5. Log in with the credentials you have just created.

C. Making Changes to any of the files in the ObjectAPI folder

1. Activate your virtual environment via '.\NAME\Scripts\activate' from the command terminal.
2. Run 'python3 manage.py makemigrations' to make sure the changes are made to the database and backend scheme.
3. Run 'python3 manage.py migrate' to complete the changes.
4. Run `python3 manage.py runserver` to check proper implementation and continue development.
