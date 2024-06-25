from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from db1.entity.car import Base
from db1.entity.user import Base
from sqlalchemy.orm import sessionmaker


def get_engine():
    return create_engine("mysql+pymysql://root@localhost:3306/flask_api")


def get_db_session():
    return sessionmaker(autocommit=False, bind=get_engine())()


def init_db():
    Base.metadata.create_all(bind=get_engine())
