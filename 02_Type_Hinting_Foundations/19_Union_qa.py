'''
Pydantic Union Type — Top Interview Q&A 🔥
Context:
id: Union[int, str]
'''


'''
1. How does Pydantic validate fields with Union types?

Answer:
Pydantic tries each type in the Union sequentially (left → right).

Flow:
- Try int
- If fails → try str
- If both fail → ValidationError

Example:
id=123 → matches int ✔
id="abc123" → matches str ✔
id=12.5 → fails both ❌
'''


'''
2. Why does id=12.5 raise a ValidationError?

Answer:
- float (12.5) cannot be safely converted to int without data loss
- It is not a string either

So:
int → fails
str → not attempted as coercion here (depends on context)

Hence → ValidationError
'''


'''
3. Does order of types in Union matter?

Answer:
Yes, VERY important.

Example:
Union[int, str] vs Union[str, int]

Pydantic checks in order:
- First matching type is used

So ordering can affect:
- Coercion behavior
- Final stored type

This is a common interview trap.
'''


'''
4. When should you use Union in real-world systems?

Answer:
Use Union when:
- A field can legitimately accept multiple types
- APIs return flexible schemas
- Backward compatibility is needed

Examples:
- ID can be int or string
- Response can be success or error object

But:
Avoid overusing Union → can make validation ambiguous.
'''


'''
🔥 Interview Killer Insight:

"Pydantic evaluates Union types sequentially,
so type order directly impacts validation and coercion behavior."

Most candidates ignore this subtle but critical detail.
'''