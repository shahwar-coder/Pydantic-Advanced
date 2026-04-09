from pydantic import BaseModel, Field

from typing import List

class Data(BaseModel):
    values: List[int] = Field(min_length=1, max_length=3)

Data(values=[1, 2])      # ✅
Data(values=[])          # ❌ too short