# strict -> Input Type Validation, if wrong input type, does not proceed, stops there, no more coercion as well
# frozen -> more like freezing the model state (no change in fields, nither it's values)

'''
Pydantic strict vs frozen — Top Interview Q&A 🔥
References: :contentReference[oaicite:0]{index=0} , :contentReference[oaicite:1]{index=1}
'''


'''
1. What is the difference between strict mode and frozen mode in Pydantic?

Answer:
strict=True:
→ Controls INPUT validation
→ Disables type coercion (input ke time hi rok deta agar type match nahi hua toh, toh coercion ka sawaal hi nahi hai)
→ Ensures exact type match at creation time

frozen=True:
→ Controls OBJECT mutability
→ Makes model immutable after creation
→ Prevents modifying fields later

Key difference:
strict → validation phase
frozen → post-creation behavior
'''


'''
2. When should you use strict mode vs frozen mode?

Answer:
Use strict mode when:
- Data correctness is critical
- You want to avoid silent conversions
- APIs must enforce exact types

Use frozen mode when:
- Data should not change after creation
- You want immutability (like config, DTOs)
- Prevent accidental updates

In real systems:
→ strict = input safety
→ frozen = state safety
'''


'''
3. What happens if you try to modify a frozen model?

Answer:
It raises an error (TypeError / validation-related error).

Example:
user.age = 30 ❌

Because:
Model is immutable → fields cannot be reassigned

This ensures data integrity after creation.
'''


'''
4. Can strict and frozen be used together?

Answer:
Yes.

You can combine both:
- strict=True → enforce correct input types
- frozen=True → prevent later modification

This creates:
✔ Fully validated
✔ Immutable models

Useful in:
- Financial systems
- Config objects
- Critical domain models
'''


'''
🔥 Interview Killer Insight:

"strict protects data at input,
frozen protects data after creation."

Senior engineers always separate these two concerns.
'''