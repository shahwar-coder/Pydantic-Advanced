from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(alias="user_name")

user = User(user_name="Rahul")
print(user.name)