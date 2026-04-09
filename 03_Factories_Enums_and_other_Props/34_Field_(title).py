from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., title="User Name")
    age: int = Field(..., title="User Age")


user = User(name="Rahul", age=25)
print(user)