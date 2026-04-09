'''
Pydantic Enum — Top Interview Q&A 🔥 (Extended)
'''


'''
1. What is Enum in Pydantic and why is it used?

Answer:
Enum is used to restrict a field to a fixed set of predefined values.

It ensures:
→ Only allowed values are accepted

Benefits:
✔ Prevents invalid input
✔ Improves data consistency
✔ Acts like controlled vocabulary
'''


'''
2. How does Pydantic validate Enum fields?

Answer:
Pydantic:
- Matches input against Enum members
- Accepts valid values
- Raises ValidationError for invalid ones

Example:
"admin" ✔
"guest" ❌
'''


'''
3. When should you use Enum instead of plain strings?

Answer:
Use Enum when:
- Values are fixed and meaningful
- You want reusable constants
- Avoid hardcoded ("magic") strings

Examples:
- Roles, statuses, types
'''


'''
4. What is the difference between Enum and Literal, and which is better?

Answer:
Enum:
- Defined as a class
- Reusable across models
- Supports methods, logic, and extensions

Literal:
- Defined inline (Literal["admin", "user"])
- Simpler but not reusable
- No additional behavior

Which is better?

Use Enum:
✔ When values are reused across multiple models
✔ When domain concepts are important

Use Literal:
✔ For quick, one-off constraints
✔ When simplicity is enough

Interview insight:
Enum = scalable design
Literal = quick constraint
'''


'''
🔥 Interview Killer Insight:

"Enum is for domain modeling and reuse,
Literal is for lightweight validation."

Choosing correctly reflects design maturity.
'''