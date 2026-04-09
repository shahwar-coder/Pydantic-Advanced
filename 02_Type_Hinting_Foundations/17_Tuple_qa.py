'''
Pydantic Tuple Handling — Top Interview Q&A 🔥
Covers:
1. Fixed-length Tuple[int, int]
2. Variable-length Tuple[int, ...] with constraints
'''


# ==============================
# 1. Fixed-Length Tuple Scenario
# ==============================

'''
Code Context:
point: Tuple[int, int]
Reference: :contentReference[oaicite:0]{index=0}
'''


'''
Q1. What does Tuple[int, int] enforce in Pydantic?

Answer:
It enforces:
- Exactly 2 elements
- Both must be integers

Example:
(10, 20) ✔ valid
(10, 20, 30) ❌ invalid (extra element)
(10, "20") ❌ invalid type

So both length and type are strictly enforced.
'''


'''
Q2. Does Pydantic allow list input for Tuple fields?

Answer:
Yes.

Example:
[10, 20] → converted to (10, 20) ✔

Pydantic accepts compatible iterables
and converts them into tuples automatically.
'''


'''
Q3. Why use Tuple instead of List here?

Answer:
- Tuple enforces fixed size
- Tuple is immutable (safer for fixed data like coordinates)
- Prevents accidental modification

Example use case:
→ Coordinates (x, y)
'''



# ==============================
# 2. Variable-Length Tuple Scenario
# ==============================

'''
Code Context:
values: Tuple[int, ...] with Field constraints
'''


'''
Q4. What does Tuple[int, ...] mean?

Answer:
It means:
- Tuple of integers
- Any number of elements allowed

"..." indicates variable length.

Example:
(1, 2) ✔
(1, 2, 3, 4) ✔
'''


'''
Q5. How do min_length and max_length work with Tuple?

Answer:
They restrict the number of elements in the tuple.

Example:
min_length=2, max_length=4

Valid:
(1, 2), (1, 2, 3)

Invalid:
(1,) ❌ too short
(1,2,3,4,5) ❌ too long
'''


'''
Q6. Does Pydantic validate each element inside Tuple?

Answer:
Yes.

Example:
(1, 2, 3) ✔
(1, "2", 3) → "2" → 2 (coercion) ✔
(1, "two", 3) ❌ invalid

Validation is applied to every element.
'''


'''
Q7. Difference between Tuple[int, int] and Tuple[int, ...]?

Answer:
Tuple[int, int]:
- Fixed length (exactly 2 elements)

Tuple[int, ...]:
- Variable length (any number of elements)

This is a very common interview question.
'''


'''
Q8. When should you prefer Tuple over List or Set?

Answer:
Use Tuple when:
- Order matters
- Size is fixed or controlled
- Data should be immutable

Examples:
- Coordinates
- RGB values
- Fixed configuration values
'''


'''
🔥 Interview Killer Insight:

"Pydantic enforces both structure and type in tuples —
fixed tuples enforce exact shape,
while variable tuples combine flexibility with constraints."

Many candidates miss the distinction between:
→ Tuple[int, int] vs Tuple[int, ...]
'''