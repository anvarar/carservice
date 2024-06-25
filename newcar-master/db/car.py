import enum
from dataclasses import dataclass


class Origin(enum.Enum):
    DOMESTIC_ASSEMBLY = "DOMESTIC_ASSEMBLY"
    Imported = "Imported"


class CarCondition(enum.Enum):
    NEW_CAR = "New Car"
    USED_CAR = "Used Car"


class CarModel(enum.Enum):
    Truck = "Truck"
    SUV = "SUV"
    Crossover = "Crossover"
    Sedan = "Sedan"
    Hatchback = "Hatchback"
    Wagon = "Wagon"
    Coupe = "Coupe"


class EngineType(enum.Enum):
    Petrol = "Petrol"
    Diesel = "Diesel"
    Hybrid = "Hybrid"
    Electric = "Electric"


@dataclass
class Car:
    ad_id: int
    origin: Origin
    condition: CarCondition
    car_model: CarModel
    distance: int
    exterior_color: str
    interior_color: str
    num_of_doors: int
    seating_capacity: int
    engine_type: EngineType
    year_of_built: int

#
# data = [{"ad_id": 1, "origin": "Imported"}]
# objs = []
# for i in data:
#     car_obj = Car(
#         ad_id=i["ad_id"],
#         origin=getattr(Origin, i["origin"])
#         #origin=i["origin"]
#     )
#     objs.append(car_obj)
#
# for i in objs:
#     print(i.origin.name)