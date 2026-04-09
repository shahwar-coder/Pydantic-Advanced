'''
Pydantic default_factory + UUID — Top Interview Q&A 🔥
Context:
Auto-generating unique IDs using default_factory
'''


'''
1. Why should we use default_factory instead of default=uuid.uuid4()?

Answer:
default=uuid.uuid4() ❌
→ Function runs ONCE at class definition time
→ Same ID reused for all instances (bug)

default_factory=uuid.uuid4 ✔
→ Function runs EACH TIME a new instance is created
→ Generates a unique ID per object

This ensures:
✔ No shared state
✔ True dynamic values
'''


'''
2. What is the role of lambda in default_factory here?

Answer:
lambda: str(uuid.uuid4())

- uuid.uuid4() returns a UUID object
- lambda wraps it to:
   → execute at runtime
   → convert UUID → string

Equivalent to:

def generate_id():
    return str(uuid.uuid4())

So lambda is just a short inline function used for dynamic value generation.
'''