from pydantic import BaseModel, field_validator
from typing import List

class Matrix(BaseModel):
    values: List[List[int]]

    @field_validator("values")
    @classmethod
    def validate_matrix(cls, v):
        # ❌ Empty matrix check
        if not v:
            raise ValueError("Matrix cannot be empty")

        # ❌ Empty row check
        if any(len(row) == 0 for row in v):
            raise ValueError("Rows cannot be empty")

        # ❌ All rows must have same length
        row_length = len(v[0])
        if any(len(row) != row_length for row in v):
            raise ValueError("All rows must have same number of columns")

        return v


# ✅ Valid
matrix = Matrix(values=[[1, 2], [3, 4]])
print(matrix)


# ❌ Invalid (uneven rows)
matrix = Matrix(values=[[1, 2], [3]])