from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate, MigrateCommand
from ChordMe.config import Config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from ChordMe.user.routes import user
    app.register_blueprint(user)
    from ChordMe.auth.routes import auth
    app.register_blueprint(auth)
    CORS(app)
    # from ChordMe.error.handlers import error
    # from ChordMe.service.routes import routes

    return app
