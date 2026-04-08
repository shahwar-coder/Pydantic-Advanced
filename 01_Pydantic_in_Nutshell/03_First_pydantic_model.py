import pydantic

# print(pydantic.VERSION) # 2.12.5

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

user = User(name="Rahul", age=54, email="rahul@gmail.com")

print(f"User Object : {user}")
print(f"User Name : {user.name}")
print(f"User Age : {user.age}")
print(f"User Email : {user.email}")


# User Object : name='Rahul' age=54 email='rahul@gmail.com'
# User Name : Rahul
# User Age : 54
# User Email : rahul@gmail.com