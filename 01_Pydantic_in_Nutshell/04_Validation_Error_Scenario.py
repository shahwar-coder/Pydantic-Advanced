'''SCENARIO BASED QUESTION - Validation Error Raised'''
"""import pydantic

# print(pydantic.VERSION) # 2.12.5

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

user = User(name="Rahul", age="fifty four", email="rahul@gmail.com")

print(f"User Object : {user}")
print(f"User Name : {user.name}")
print(f"User Age : {user.age}")
print(f"User Email : {user.email}")"""

'''
Scenario-Based Interview Q&A (Pydantic Validation Error)
Context:
User passed age="fifty four" (string) to a field expecting int.
Pydantic raised ValidationError.
'''


'''
1. Why did this ValidationError occur?

Answer:
The error occurred because Pydantic expected an integer for the "age" field,
but received a non-numeric string ("fifty four").

Pydantic attempts type coercion (e.g., "54" → 54),
but it cannot convert natural language text into an integer.

Hence, it raises:
"Input should be a valid integer"
'''


'''
2. How can you fix or handle this issue properly?

Answer:
There are multiple approaches:

1. Provide correct input:
   age=54

2. Preprocess input before passing to model:
   Convert "fifty four" → 54 using custom logic

3. Use a custom validator:
   Handle and transform input before validation fails

Example:
'''

from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int

    @field_validator("age", mode="before")
    def convert_age(cls, v):
        if isinstance(v, str) and v.lower() == "fifty four":
            return 54
        return v


'''
3. What does this error tell you about Pydantic’s validation system?

Answer:
- Pydantic enforces strict type validation based on type hints
- It performs safe type coercion where possible
- It does NOT guess ambiguous conversions (like words → numbers)
- Errors are explicit and informative (great for debugging APIs)

This ensures strong data integrity in backend systems.
'''
