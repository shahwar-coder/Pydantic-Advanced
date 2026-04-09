from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(pattern="^[a-zA-Z]+$")

User(username="Rahul")   # ✅
User(username="rahul123") # ❌


'''
======================
📌 OVERALL PURPOSE
======================
Demonstrates how to enforce string validation using
regex (pattern) in Pydantic Field.

======================
📌 CORE CONCEPT
======================

username: str = Field(pattern="^[a-zA-Z]+$")

→ pattern = regular expression (regex)
→ Enforces format constraints on string input

Regex breakdown:
"^[a-zA-Z]+$"

^      → start of string  
[a-zA-Z] → only letters (lowercase + uppercase)  
+      → one or more characters  
$      → end of string  

✔ Means: ONLY alphabets allowed, no numbers/symbols

======================
📌 EXECUTION FLOW
======================

User(username="Rahul")

STEP 1:
Type check → str ✔

STEP 2:
Regex validation:
"Rahul" → matches pattern ✔

→ Model created successfully

----------------------

User(username="rahul123")

STEP 1:
Type check → str ✔

STEP 2:
Regex validation:
"rahul123" → contains numbers ❌

→ ValidationError raised

======================
📌 ERROR BEHAVIOR
======================

Error includes:
- field name (username)
- pattern mismatch info
- input value

======================
📌 KEY TAKEAWAYS
======================

✔ pattern enforces string format using regex  
✔ Validation happens AFTER type checking  
✔ Prevents invalid formats (e.g., digits, symbols)  

======================
📌 INTERVIEW INSIGHT
======================

Use pattern when:
→ Input must follow strict format (username, email, IDs)

Common use cases:
- Username rules
- Phone numbers
- Custom IDs

'''