import json

from sqlalchemy import text

from db1.entity.car import Car
from db1.entity.user import User


class CarData:

    def __init__(self, session):
        self.session = session

    def get_cars_by_filter(self,key,value):
        # with open('dataset/users.json', 'r') as f:
        #     car = json.load(f)
        #     return car

        # Query for Car objects matching the filter condition
       car_data= self.session.query(Car).filter(getattr(Car, key) == value).all()
       return car_data

    def create_car(self, card_data: dict):
        # with open('dataset/vehicle.json', 'r') as f:
        #     data = json.load(f)
        #     data.append(card_data)
        # with open('dataset/vehicle.json', 'w') as f:
        #     json.dump(data, f, indent=4)
        car_obj = Car(ad_id=card_data['ad_id'],
                      origin=card_data['origin'],
                      condition=card_data['condition'],
                      car_model=card_data['car_model'],
                      exterior_color=card_data['exterior_color'],
                      interior_color=card_data['interior_color'],
                      num_of_doors=card_data['num_of_doors'],
                      seating_capacity=card_data['seating_capacity'],
                      engine=card_data['engine'],
                      fuel_system=card_data['fuel_system'],
                      distance=card_data['distance'],
                      price=card_data['price'],
                      year_of_built=card_data['year_of_built'],
                      vehicle_number=card_data['vehicle_number'])

        self.session.add(car_obj)


    def get_car_by_id(self, ad_id: int):
        # car=query(Car).filter_by(ad_id=ad_id).first()
        # return car
        # with open('dataset/orders.json', 'r') as f:
        #     data = json.load(f)
        #     for car in data:
        #         if car.get("ad_id") == ad_id:
        #             return car
        value=self.session.query(Car).filter_by(ad_id=ad_id).first()
        print(value)
        return value
    def delete_car_by_id(self, ad_id: int):
        # with open('dataset/vehicle.json', 'r') as f:
        #     data = json.load(f)
        #
        # for car in data:
        #     if car.get("ad_id") == ad_id:
        #         data.remove(car)
        #         break
        self.session.query(Car).filter_by(ad_id=ad_id).delete()

        # with open('dataset/vehicle.json', 'w') as f:
        #     json.dump(data, f, indent=4)

    def predict_avg_car_price(self, properties) -> int:
        value = self.session.query(Car).all()
        return value
        # with open('dataset/vehicle.json', 'r') as f:
        #     data = json.load(f)
        #     return data

    def get_user_details(self,ad_id):
        try:
            user_obj = self.session.query(User).filter_by(user_id=ad_id).first()
            if user_obj is None:
                raise ValueError("no data found!!!")
            return user_obj
        except ValueError as e:
            return {"error":str(e)}
        except Exception as e:
            return {"error":str(e)}

        # print(user.user_type)
        # return user
