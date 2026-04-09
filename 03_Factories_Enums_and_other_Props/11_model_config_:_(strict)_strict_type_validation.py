'''
model_config = the strict mode
'''

from pydantic import BaseModel, ConfigDict, ValidationError


class User(BaseModel):
    model_config = ConfigDict(strict=True)

    name: str
    age: int


# ✅ Valid
user1 = User(name="Rahul", age=25)
print("User1:", user1)


# ❌ Invalid (no type conversion allowed now)
try:
    user2 = User(name=123, age="25")
except ValidationError as e:
    print("\n❌ Error:")
    print(e)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# User1: name='Rahul' age=25

# ❌ Error:
# 2 validation errors for User
# name
#   Input should be a valid string [type=string_type, input_value=123, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_type
# age
#   Input should be a valid integer [type=int_type, input_value='25', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.12/v/int_type


'''
======================
📌 OVERALL PURPOSE
======================
Demonstrates STRICT MODE in Pydantic:
→ No automatic type coercion (conversion)

======================
📌 CORE CONCEPT
======================

model_config = ConfigDict(strict=True)

→ Enables strict validation:
   - Input must EXACTLY match declared types
   - No implicit conversions allowed

======================
📌 EXECUTION FLOW
======================

user1 = User(name="Rahul", age=25)

→ Types match:
   name → str ✔
   age → int ✔
→ Model created successfully

----------------------

user2 = User(name=123, age="25")

→ Strict mode active:

name=123
❌ int → str NOT allowed

age="25"
❌ str → int NOT allowed

→ Raises ValidationError

======================
📌 KEY DIFFERENCE
======================

Without strict mode:
age="25" → auto converts to 25 ✔

With strict mode:
age="25" → ❌ error

======================
📌 KEY TAKEAWAYS
======================

✔ strict=True disables type coercion  
✔ Enforces exact type matching  
✔ Safer for production-grade validation  

======================
📌 INTERVIEW INSIGHT
======================

Use strict mode when:
→ Data correctness is critical
→ You want to avoid hidden conversions

'''