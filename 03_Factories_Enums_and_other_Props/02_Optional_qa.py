'''
Pydantic Optional — Deep Concept Interview Q&A 🔥
Context:
nickname: Optional[str]
'''


'''
1. What does Optional[str] actually mean in Pydantic?

Answer:
Optional[str] means:
→ The field can be either:
   - str
   - None

IMPORTANT:
Optional does NOT mean the field is optional (i.e., can be omitted).
It only means the value can be None.

So:
nickname=None ✔ valid
nickname="R" ✔ valid
'''


'''
2. Is the field truly optional if defined as Optional[str]?

Answer:
No — this is a common misconception.

Optional[str] allows None as a value,
but the field is still REQUIRED unless a default is provided.

Example:
class User(BaseModel):
    nickname: Optional[str]

User() ❌ → ValidationError (field missing)

To make it optional (not required):
nickname: Optional[str] = None
'''


'''
3. How does Pydantic validate Optional fields internally?

Answer:
Pydantic treats Optional[str] as:
Union[str, None]

Validation flow:
- If value is None → accept ✔
- Else → validate as str

So:
Optional[T] = Union[T, None]

This is how Pydantic processes it internally.
'''


'''
4. When should you use Optional in real-world systems?

Answer:
Use Optional when:
- Field may not have a value
- Field is nullable in database
- Partial updates (PATCH APIs)

Examples:
- nickname
- middle_name
- secondary_email

But combine with default (= None) if field is truly optional.
'''


'''
🔥 Interview Killer Insight:

"Optional[T] means 'can be None', NOT 'can be missing'.
To make a field optional in input, you must provide a default value."

This is one of the most common interview traps.
'''
# VVIP
# Pydantic treats 
# Optional[str] 
# as: 
# Union[str, None]