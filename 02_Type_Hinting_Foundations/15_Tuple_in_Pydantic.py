from pydantic import BaseModel, ValidationError
from typing import Tuple


class Coordinates(BaseModel):
    point: Tuple[int, int]


# ✅ Valid
data = Coordinates(point=(10, 20))
print("✅ Output:", data)


# ❌ Invalid (wrong size)
data = Coordinates(point=(10, 20, 30))