from flask import Flask, current_app
from flask_restful import Api, Resource

from config import run_config
from db import db

from create_db import create_db
from rooms import room
from staff import staff
from tenants import tenant


def create_app():
  app = Flask(__name__)
  app.config.from_object(run_config())
  db.init_app(app)

  app.register_blueprint(room)
  app.register_blueprint(create_db)
  app.register_blueprint(tenant)
  app.register_blueprint(staff)

  return app



if __name__ == '__main__':
    create_app().run(debug=True)
