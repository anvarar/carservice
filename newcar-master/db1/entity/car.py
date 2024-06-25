from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import validates
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Car(Base):
    __tablename__ = 'car'
    ad_id = Column(Integer, primary_key=True)
    origin = Column(String(20))
    condition = Column(String(20))
    car_model = Column(String(20))
    exterior_color = Column(String(20))
    interior_color = Column(String(20))
    num_of_doors = Column(Integer)
    seating_capacity = Column(Integer)
    engine = Column(String(20))
    fuel_system = Column(String(20))
    distance = Column(Float(20))
    price = Column(Float(20))
    year_of_built = Column(Integer)
    vehicle_number = Column(String(50))


CONDITION = ("New Car", "Used Car")


@validates('condition')
def validate_origin(self, value):
    if value not in self.CONDITION:
        raise ValueError
    else:
        value
