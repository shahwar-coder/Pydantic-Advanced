'''
Pydantic Literal — Top Interview Q&A 🔥
'''


'''
1. What is Literal in Pydantic and how does it work?

Answer:
Literal is used to restrict a field to specific fixed values.

Example:
from typing import Literal

status: Literal["success", "error"]

Pydantic ensures:
→ Only these exact values are accepted

Anything else → ValidationError
'''


'''
2. How is Literal different from Enum?

Answer:
Literal:
- Inline definition
- Not reusable
- Simple and lightweight

Enum:
- Defined as a class
- Reusable across models
- Supports methods and extensions

Use Literal for quick constraints,
Enum for scalable design.
'''


'''
3. Does Pydantic perform coercion with Literal?

Answer:
No (strict matching).

Example:
Literal[1, 2]

Input:
1 ✔
"1" ❌ (string ≠ int)

Literal requires exact value and type match.
'''


'''
4. When should you use Literal in real-world systems?

Answer:
- Small fixed set of values
- One-off constraints
- API flags or modes

Examples:
- status: Literal["success", "error"]
- method: Literal["GET", "POST"]

Avoid Literal when:
→ Values are reused → use Enum instead
'''


'''
5. What are limitations of Literal?

Answer:
- Not reusable across multiple models
- Cannot attach methods or behavior
- Harder to maintain if values grow

So:
Literal is simple but not scalable.
'''


'''
🔥 Interview Killer Insight:

"Literal enforces exact value matching with zero flexibility,
making it ideal for strict, small, and one-off constraints."

Misusing Literal instead of Enum is a common design mistake.
'''