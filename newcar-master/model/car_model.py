from flask_restx import fields
from endpoints.namespace import car

car_model = car.model('Car', {
    "ad_id": fields.Integer,
    "origin": fields.String,
    "condition": fields.String ,
    "car_model": fields.String ,
    "exterior_color": fields.String ,
    "interior_color": fields.String ,
    "num_of_doors": fields.Integer,
    "seating_capacity": fields.Integer,
    "engine": fields.String ,
    "fuel_system": fields.String ,
    "distance": fields.Integer,
    "price": fields.Integer,
    "year_of_built": fields.Integer,
    "vehicle_number": fields.String
})