from pydantic import BaseModel
from typing import Any


class Data(BaseModel):
    value: Any


# ✅ All valid
d1 = Data(value=123)
d2 = Data(value="hello")
d3 = Data(value=[1, 2, 3])
d4 = Data(value={"a": 1})

print(d1, d2, d3, d4)