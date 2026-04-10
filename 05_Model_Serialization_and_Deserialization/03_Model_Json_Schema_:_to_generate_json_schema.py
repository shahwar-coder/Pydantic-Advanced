from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    name: str = Field(..., min_length=3, title="User Name")
    age: int = Field(default=18, ge=0, le=100)
    email: EmailStr
    nickname: Optional[str] = None


# 🔹 Generate JSON Schema
schema = User.model_json_schema()

print(schema)


# {
#   "title": "User",
#   "type": "object",
#   "properties": {
#     "name": {
#       "title": "User Name",
#       "type": "string",
#       "minLength": 3
#     },
#     "age": {
#       "type": "integer",
#       "minimum": 0,
#       "maximum": 100,
#       "default": 18
#     },
#     "email": {
#       "type": "string",
#       "format": "email"
#     },
#     "nickname": {
#       "anyOf": [
#         { "type": "string" },
#         { "type": "null" }
#       ]
#     }
#   },
#   "required": ["name", "email"]
# }

# Used for:

# API documentation (FastAPI)
# Validation specs
# OpenAPI generation



'''
======================
📌 PURPOSE (CODE)
======================
Generates a JSON Schema from a Pydantic model
→ Used for API docs, validation rules, OpenAPI

schema = User.model_json_schema()

======================
📌 OUTPUT EXPLAINED
======================

"title": "User"
→ Name of the model (class name)

"type": "object"
→ This schema represents a JSON object (dict)

----------------------

"properties"
→ Defines all fields in the model

Each field contains its validation + metadata

----------------------

"name": {
  "title": "User Name",
  "type": "string",
  "minLength": 3
}

→ "title": comes from Field(title=...)
→ "type": string → Python str
→ "minLength": 3 → from Field(min_length=3)

----------------------

"age": {
  "type": "integer",
  "minimum": 0,
  "maximum": 100,
  "default": 18
}

→ "minimum"/"maximum" → from ge=0, le=100  
→ "default": 18 → default value if not provided  

----------------------

"email": {
  "type": "string",
  "format": "email"
}

→ EmailStr becomes:
   - type: string
   - format: email (special validation hint)

----------------------

"nickname": {
  "anyOf": [
    { "type": "string" },
    { "type": "null" }
  ]
}

→ Optional[str] means:
   - can be string OR null
→ represented using "anyOf"

----------------------

"required": ["name", "email"]

→ Fields WITHOUT default → required  
→ Fields WITH default → optional  

So:
✔ name → required (Field(...))  
✔ email → required (no default)  
✔ age → optional (default=18)  
✔ nickname → optional (default=None)  

======================
📌 KEY TAKEAWAYS
======================

✔ model_json_schema() → converts model → JSON schema  
✔ Field constraints → reflected in schema  
✔ Optional → becomes "null" allowed  
✔ Required fields → listed explicitly  

======================
📌 INTERVIEW INSIGHT
======================

This schema is used by:
→ FastAPI to auto-generate Swagger / OpenAPI docs  
→ Frontend to understand API contract  

'''