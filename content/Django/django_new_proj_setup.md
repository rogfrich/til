# Setting up a new Django project

1. Set up working folder
1. Create venv
1. `pip install django`
1. `django-admin startproject <name> .` (note the period - use this to create the project in the working directory and not a subfolder)
1. `python manage.py migrate`
1. `python manage.py startapp <name>`
1. Add `appname.apps.AppnameConfig` to `INSTALLED_APPS` in `settings.py` (replace appname with the name of the app)