from flask import Flask, current_app
from flask_restful import Api, Resource

from config import run_config
from hotel import rooms, tenants, staff

app = Flask(__name__)
api = Api(app)

app.config.from_object(run_config())
app.register_blueprint(rooms.room)
app.register_blueprint(tenants.tenant)
app.register_blueprint(staff.staff)


if __name__ == '__main__':
    app.run(debug=True)
