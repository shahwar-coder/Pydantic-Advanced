from pydantic import BaseModel, ValidationError
from typing import Union


class User(BaseModel):
    id: Union[int, str]


# ✅ Valid (int)
user1 = User(id=123)
print("User1:", user1)

# ✅ Valid (str)
user2 = User(id="abc123")
print("User2:", user2)


# ❌ Invalid
user3 = User(id=12.5)