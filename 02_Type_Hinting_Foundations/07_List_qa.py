'''
Pydantic List Handling — Scenario-Based Interview Q&A 🔥
Covers:
1. List[str]
2. List validation using Field
3. List of nested objects
'''


# ==============================
# 1. List[str] Scenario
# ==============================

'''
Code Context:
User model with hobbies: List[str]
Valid: ["cricket", "coding"]
Invalid: "cricket" (not a list)
'''


'''
Q1. Why does hobbies="cricket" raise a ValidationError?

Answer:
Because Pydantic expects a list of strings (List[str]),
but received a single string instead.

Pydantic does NOT automatically wrap a string into a list.
Type mismatch → ValidationError.
'''


'''
Q2. What validation does List[str] enforce?

Answer:
- Ensures the input is a list
- Ensures each element inside the list is a string

Example:
["cricket", "coding"] ✔
["cricket", 123] ❌ (invalid element type)
'''


'''
Q3. Does Pydantic perform coercion inside lists?

Answer:
Yes, but only when safe.

Example:
["1", "2"] → can remain strings ✔
[1, 2] → may be coerced to ["1", "2"] depending on context

But:
"hobby" → cannot become ["hobby"] ❌
'''



# ==============================
# 2. List Validation using Field
# ==============================

'''
Code Context:
hobbies: List[str] = Field(min_length=1, max_length=5)
'''


'''
Q1. What do min_length and max_length mean for lists?

Answer:
They define constraints on the number of items in the list.

- min_length=1 → at least 1 item required
- max_length=5 → at most 5 items allowed

This validates list size, NOT string length.
'''


'''
Q2. What happens if hobbies=[] is passed?

Answer:
ValidationError is raised because:
List length = 0 < min_length=1

So empty lists are not allowed in this case.
'''


'''
Q3. Can Field() validate individual elements of the list?

Answer:
No, Field() only validates the container (list size).

To validate elements:
- Use type hints (List[str])
- Or custom validators

Field does NOT validate each item’s content.
'''



# ==============================
# 3. List of Nested Objects
# ==============================

'''
Code Context:
addresses: List[Address]
Each Address has city and pincode
'''


'''
Q1. How does Pydantic handle list of nested models?

Answer:
Pydantic:
- Iterates through the list
- Converts each dictionary into an Address object
- Validates each field inside Address

So dict → Address model automatically.
'''


'''
Q2. What happens if one nested object is invalid?

Answer:
Pydantic raises a ValidationError for that specific item.

Example:
{"city": "Delhi", "pincode": "abc"} ❌

Error will indicate:
addresses -> index -> field → error

This makes debugging precise.
'''


'''
Q3. Why are nested models important in real-world systems?

Answer:
- Represent structured data (e.g., user → multiple addresses)
- Improve readability and maintainability
- Ensure validation at multiple levels

Common in APIs:
JSON → deeply nested → mapped to Pydantic models
'''


'''
🔥 Interview Killer Insight:

"List validation in Pydantic works at two levels:
1. Container level (list size via Field)
2. Element level (type hints & nested models)"

Most candidates miss this distinction.
'''

# -=-=-=-=-=-=-=-=

'''
Pydantic Nested List (Matrix) — Top Interview Q&A 🔥
Context:
values: List[List[int]] → 2D structure (matrix)
'''


'''
Q1. How does Pydantic validate a nested list like List[List[int]]?

Answer:
Pydantic performs validation in layers:

1. Outer structure → must be a list
2. Each element inside → must also be a list
3. Inner elements → must be integers

So validation happens recursively:
List → List → int

Example:
[[1, 2], [3, 4]] ✔ valid
[[1, "2"], [3, 4]] ❌ invalid (string inside)
'''


'''
Q2. Will Pydantic perform type coercion inside nested lists?

Answer:
Yes, Pydantic applies coercion at all levels if safe.

Example:
[["1", "2"], ["3", "4"]] → [[1, 2], [3, 4]] ✔

But:
[["one", "two"]] ❌ → cannot convert → ValidationError

So coercion is recursive but still safe and controlled.
'''


'''
Q3. How would you enforce stricter validation for a matrix structure?

Answer:
By default, Pydantic only enforces types, not structure consistency.

To enforce stricter rules (like fixed row size), use a validator:

Example:
- Ensure all rows have same length
- Ensure matrix is not empty

This requires custom validation logic using @field_validator.

Key point:
Pydantic validates types automatically,
but structural rules (like matrix shape) must be enforced manually.
'''


'''
🔥 Interview Insight:

"Nested lists in Pydantic are validated recursively,
but business constraints (like matrix dimensions)
require custom validators."

This is a common senior-level discussion point.
'''