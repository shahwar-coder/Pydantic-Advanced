from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    addresses: List[Address]


user = User(
    name="Rahul",
    addresses=[
        {"city": "Delhi", "pincode": 110001},
        {"city": "Mumbai", "pincode": 400001}
    ]
)

print(user)