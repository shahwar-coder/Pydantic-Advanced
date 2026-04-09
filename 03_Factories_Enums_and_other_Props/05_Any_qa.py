'''
Pydantic Any Type — Top Interview Q&A (Concept Depth 🔥)
Context:
value: Any / data: Any
'''


'''
1. What does Any type mean in Pydantic and how is it validated?

Answer:
Any means:
→ Accept ANY type of value without validation

Examples:
123 ✔
"hello" ✔
[1, 2, 3] ✔
{"a": 1} ✔

Important:
Pydantic does NOT perform type checking or structure validation for Any.
It simply accepts the value as-is.
'''


'''
2. When should you use Any in real-world systems?

Answer:
Use Any when:
- Data structure is dynamic or unknown
- Generic API responses (wrapper pattern)
- Pass-through data (no strict schema needed)

Example:
APIResponse → data can be dict, list, string, etc.

Avoid using Any when:
- You need strict validation
- Data structure is known (use BaseModel instead)
'''


'''
3. What are the risks of using Any?

Answer:
- No validation → invalid data can pass silently
- No type safety → runtime errors later
- Harder debugging

Example:
data={"age": "twenty"} ✔ passes
→ but may break logic later

So:
Any sacrifices safety for flexibility.
'''


'''
4. What is a better alternative to Any for safer design?

Answer:
Use:
- Union (limited flexibility with validation)
- BaseModel (structured validation)
- Generic models (advanced use)

Example:
Instead of:
data: Any ❌

Use:
data: Union[User, List[User], str] ✔

This keeps flexibility while maintaining validation.
'''


'''
🔥 Interview Killer Insight:

"Any bypasses Pydantic’s validation system,
so it should be used only when flexibility is required,
otherwise it defeats the purpose of Pydantic."

This is a strong senior-level design point.
'''