from pydantic import BaseModel, StrictInt, StrictStr, StrictBool

class User(BaseModel):
    age: StrictInt
    name: StrictStr
    is_active: StrictBool


# ✅ Valid input
user1 = User(age=25, name="Rahul", is_active=True)
print(user1)


# ❌ Invalid inputs
user2 = User(age="25", name=123, is_active="yes")