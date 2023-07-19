# Course Allocation System (OARS)

This is a course allocation system where registered students may request available courses and 
professors can offer courses and can optionally define filters and preferences to automatically accept or reject.

## Tech
This project is built using a number of open source projects.

- [Django framework](https://www.djangoproject.com/)
- [Twitter Bootstrap](http://getbootstrap.com/)
- [AdminLTE template](http://almsaeedstudio.com/AdminLTE/)
- [Grappelli admin interface](http://grappelliproject.com/)

## Setup

1. Install [Python 3.x](https://www.python.org/downloads/)
2. Install [Django 1.7](https://docs.djangoproject.com/en/1.7/intro/install/)
3. Download the code
4. cd to the project directory
5. run the following command  `python3 manage.py runserver`
6. Done!

## Site map

After installation, you can view the website at [http://localhost:8000/](http://localhost:8000/)

URL configuration (relative path):

- admin: [/admin](http://localhost:8000/admin/)
- login: [/auth/login](http://localhost:8000/login/)
- logout: [/logout](http://localhost:8000/logout/)
- password reset: [/password_reset](http://localhost:8000/password_reset/)
- password change: [/password_change*](http://localhost:8000/password_change/)
- student: [/student](http://localhost:8000/student/)
- professor: [/professor](http://localhost:8000/professor/)
- dugc: [/dugc](http://localhost:8000/dugc/)

Other facilities can be explored easily using the interface once you are logged in.

## Initial settings

### Site email

- email: oars.django@gmail.com
