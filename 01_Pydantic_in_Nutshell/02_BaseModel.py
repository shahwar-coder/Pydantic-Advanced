'''
Pydantic BaseModel — Interview Questions (Focused Set)
'''


'''
1. What is BaseModel in Pydantic and why is it important?

Answer:
BaseModel is the core class in Pydantic used to define data schemas.
It provides automatic validation, parsing, and serialization using Python type hints.
All Pydantic models must inherit from BaseModel.
'''


'''
2. How does BaseModel perform validation when creating an instance?

Answer:
When a model instance is created, BaseModel:
- Reads type hints
- Parses incoming data (type coercion if possible)
- Validates values against constraints
- Raises ValidationError if validation fails
'''


'''
3. What are some commonly used methods of BaseModel in Pydantic v2?

Answer:
- model_dump() → converts model to dictionary
- model_dump_json() → converts model to JSON string
- model_validate() → validates external data into model
These methods are used for serialization and validation workflows.
'''


'''
4. How does BaseModel handle extra or unexpected fields?

Answer:
By default, extra fields are ignored.
You can control this behavior using model_config:
- "ignore" → ignore extra fields
- "forbid" → raise error
- "allow" → include extra fields
'''


'''
5. Can BaseModel be nested and reused across models?

Answer:
Yes, BaseModel supports nested models.
You can define one model inside another to represent structured data.
This promotes reusability and clean schema design.
'''


'''
6. Show a simple implementation of BaseModel.

Answer:
A basic example defines fields with type hints and creates an instance.
Pydantic automatically validates and converts input data.
'''

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

user = User(id="1", name="Alice")  # id will be converted to int
print(user)
print(user.model_dump())