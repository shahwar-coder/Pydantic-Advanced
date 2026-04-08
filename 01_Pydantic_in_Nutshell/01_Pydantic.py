"""
Pydantic Interview Q&A (High Priority 🚀)
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Union
from fastapi import FastAPI


'''
1. What is Pydantic?
Answer:
Pydantic is a data validation and settings management library
that uses Python type hints. It validates, parses, and serializes data.
'''


'''
2. Why is Pydantic used?
Answer:
- Data validation
- Data parsing (type coercion)
- Serialization (dict/json)
- Strong integration with FastAPI
'''


'''
3. Basic Example
'''

class User(BaseModel):
    id: int
    name: str = Field(min_length=3)

user = User(id="1", name="John")  # id is coerced to int
print(user)


'''
4. What are type hints in Pydantic?
Answer:
Pydantic relies on Python type hints such as:
int, str, List, Optional, Union
'''

class Item(BaseModel):
    name: str
    tags: Optional[List[str]] = None


'''
5. What is BaseModel?
Answer:
BaseModel is the core class used to define data schemas in Pydantic.
'''


'''
6. Difference: Pydantic vs Dataclasses?
Answer:
- Pydantic: validation + parsing + serialization
- Dataclasses: only structure, no validation
'''


'''
7. What is Field() used for?
Answer:
Used to define validation rules and metadata like:
min_length, max_length, gt, default, etc.
'''

class Product(BaseModel):
    price: float = Field(gt=0)


'''
8. What are validators?
Answer:
Custom validation logic using decorators like @field_validator
'''

class Person(BaseModel):
    name: str

    @field_validator("name")
    def validate_name(cls, v):
        if not v.isalpha():
            raise ValueError("Name must contain only letters")
        return v


'''
9. What are nested models?
Answer:
Models inside models for structured data.
'''

class Address(BaseModel):
    city: str

class UserWithAddress(BaseModel):
    name: str
    address: Address


'''
10. How does serialization work?
Answer:
Pydantic v2 uses:
- model_dump() -> dict
- model_dump_json() -> JSON
'''

u = User(id=1, name="Alice")
print(u.model_dump())
print(u.model_dump_json())


'''
11. Pydantic v1 vs v2?
Answer:
v1:
- .dict()
- .json()

v2:
- .model_dump()
- .model_dump_json()

v2 is faster and uses pydantic-core internally.
'''


'''
12. How validation works internally?
Answer:
- Input data is parsed using type hints
- Validated via pydantic-core engine
- Errors raised if validation fails
'''


'''
13. Config in Pydantic
Answer:
Used to customize model behavior like forbidding extra fields.
'''

class ConfigExample(BaseModel):
    name: str

    model_config = {
        "extra": "forbid"
    }


'''
14. FastAPI Integration Example
Answer:
Pydantic models are used for request validation automatically.
'''

app = FastAPI()

class APIItem(BaseModel):
    name: str

@app.post("/items")
async def create_item(item: APIItem):
    return item


'''
15. Common Interview Trap Question:
What happens if wrong type is passed?

Answer:
Pydantic tries to coerce the type.
If not possible, it raises ValidationError.
'''

try:
    User(id="abc", name="John")
except Exception as e:
    print(e)


'''
16. Advanced: Union Type
Answer:
Allows multiple possible types for a field.
'''

class Data(BaseModel):
    value: Union[int, str]


'''
17. Why is Pydantic critical in backend systems?
Answer:
- Prevents invalid data
- Enforces API contracts
- Reduces runtime bugs
'''


'''
🔥 Interview Killer Summary:

Pydantic ensures strict data validation using type hints,
automatically parsing and serializing data, and integrates
seamlessly with FastAPI for request/response validation.
'''