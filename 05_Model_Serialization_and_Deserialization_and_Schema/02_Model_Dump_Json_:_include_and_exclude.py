from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
    city: str


user = User(
    name="Rahul",
    age=25,
    email="rahul@gmail.com",
    city="Delhi"
)

print("Full model:", user)

# 🔹 Include only selected fields
print("\nInclude only name & email:")
print(user.model_dump(include={"name", "email"}))

# 🔹 Exclude specific fields
print("\nExclude age & city:")
print(user.model_dump(exclude={"age", "city"}))


# Include only name & email:
# {'name': 'Rahul', 'email': 'rahul@gmail.com'}

# Exclude age & city:
# {'name': 'Rahul', 'email': 'rahul@gmail.com'}