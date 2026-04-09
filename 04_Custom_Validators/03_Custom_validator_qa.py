'''
Pydantic @field_validator & @model_validator — Deep Interview Q&A 🔥
Focus:
- Concept clarity
- Execution order
- Real-world usage
'''


'''
1. What is the difference between @field_validator and @model_validator?

Answer:
@field_validator:
→ Validates a SINGLE field
→ Works on one field at a time

@model_validator:
→ Validates the ENTIRE model
→ Has access to multiple fields together

Use case:
- field_validator → validate email format
- model_validator → validate password == confirm_password

Key idea:
field → local validation
model → cross-field validation
'''


'''
2. What is the difference between mode="before" and mode="after"?

Answer:
mode="before":
→ Runs BEFORE type validation / parsing
→ Works on raw input

mode="after":
→ Runs AFTER parsing
→ Works on validated Python objects

Example:
"25" → before sees "25"
→ after sees 25 (int)

This is a very common interview trap.
'''


'''
3. Can @field_validator access other fields in the model?

Answer:
Not reliably.

@field_validator is designed for single-field validation.

If you need multiple fields:
→ Use @model_validator

Trying cross-field logic in field_validator is bad design.
'''


'''
4. What happens if a validator raises ValueError?

Answer:
Pydantic catches it and converts it into:
→ ValidationError

This ensures:
✔ Standardized error handling
✔ Clear error messages for users

Important:
You should raise ValueError, not ValidationError manually.
'''


'''
5. What is execution order of validation in Pydantic?

Answer:
1. model_validator(mode="before")
2. field_validator(mode="before")
3. Type parsing / coercion
4. field_validator(mode="after")
5. model_validator(mode="after")

This pipeline is critical for deep understanding.
'''


'''
6. When would you use model_validator(mode="before")?

Answer:
- Preprocess raw input
- Normalize data (e.g., merge fields)
- Reject invalid structure early

Example:
Convert incoming payload before parsing

This is advanced usage.
'''


'''
7. What is a common mistake with validators in interviews?

Answer:
- Using field_validator for cross-field logic ❌
- Forgetting mode="before"/"after"
- Not understanding execution order
- Raising wrong exception types

These indicate shallow understanding.
'''


'''
🔥 Interview Killer Insight:

"field_validator is for field-level rules,
model_validator is for business logic across fields."

Understanding WHEN to use each is a strong senior signal.
'''