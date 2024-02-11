# A script that creates the database used in application.py (source: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/contexts/)

from application import (db, app)

with app.app_context():
    db.create_all()