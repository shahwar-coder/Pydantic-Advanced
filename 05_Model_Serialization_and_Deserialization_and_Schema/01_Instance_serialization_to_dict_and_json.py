from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    name: str
    age: int
    created_at: datetime


user = User(name="Rahul", age=25, created_at="2026-04-10T10:30:00")

print("Model instance:", user)

# 🔹 Convert to dict
user_dict = user.model_dump()
print("\nAs dict:", user_dict)

# 🔹 Convert to JSON
user_json = user.model_dump_json()
print("\nAs JSON:", user_json)


# As dict: {'name': 'Rahul', 'age': 25, 'created_at': datetime.datetime(2026, 4, 10, 10, 30)}
# As JSON: {"name":"Rahul","age":25,"created_at":"2026-04-10T10:30:00"}