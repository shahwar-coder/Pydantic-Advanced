'''
Pydantic Strict Mode — Interview Questions (Very Important 🔥)
Context:
Two ways to enforce strict typing:
1. Global strict mode → ConfigDict(strict=True)
2. Field-level strict types → StrictInt, StrictStr, StrictBool
'''


'''
1. What is strict mode in Pydantic and why is it used?

Answer:
Strict mode disables type coercion.
Pydantic will no longer convert values (e.g., "25" → 25).

It ensures:
- Exact type matching
- No implicit conversions
- Higher data integrity (important in production systems)

Used when:
→ You want to reject incorrect input instead of silently fixing it
'''


'''
2. What is the difference between global strict mode and Strict types?

Answer:
1. Global strict mode (ConfigDict(strict=True)):
   - Applies strict validation to ALL fields
   - Easier to enforce consistency across the model

2. Field-level strict types (StrictInt, StrictStr, etc.):
   - Applied to specific fields only
   - More granular control

Example:
- Use global → when entire model must be strict
- Use Strict types → when only some fields need strictness
'''


'''
3. What will happen if you pass age="25" in strict mode?

Answer:
It will raise a ValidationError.

Reason:
In strict mode, Pydantic does NOT convert string to int.
"25" remains a string → type mismatch → error

This is opposite of default behavior where coercion happens.
'''


'''
4. When should you prefer strict mode in real-world systems?

Answer:
- Financial systems (money, transactions)
- Authentication / authorization data
- APIs where correctness is critical
- When input source is untrusted

Strict mode prevents silent bugs caused by unintended conversions.
'''


'''
5. Can strict mode and normal fields be mixed?

Answer:
Yes.

You can:
- Use global strict mode and override specific fields if needed
- Or use Strict types only for sensitive fields

This gives flexibility in schema design.
'''


'''
🔥 Interview Insight:

Default Pydantic = "smart parsing"
Strict mode = "exact validation"

Good engineers know WHEN to use each.
'''