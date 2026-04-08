import pydantic

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

try:
    user = User(name="Rahul", age="54", email="rahul@gmail.com")
except pydantic.ValidationError as err:
    print(f"Error : {err}")

print(f"User Object : {user}")
print(f"User Name : {user.name}")
print(f"User Age : {user.age}")
print(f"User Email : {user.email}")


'''
Scenario-Based Interview Q&A (Pydantic Type Coercion)
Context:
age="54" (string) is passed where int is expected.
No ValidationError occurs because Pydantic coerces the value.
'''


'''
1. Why is no ValidationError raised in this case?

Answer:
Pydantic performs type coercion when possible.
The string "54" can be safely converted into an integer (54),
so Pydantic automatically parses it instead of raising an error.

This is part of Pydantic’s design:
→ "Be strict when necessary, flexible when safe"
'''


'''
2. What will be the final type and value of the age field?

Answer:
- Final type: int
- Final value: 54

Even though the input was a string, Pydantic converts it internally.
So:
type(user.age) → int
user.age → 54
'''


'''
3. When would coercion fail and raise a ValidationError instead?

Answer:
Coercion fails when the input cannot be safely converted.

Examples:
- age="fifty four" → cannot convert → ValidationError
- age="54abc" → invalid integer → ValidationError
- age=None (if not Optional) → ValidationError

So:
✔ "54" → valid (coercion works)
✖ "fifty four" → invalid (error raised)

This highlights that Pydantic allows safe parsing,
but prevents ambiguous or unsafe conversions.
'''