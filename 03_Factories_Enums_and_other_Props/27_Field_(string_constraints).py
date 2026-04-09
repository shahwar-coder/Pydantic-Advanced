from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=3, max_length=10)

User(name="Rahul")  # ✅
User(name="Ra")     # ❌ too short