'''
Pydantic Field — Top / Important / Tricky Interview Q&A 🔥
'''


'''
1. What is the real purpose of Field() in Pydantic beyond just defaults?

Answer:
Field() is not just for defaults — it provides:
- Validation constraints (min_length, gt, etc.)
- Metadata (description, title)
- Default values / default_factory

So:
Field = validation + metadata + configuration

Many candidates wrongly think it's only for defaults.
'''


'''
2. What is the difference between default= and default_factory in Field()?

Answer:
default:
→ Static value
→ Shared across instances (danger with mutable types)

default_factory:
→ Function executed per instance
→ Generates fresh value each time

Example trap:
Field(default=[]) ❌ shared list bug
Field(default_factory=list) ✔ safe
'''


'''
3. Does Field() enforce validation by itself?

Answer:
No.

Field only defines rules,
but validation is executed by Pydantic engine.

Example:
name: str = Field(min_length=3)

Field defines constraint,
Pydantic enforces it.

So:
Field ≠ validator
Field → configuration for validation
'''


'''
4. What does Field(...) (ellipsis) mean?

Answer:
Field(...) means:
→ This field is REQUIRED

Example:
name: str = Field(...)

Even if no default is provided,
this explicitly marks the field as mandatory.

This is often used in FastAPI schemas.
'''


'''
5. Can Field() change how data is parsed or only validated?

Answer:
Primarily validation + metadata.

But combined with:
- default_factory
- alias
- strict settings

It can influence parsing behavior indirectly.

Still:
Core parsing is handled by Pydantic, not Field itself.
'''


'''
🔥 Interview Killer Insight:

"Field defines the rules, Pydantic enforces them."

Understanding this separation is a strong signal of depth.
'''