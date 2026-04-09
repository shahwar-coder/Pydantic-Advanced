'''
Pydantic Set Handling — Top Interview Q&A 🔥
Context:
values: Set[int] with Field constraints
Reference: :contentReference[oaicite:0]{index=0}
'''


'''
1. How does Pydantic handle duplicate values in a Set field?

Answer:
Pydantic converts input into a Python set,
which automatically removes duplicates.

Example:
{1, 2, 3, 3, 4} → {1, 2, 3, 4}

Important:
Deduplication happens BEFORE validation.
'''


'''
2. How do min_length and max_length work with Set?

Answer:
They apply to the number of UNIQUE elements in the set.

Example:
Input: {1, 2, 2, 3}
After deduplication: {1, 2, 3} → length = 3

Validation is applied AFTER duplicates are removed.
'''


'''
3. What happens if duplicates reduce the set below min_length?

Answer:
ValidationError is raised.

Example:
values={1, 1}
→ becomes {1}
→ length = 1 < min_length=2 ❌

So even if input looked large,
final unique size matters.
'''


'''
4. Does Pydantic perform type coercion in Set?

Answer:
Yes, if safe.

Example:
{"1", "2"} → {1, 2} ✔

But:
{"one", "two"} ❌ → cannot convert → ValidationError

Coercion works before set formation.
'''


'''
5. When should you prefer Set over List in Pydantic?

Answer:
Use Set when:
- Uniqueness is required
- Order does NOT matter

Use List when:
- Order matters
- Duplicates are allowed

Set is ideal for:
→ Tags, IDs, unique items
'''


'''
🔥 Interview Killer Insight:

"Pydantic leverages Python’s set behavior,
so uniqueness is enforced automatically,
and validation happens on the deduplicated result."

Many candidates miss the order:
→ parse → deduplicate → validate
'''