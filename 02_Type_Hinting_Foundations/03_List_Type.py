from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str
    hobbies: List[str]


# ✅ Valid
user = User(name="Rahul", hobbies=["cricket", "coding"])
print(user)

# ❌ Invalid
user = User(name="Rahul", hobbies="cricket")  # not a list