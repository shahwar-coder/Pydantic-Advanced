from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str

user = User(name="Rahul", age=25)

print(user)
print(user.age)  # accessible

# name='Rahul' age=25
# 25


'''
📌 PURPOSE
Allows extra (undefined) fields in the model.

📌 CORE
model_config = ConfigDict(extra="allow")
→ Accepts fields not defined in schema

📌 FLOW
Input:
name="Rahul", age=25

→ "name" → validated ✔
→ "age" → not defined, but allowed ✔
→ stored in model

📌 ACCESS
user.age → works ✔

📌 TAKEAWAY
✔ extra="allow" keeps unexpected fields  
✔ Useful for flexible / evolving schemas  

📌 CONTRAST
extra="ignore" → drops extra fields  
extra="forbid" → raises error  

'''