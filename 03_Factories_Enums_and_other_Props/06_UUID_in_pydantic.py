from pydantic import BaseModel, Field
import uuid


class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4())) # think of lambda a short had for a small function responsble to generate new IDs
    name: str


# Create users
user1 = User(name="Rahul")
user2 = User(name="Ali")

print(user1)
print(user2)


# id='a3f1c9e2-8c1a-4d3a-9c6b-123456789abc' name='Rahul'
# id='b7e2d4f1-2a3b-4c5d-8e9f-987654321xyz' name='Ali'


'''
Before we read,

def generate_id():
    return str(uuid.uuid4())

is the equivalent for,

lambda function we wrote

======================
📌 OVERALL PURPOSE
======================
Demonstrates how to:
- Auto-generate dynamic default values
- Use default_factory in Pydantic
- Assign unique IDs (UUID) per instance

======================
📌 CORE CONCEPTS
======================

id: str = Field(default_factory=...)
→ default_factory:
   - Runs a function to generate value at runtime
   - Called separately for EACH object

uuid.uuid4()
→ Generates a unique random UUID

lambda: str(uuid.uuid4())
→ Converts UUID → string

======================
📌 EXECUTION FLOW
======================

user1 = User(name="Rahul")

STEP 1:
"id" not provided → default_factory triggers

STEP 2:
lambda runs → uuid.uuid4() → unique ID generated

STEP 3:
id assigned to user1

Same process repeats independently for user2

⚠️ Each instance gets a DIFFERENT ID

======================
📌 OUTPUT
======================

user1 → id='random-uuid-1', name='Rahul'
user2 → id='random-uuid-2', name='Ali'

======================
📌 KEY TAKEAWAYS
======================

✔ default_factory generates dynamic defaults  
✔ Runs per instance (not shared like default=...)  
✔ Ideal for unique values (UUID, timestamps, etc.)  

======================
📌 INTERVIEW INSIGHT
======================

default=uuid.uuid4() ❌ (wrong)
→ runs once at definition time

default_factory=uuid.uuid4 ✔
→ runs per object creation

'''