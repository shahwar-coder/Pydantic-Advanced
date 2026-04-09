from pydantic import BaseModel, Field

class User(BaseModel):
    age: int = Field(default=18)

print(User())  # age=18