from flask import Flask

from db_factory import init_db
from endpoints import car_


def create_app():
    app = Flask(__name__)
    app.register_blueprint(car_)
    return app


if __name__ == '__main__':
    app = create_app()
    init_db()
    app.run(debug=True)
