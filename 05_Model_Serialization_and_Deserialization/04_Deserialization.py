from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int


# dict → model
user1 = User.model_validate({"name": "Rahul", "age": "25"})

# JSON → model
user2 = User.model_validate_json('{"name": "Ali", "age": 30}')

print(user1)
print(user2)