from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(strict=True)

    name: str
    age: int
    email: str


# ✅ Valid
user1 = User(name="Rahul", age=25, email="rahul@gmail.com")
print(user1)


# ❌ Invalid (no conversion allowed now)
user2 = User(name=123, age="25", email=456)