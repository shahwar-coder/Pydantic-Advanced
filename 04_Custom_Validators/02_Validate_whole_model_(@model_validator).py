from pydantic import BaseModel, model_validator

class User(BaseModel):
    age: int
    name: str

    @model_validator(mode="after")
    def check_user(self):
        if self.name == "Admin" and self.age < 18:
            raise ValueError("Admin must be 18+")
        return self


'''
📌 PURPOSE
Applies cross-field validation using @model_validator

📌 CORE
@model_validator(mode="after")
→ Runs after all fields are validated
→ Access to full object (self)

======================
📌 EXECUTION FLOW
======================

Input: User(age=..., name=...)

STEP 1:
Field validation
→ age is int ✔
→ name is str ✔

STEP 2:
Model validator runs

Condition:
if name == "Admin" AND age < 18
→ ❌ raise ValueError

else:
→ ✔ valid

======================
📌 BEHAVIOR
======================

("Admin", 17) → ❌ error  
("Admin", 18) → ✔ valid  
("Rahul", 10) → ✔ valid  

======================
📌 TAKEAWAYS
======================

✔ model_validator is for multi-field logic  
✔ Runs after field validation  
✔ Must return self  

'''