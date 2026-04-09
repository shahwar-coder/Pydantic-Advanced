from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(...)

user = User(name="Rahul")  # ✅ required

# 👉 ... means: must be provided