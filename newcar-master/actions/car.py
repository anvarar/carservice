from data.car import CarData


class CarAction:
    def __init__(self, session):
        self.session = session
        self.car_data = CarData(session)

    def get_user_details(self, ad_id: int, car_id: int):
        user = self.car_data.get_user_details(ad_id)
        print(user.usertype)
        if user.usertype == "Prime":
            print("helloo")
            car_data = self.car_data.get_car_by_id(car_id)
            return [{
                    'ad_id': car_data.ad_id,
                    'origin': car_data.origin,
                    'condition': car_data.condition,
                    'car_model': car_data.car_model,
                    'exterior_color': car_data.exterior_color,
                    'num_of_doors': car_data.num_of_doors,
                    'seating_capacity': car_data.seating_capacity,
                    'engine': car_data.engine,
                    'fuel_system': car_data.fuel_system,
                    'distance': car_data.distance,
                    'price': car_data.price,
                    'year_of_built': car_data.year_of_built,
                    'vehicle_number': car_data.vehicle_number
            }]
        else:
            car_data = self.car_data.get_car_by_id(car_id)
            return [{
                'ad_id': car_data.ad_id,
                'origin': car_data.origin,
                'condition': car_data.condition,
                'car_model': car_data.car_model,
                'exterior_color': car_data.exterior_color,
                'num_of_doors': car_data.num_of_doors,
                'seating_capacity': car_data.seating_capacity,
                'engine': car_data.engine,
                'fuel_system': car_data.fuel_system,
                'distance': car_data.distance,
                'price': car_data.price,
                'year_of_built': car_data.year_of_built

          }]


        # with open('dataset/users.json', 'r') as f:
        #     data = json.load(f)
        # for x in data:
        #     print(x)
        #     if x['user'] == user and x['ad_id'] == ad_id:
        #         return x
        #     elif x['user'] == "Normal" and x['ad_id'] == ad_id:
        #         print(x['user'])
        #         print(x['ad_id'])
        #         x.pop('vehicle_number')
        #         return x

    def get_cars_by_filter(self, filters: list[dict]) -> list:
        for x in filters:
            key = x['key']
            value = x['value']
            filtered_car = self.car_data.get_cars_by_filter(key,value)
            l2=[]
            for car_data in filtered_car:

                l1={'ad_id': car_data.ad_id,
                'origin': car_data.origin,
                'condition': car_data.condition,
                'car_model': car_data.car_model,
                'exterior_color': car_data.exterior_color,
                'num_of_doors': car_data.num_of_doors,
                'seating_capacity': car_data.seating_capacity,
                'engine': car_data.engine,
                'fuel_system': car_data.fuel_system,
                'distance': car_data.distance,
                'price': car_data.price,
                'year_of_built': car_data.year_of_built}
                l2.append(l1)
            return l2
            # filtered_car = [car for car in filtered_car if  getattr(car, key) == value]



    def create_car(self, card_data: dict):
        return self.car_data.create_car(card_data)

    def get_car_by_id(self, ad_id1: str):
        vehicle= self.car_data.get_car_by_id(ad_id1)
        l=[{"ad_id":vehicle.ad_id,
            "origin":vehicle.origin,
            "condition":vehicle.condition,
            "car_model":vehicle.car_model,
            "exterior_color":vehicle.exterior_color,
            "interior_color":vehicle.interior_color,
            "num_of_doors":vehicle.num_of_doors,
            "seating_capacity":vehicle.seating_capacity,
            "engine":vehicle.engine,
            "fuel_system":vehicle.fuel_system,
            "distance":vehicle.distance,
            "price":vehicle.price,
            "year_of_built":vehicle.year_of_built,
            "vehicle_number":vehicle.vehicle_number}
           ]
        return l

    def delete_car_by_id(self, ad_id: int):
        delete_car = self.car_data.delete_car_by_id(ad_id)
        if delete_car is None:
            return "Successfully Deleted!!!"
        else:
            return "Failed to Delete,Something Wrong!"

    # def get_cars_by_user(self,filters: list[dict]) -> list:
    #     print(filters)
    #     print(filters[0]['key'])
    #     with open('dataset/users.json','r') as f:
    #         data = json.load(f)
    #     for x in data:
    #         if filters[0]['user'] == 'Prime':
    #             return x
    def predict_avg_car_price(self, properties) -> int:
        values = self.car_data.predict_avg_car_price(properties)
        matched_prices = []
        for car in properties:
            condition = car['condition']
            car_model = car['car_model']
            engine = car['engine']
            year_of_built = car['year_of_built']
            filtered_values = [x.price for x in values
                               if x.condition == condition
                               and x.car_model == car_model
                               and x.engine == engine
                               and x.year_of_built == year_of_built]
            matched_prices.extend(filtered_values)

        if matched_prices:
            avg_price = sum(matched_prices) / len(matched_prices)
            return avg_price
        else:
            return "no car is found with the specified specification"


    def update_car_data(self,ad_id,data):
        car=self.car_data.get_car_by_id(ad_id)
        if car:
            for key,value in data.items():
                setattr(car, key, value)
            return car

