from pydantic import BaseModel, field_validator

class User(BaseModel):
    age: int

    @field_validator("age")
    @classmethod
    def check_age(cls, v):
        if v < 0:
            raise ValueError("Age must be positive")
        return v


'''
📌 PURPOSE
Validates a single field using @field_validator

📌 CORE
@field_validator("age")
→ Custom validation for "age" field

======================
📌 EXECUTION FLOW
======================

Input: age = value

STEP 1:
Type validation → must be int ✔

STEP 2:
Custom validator runs

if v < 0:
→ ❌ raises ValueError

else:
→ returns value ✔

======================
📌 BEHAVIOR
======================

age = 10 → ✔ valid  
age = -5 → ❌ error ("Age must be positive")

======================
📌 TAKEAWAYS
======================

✔ Used for field-level custom rules  
✔ Runs after type validation  
✔ Must return the validated value  

'''