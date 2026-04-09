'''
Pydantic Dict & Nested Dict — Top Interview Q&A (Deep Concepts 🔥)
Covers:
1. Dict[str, Model]
2. Dict within Dict (deep nesting)
'''


# ==============================
# 1. Dict[str, Product] Scenario
# ==============================

'''
Code Context:
products: Dict[str, Product]
'''


'''
Q1. What does Dict[str, Product] represent in Pydantic?

Answer:
It represents:
- Dynamic keys (str) → e.g., "p1", "p2"
- Structured values → Product model

So:
{
  "p1": Product(...),
  "p2": Product(...)
}

This allows flexible keys with strict value validation.
'''


'''
Q2. How does Pydantic handle inner dictionaries in this case?

Answer:
Pydantic automatically converts inner dictionaries into Product objects.

Example:
{"name": "tea", "price": 4.99}
        ↓
Product(name="tea", price=4.99)

This happens recursively during model initialization.
'''


'''
Q3. What happens if one product has invalid data?

Answer:
Pydantic raises ValidationError with a precise path.

Example:
products → p1 → price

This tells:
- Which key failed
- Which field inside failed

This makes debugging highly efficient.
'''



# ==============================
# 2. Dict within Dict Scenario
# ==============================

'''
Code Context:
orders: Dict[str, Dict[str, Order]]
'''


'''
Q4. How does Pydantic validate deeply nested dictionaries?

Answer:
Validation is recursive:

1. Validate outer dict (user_id level)
2. Validate inner dict (order_id level)
3. Convert each inner dict → Order model
4. Validate fields inside Order

So validation happens at every level automatically.
'''


'''
Q5. What is the real-world significance of Dict[str, Dict[str, Model]]?

Answer:
It models hierarchical data:

Example:
User → Orders → Order details

Common use cases:
- E-commerce order systems
- User activity tracking
- Multi-level configurations

It allows flexible keys with strict schema enforcement.
'''


'''
Q6. How do you access deeply nested data in such structures?

Answer:
Access is intuitive:

order_book.orders["user1"]["order1"].product_id

Because:
- Outer dict → user
- Inner dict → order
- Value → Pydantic model

No manual parsing needed.
'''


'''
Q7. What happens if a nested field has wrong type?

Answer:
ValidationError is raised with full path.

Example:
orders → user1 → order1 → quantity

This pinpoints exact location of failure inside nested structure.
'''


'''
Q8. Does Pydantic support coercion in nested dicts?

Answer:
Yes, coercion works at all levels.

Example:
{"quantity": "2"} → quantity=2 ✔

But:
{"quantity": "two"} ❌ → ValidationError

Coercion is recursive but safe.
'''


'''
Q9. How is Dict[str, Model] different from List[Model]?

Answer:
Dict[str, Model]:
- Key-based access
- Dynamic identifiers (e.g., product IDs)

List[Model]:
- Index-based access
- Ordered collection

Use Dict when keys matter (IDs, names),
use List when order matters.
'''


'''
Q10. What are potential pitfalls of using nested dictionaries?

Answer:
- Deep nesting can become hard to manage
- Complex validation logic may be required
- Performance considerations for very large data

Solution:
- Use modular models
- Add validators where needed
'''


'''
🔥 Interview Killer Insight:

"Pydantic turns deeply nested JSON structures into fully validated,
type-safe Python objects with recursive parsing and precise error tracking."

Most candidates understand shallow models,
but struggle to explain deep nested validation clearly.
'''