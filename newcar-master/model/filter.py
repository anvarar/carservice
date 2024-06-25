from flask_restx import fields
from endpoints.namespace import car

filter = car.model('Filter', {
    "key": fields.String,
    "value": fields.String,
})