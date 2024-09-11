# Flask Application Structure
--------------------------------------------------------------------------------------------
/your app
    /app.py
    /config.py
    /app
        /__init__.py
        /views.py
        /models.py
        /static/
            /main.css
       /templates/
            /home.html
       /requirements.txt
       /your appenv
-------------------------------------------------------------------------------------------
# app.py contains the actual python code that will import the app and start development server.
# config.py - store configuration for your app
# __init__.py - initialize your application creating a Flask app instance
# views.py this is where routes are defined
# models.py - This is where you define models for your application
# static - contains static files i.e css, javascript, images.
# templates - this is where you store html templates i.e. index.html, home.html
# requirements.txt - This is where you store your packages dependencies, you can use pip
# your appenv - your virtual environment for development