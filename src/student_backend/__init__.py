import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():
    """ flask app factory """

    # define app
    app = Flask(__name__)

    # initialize settings
    base_path = os.path.dirname(os.path.realpath(__file__))
    default = os.path.join(base_path, "configs", "local.cfg")
    config_file = os.getenv("STUDENT_BACKEND_SETTINGS", default)
    app.config.from_pyfile(config_file)

    # # Initialize students_backend log files
    # flask_log_file = os.path.join(app.config["LOG_DIR"], "flask.app.log")
    # flask_log_handler = RotatingFileHandler(
    #     flask_log_file,
    #     maxBytes=app.config["LOG_MAX_BYTES"],
    #     backupCount=app.config["LOG_BACKUP_COUNT"]
    # )
    # flask_log_handler.setLevel(app.config["LOG_LEVEL"])
    # app.logger.addHandler(flask_log_handler)

    # import models
    from .student.models import db as student_db

    # initialize models
    student_db.init_app(app)

    db = SQLAlchemy(app)
    Migrate(app, db)

    @app.route("/")
    def index():
        return render_template('home.html')

    return app
