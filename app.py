# app.py
from flask import Flask
from config.config import Config
from database.db import db
from routes import register_blueprints

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
