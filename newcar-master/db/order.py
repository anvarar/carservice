import enum
from dataclasses import dataclass


class CustomerType(enum.Enum):
    Normal = "Normal"
    Regular = "Normal"


@dataclass
class CarOrder:
    order_id: int
    car_id: int
    user_id: int
    """
    fill up the remaining details like discount, price, quantity, user_info etc..
    
    """
