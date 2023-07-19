# LAB - Class 33

Project: Lab: Authentication & Production Server
Author: Anas Alsallak

## Setup

    1. create a venv using python -m venv .venv
    2. activate it : source .venv/bin/activate and when done deactivate
    
    3. install requirments usnig : pip install -r requirement.txt

    - How to initialize/run your application (where applicable)
        python manage.py runserver
    - To run the docker container:
        1. You need to instal docker if you do not have one.
        2. run sudo docker build . -t <name>:tag in your terminal
        3. run sudo docker compose up to run the image instance
        4. docker compose run web python manage.py (createsuperuser,migrate,...) in a 2nd terminal

     - Tests
    How do you run tests?
    1. in the terminal run : python manage.py test
