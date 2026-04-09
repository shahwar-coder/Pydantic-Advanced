'''
extra=ignore is default too.
'''

from pydantic import BaseModel

class User(BaseModel):
    name: str

user = User(name="Rahul", age=25)  # extra field

print(user)
print(user.model_dump())