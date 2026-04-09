'''
Pydantic "extra" config — Top Interview Q&A 🔥
References:
- allow
- forbid
- ignore
'''


'''
1. What is "extra" in Pydantic and why is it important?

Answer:
"extra" controls how Pydantic handles fields that are NOT defined in the model.

It decides:
→ Accept them
→ Ignore them
→ Reject them

This is critical for:
- API validation
- Schema enforcement
- Handling unexpected input
'''


'''
2. What are the three modes of "extra" and how do they differ?

Answer:

| Mode    | Behavior                          | Stored? | Error? |
|---------|----------------------------------|---------|--------|
| ignore  | Ignores extra fields             | ❌ No   | ❌ No  |
| allow   | Accepts and stores extra fields  | ✔ Yes  | ❌ No  |
| forbid  | Rejects extra fields             | ❌ No   | ✔ Yes |

Example:
Input → name="Rahul", age=25

ignore:
→ age dropped

allow:
→ age kept and accessible

forbid:
→ ValidationError
'''


'''
3. What is the default behavior of "extra" in Pydantic?

Answer:
Default = "ignore"

So:
Extra fields are silently ignored unless configured otherwise.

This is important because:
→ Unexpected data might be lost without notice
'''


'''
4. When should you use each mode in real-world systems?

Answer:

ignore:
→ When extra data is irrelevant
→ Quick prototyping

allow:
→ Flexible schemas (evolving APIs)
→ When you want to preserve unknown data

forbid:
→ Strict APIs
→ Security-sensitive systems
→ Prevent unexpected input

Best practice:
Use "forbid" in production APIs for strict validation.
'''


'''
🔥 Interview Killer Insight:

"'extra' defines how your system reacts to unexpected input —
ignore hides it, allow keeps it, forbid blocks it."

Choosing the wrong mode can lead to silent bugs or security issues.
'''