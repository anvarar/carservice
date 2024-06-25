from sqlalchemy import Column, Integer,String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer,primary_key=True)
    username= Column(String(50))
    usertype=Column(String(10))
    phonenumber=Column(String(10))


