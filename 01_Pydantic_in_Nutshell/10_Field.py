from pydantic import BaseModel, Field, EmailStr, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(strict=True)

    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=18, le=120)
    email: EmailStr