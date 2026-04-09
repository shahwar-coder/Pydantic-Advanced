from pydantic import BaseModel, Field, ValidationError
from typing import Tuple


class Numbers(BaseModel):
    values: Tuple[int, ...] = Field(min_length=2, max_length=4)


try:
    data = Numbers(values=(1, 2, 3))
    print("✅ Output:", data)

except ValidationError as e:
    print("❌ Validation Error:")
    print(e)


'''
======================
📌 OVERALL PURPOSE
======================
Shows how Pydantic handles:
1. Tuple type (ordered, immutable collection)
2. Variable-length tuples using Tuple[int, ...]
3. Length constraints via Field (min_length, max_length)

======================
📌 CORE CONCEPTS
======================

values: Tuple[int, ...]
→ Tuple of integers with variable length
→ "..." means: any number of int elements

Tuple properties:
✔ Ordered
✔ Immutable
✔ Allows duplicates (unlike set)

Field(min_length=2, max_length=4)
→ Enforces size constraints on the tuple

======================
📌 EXECUTION FLOW
======================

Input:
values=(1, 2, 3)

STEP 1: Type Validation
→ Pydantic checks:
   - Is it iterable? ✔
   - Are all elements int? ✔

STEP 2: Tuple Handling
→ Input already a tuple → no conversion needed
→ (If list was given, it would be converted to tuple)

STEP 3: Length Validation
→ len((1,2,3)) = 3

Check:
✔ min_length=2 → pass
✔ max_length=4 → pass

STEP 4: Model Creation
→ Stored as:
   values = (1, 2, 3)

======================
📌 OUTPUT
======================
values=(1, 2, 3)

======================
📌 ERROR SCENARIOS
======================

1. Too short:
values=(1,)
→ ❌ fails min_length

2. Too long:
values=(1,2,3,4,5)
→ ❌ fails max_length

3. Wrong type:
values=(1, "a")
→ ❌ element validation fails

======================
📌 KEY DIFFERENCE (Tuple vs Set)
======================

Tuple:
✔ Ordered
✔ Allows duplicates
✔ Immutable

Set:
✔ Unordered
✔ Removes duplicates
✔ Mutable

======================
📌 KEY TAKEAWAYS
======================

✔ Tuple[int, ...] allows flexible-length integer tuples  
✔ Field constraints apply to tuple length  
✔ Pydantic validates each element + structure  
✔ Accepts list input → converts to tuple  

======================
📌 INTERVIEW INSIGHT
======================

Use Tuple when:
→ Order matters
→ Data should not change (immutability)
→ Fixed/controlled sequence structure needed

'''