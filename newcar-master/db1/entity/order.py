from sqlalchemy import Column, Integer, Float, String

from data import Base


class Car(Base):
    __tablename__ = 'carorder'
    order_id=Column(Integer)
    car_id=Column(Integer)
    user_id= Column(Integer)
    price =Column(Float)
    discount =Column(String(5))
    quantity =Column(Integer)
    user_type =Column(String(10))
