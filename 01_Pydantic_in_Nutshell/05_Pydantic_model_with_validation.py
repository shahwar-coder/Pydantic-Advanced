import pydantic

# print(pydantic.VERSION) # 2.12.5

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

try:
    user = User(name="Rahul", age="fifty-four", email="rahul@gmail.com")
except pydantic.ValidationError as err:
    print(f"Error : {err}")

print(f"User Object : {user}")
print(f"User Name : {user.name}")
print(f"User Age : {user.age}")
print(f"User Email : {user.email}")

# We can capture in more ways eg...logs etc.