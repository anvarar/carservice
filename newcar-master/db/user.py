import enum
from dataclasses import dataclass


class CustomerType(enum.Enum):
    Normal = "Normal"
    PRIME = "PRIME"


@dataclass
class User:
    user_id: str
    username: str
    """
    fill up the basic user details
    """
