from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    age: int


user = User(name="Rahul", age=25)
print(user)

# ❌ Try modifying
user.age = 30


'''
======================
📌 OVERALL PURPOSE
======================
Demonstrates IMMUTABILITY in Pydantic using:
→ frozen=True

======================
📌 CORE CONCEPT
======================

model_config = ConfigDict(frozen=True)

→ Makes model instances immutable (read-only)
→ Similar to "frozen dataclass"

======================
📌 EXECUTION FLOW
======================

user = User(name="Rahul", age=25)

→ Object created normally ✔

----------------------

user.age = 30

→ ❌ Modification attempt

→ Since frozen=True:
   - Attribute assignment is blocked
   - Raises error (TypeError / ValidationError)

======================
📌 BEHAVIOR
======================

✔ Read allowed:
user.age → 25

❌ Write NOT allowed:
user.age = 30 → error

======================
📌 KEY TAKEAWAYS
======================

✔ frozen=True makes model immutable  
✔ Prevents accidental data changes  
✔ Ensures data integrity  

======================
📌 INTERVIEW INSIGHT
======================

Use frozen models when:
→ Data should not change after creation
→ Working with configs, constants, safe state objects

'''