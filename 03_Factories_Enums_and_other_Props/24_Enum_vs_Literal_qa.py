'''
Enum vs Literal — Deep Interview Q&A (Concept + Design 🔥)
References: :contentReference[oaicite:0]{index=0} , :contentReference[oaicite:1]{index=1}
'''


'''
1. Why is Enum preferred over Literal in scalable systems?

Answer:
Enum is reusable across multiple models.

Example:
Order.status and Shipment.status both use OrderStatus Enum.

With Literal:
→ You would repeat Literal["pending", "shipped", "delivered"] everywhere ❌

Problems:
- Code duplication
- Harder to maintain
- Risk of inconsistency

Enum solves this:
✔ Single source of truth
✔ Reusable across entire codebase
'''


'''
2. How does Enum support behavior while Literal does not?

Answer:
Enum is a class → can have methods.

Example:
class Role(Enum):
    def is_admin(self):
        ...

This allows:
✔ Business logic inside the type
✔ Cleaner design

Literal:
❌ Cannot define methods
❌ Only static value constraint

This is a major design advantage of Enum.
'''


'''
3. In a real system, when would Literal become a bad choice?

Answer:
Literal becomes problematic when:
- Values are reused across multiple places
- Business logic is needed
- Domain grows over time

Example:
Status used in:
- Orders
- Shipments
- Payments

Using Literal:
→ Duplication everywhere ❌

Using Enum:
→ Centralized + maintainable ✔
'''


'''
4. Can Enum and Literal behave differently in validation and type safety?

Answer:
Yes.

Enum:
- Stronger abstraction (type + behavior)
- Values are tied to a class
- Better for domain modeling

Literal:
- Only value matching
- No abstraction
- Less expressive

So:
Enum → domain-level modeling
Literal → simple validation constraint
'''


'''
🔥 Interview Killer Insight:

"Literal is for constraints,
Enum is for domain modeling."

Senior engineers prefer Enum because it:
✔ scales
✔ supports behavior
✔ avoids duplication
'''