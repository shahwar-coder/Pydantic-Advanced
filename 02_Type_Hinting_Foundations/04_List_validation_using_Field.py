from pydantic import BaseModel, Field
from typing import List

class User(BaseModel):
    hobbies: List[str] = Field(min_length=1, max_length=5)