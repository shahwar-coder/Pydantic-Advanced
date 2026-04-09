'''
Pydantic default_factory — Generic High-Priority Interview Q&A 🔥
'''


'''
1. What is default_factory in Pydantic and when is it executed?

Answer:
default_factory is used to generate dynamic default values using a function.

Execution:
- Runs ONLY when the field is not provided
- Runs at instance creation time (not class definition time)

This ensures:
✔ Fresh value per object
✔ No shared state between instances
'''


'''
2. What is the key difference between default and default_factory?

Answer:
default:
- Static value
- Evaluated once at class definition

default_factory:
- Dynamic value
- Function executed per instance

Example:
default=[] ❌ → shared list bug
default_factory=list ✔ → new list per instance

This is a very common interview trap.
'''


'''
3. What types of problems does default_factory solve?

Answer:
- Mutable default issues (list, dict, set)
- Unique value generation (UUIDs)
- Dynamic values (timestamps, random values)
- Avoiding shared state bugs

It ensures each instance is independent.
'''


'''
4. Can default_factory accept arguments or complex logic?

Answer:
No direct arguments can be passed.

But:
You can wrap logic using:
- lambda
- custom function

Example:
default_factory=lambda: generate_value(x, y)

This allows flexible and complex default generation.
'''


'''
🔥 Interview Killer Insight:

"default_factory is essential for avoiding shared mutable state
and generating dynamic defaults safely in Python models."

Missing this concept is a major red flag in interviews.
'''