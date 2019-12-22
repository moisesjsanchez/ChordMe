import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ChordMe.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    
    from ChordMe.user.routes import user
    app.register_blueprint(user)
    #from ChordMe.error.handlers import error
    #from ChordMe.service.routes import routes

    return app
