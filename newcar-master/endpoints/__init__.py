from flask_restx import Api
from flask import Blueprint

from endpoints.car import car

car_ = Blueprint("car",__name__)
api =Api(car_,title="car showroom",description="is for various car showroom activities")
api.add_namespace(car)



