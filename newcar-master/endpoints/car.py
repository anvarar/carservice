import json

from flask import request
from flask_restx import Resource
from actions.car import CarAction
from db_factory import get_db_session
from endpoints.namespace import car
from model.car_model import car_model
from model.avg_price import avg
from model.filter import filter

# to predict the avg price of a car based on some properties
@car.route("/predict")
class Avg(Resource):
    @car.expect(avg)
    def post(self):
        session = get_db_session()
        car_obj = CarAction(session)
        data = [car.payload]
        result = car_obj.predict_avg_car_price(data)
        return f"average price is:{result}"


# to create/post new car
@car.route("/create_car")
class CreateCar(Resource):
    @car.expect(car_model)
    def post(self):
        session = get_db_session()
        car_obj = CarAction(session=session)
        new_car = car.payload
        create_obj = car_obj.create_car(new_car)
        session.commit()
        return "Data Entered into the Database Successfully!!!"


# #get a car based on tha id
@car.route("/get_car_by_id/<int:id1>")
class ReadCarData(Resource):
    def get(self, id1):
        session = get_db_session()
        car_obj = CarAction(session)
        value = car_obj.get_car_by_id(id1)
        if value is None:
            return {"message": "Car not found"}
        else:
            return value


# #delete a car based on the id
@car.route("/delete/<int:data>")
class DeleteCar(Resource):
    def delete(self, data):
        session = get_db_session()
        car_obj = CarAction(session)
        value = car_obj.delete_car_by_id(data)
        session.commit()
        return value


# #filter cars based on some properties
@car.route("/filter")
class FilterCar(Resource):
    @car.expect(filter)
    def post(self):
        session = get_db_session()
        car_obj = CarAction(session)
        filters = [car.payload]
        value = car_obj.get_cars_by_filter(filters)
        return value


# #showing various properties of a car based on customer type
@car.route("/check_customertype/<int:ad_id>/<int:car_id>")
class CustomerType(Resource):
    def get(self, ad_id,car_id):
        session =get_db_session()
        car_obj =CarAction(session)
        data= car_obj.get_user_details(ad_id,car_id)
        return data

@car.route("/update/<int:id>")
class Update(Resource,id):
    def put(self,id):
        data=request.json
        session = get_db_session()
        car_obj =CarAction(session)
        updated_data=car_obj.car_data.update_car_data(ad_id,data)
        session.commit()
        return "updated Successfully!!!"
