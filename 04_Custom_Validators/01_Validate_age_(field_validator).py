from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    name: str
    age: int = Field(..., gt=0, le=30)

    @field_validator("age")
    @classmethod
    def validate_age(cls, v):
        if v<18 and v%2!=0:
            raise ValueError("If age is less than 18, it must be even")
        return v

user = User(name="Rahul", age=25)



'''
📌 PURPOSE
Combines built-in validation (Field) + custom validation (@field_validator)

📌 CORE
age: int = Field(..., gt=0, le=30)
→ Age must be:
   > 0 and ≤ 30

@field_validator("age")
→ Runs AFTER Field validation

======================
📌 EXECUTION FLOW
======================

Input: age=25

STEP 1: Field validation
→ 25 > 0 ✔
→ 25 ≤ 30 ✔

STEP 2: Custom validator runs
if v < 18 and v % 2 != 0:
→ 25 < 18 ❌ → condition false → passes

→ Final: Model created ✔

======================
📌 VALIDATOR LOGIC
======================

Condition:
if age < 18 AND odd → ❌ error

So:
- age < 18 → must be EVEN
- age ≥ 18 → no restriction

======================
📌 KEY TAKEAWAYS
======================

✔ Field handles basic constraints  
✔ @field_validator handles custom logic  
✔ Runs in order: Field → Validator  

'''