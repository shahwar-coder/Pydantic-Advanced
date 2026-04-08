from pydantic import BaseModel
from typing import List

class Matrix(BaseModel):
    values: List[List[int]]


# ✅ Valid input
matrix = Matrix(values=[[1, 2], [3, 4]])
print(matrix)