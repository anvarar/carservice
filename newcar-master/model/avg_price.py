from flask_restx import fields
from endpoints.namespace import car

avg = car.model('Avg',{
    "condition": fields.String,
    "car_model": fields.String,
    "engine": fields.String,
    "year_of_built": fields.Integer,
})