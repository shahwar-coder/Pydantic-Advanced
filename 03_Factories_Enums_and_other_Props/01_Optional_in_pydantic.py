from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    nickname: Optional[str]


# ✅ Works
user1 = User(name="Rahul", nickname="R")
print(user1)

# ✅ Works (None allowed)
user2 = User(name="Rahul", nickname=None)
print(user2)