from pydantic import BaseModel, ValidationError, Field
from typing import Set


class UniqueNumbers(BaseModel):
    values: Set[int] = Field(min_length=2, max_length=5)


try:
    data = UniqueNumbers(values={1, 2, 3, 3, 4})
    print("✅ Output:", data)

except ValidationError as e:
    print("❌ Validation Error:")
    print(e)


# ✅ Output: values={1, 2, 3, 4}


# -=-=-=-=


'''
======================
📌 OVERALL PURPOSE
======================
Demonstrates how Pydantic:
1. Handles Set type (ensures uniqueness)
2. Applies constraints using Field (min_length, max_length)
3. Automatically removes duplicates during parsing

======================
📌 CORE CONCEPTS
======================

values: Set[int]
→ A set:
   - Stores UNIQUE elements only
   - Automatically removes duplicates

Field(min_length=2, max_length=5)
→ Constraints on collection size:
   - At least 2 items
   - At most 5 items

======================
📌 EXECUTION FLOW
======================

Input:
values={1, 2, 3, 3, 4}

STEP 1: Type Enforcement
→ Pydantic sees Set[int]
→ Converts input into a Python set

STEP 2: Duplicate Removal
→ Set automatically removes duplicates:
   {1, 2, 3, 3, 4} → {1, 2, 3, 4}

⚠️ Important:
Deduplication happens BEFORE validation

STEP 3: Validation (Field constraints)
→ Length check:
   len({1,2,3,4}) = 4

Check:
✔ min_length=2 → pass
✔ max_length=5 → pass

STEP 4: Model Creation
→ Final stored value:
   values = {1, 2, 3, 4}

======================
📌 OUTPUT
======================
values={1, 2, 3, 4}

→ Duplicate "3" removed automatically

======================
📌 ERROR SCENARIOS
======================

1. Too few elements:
values={1}
→ ❌ Fails min_length

2. Too many elements:
values={1,2,3,4,5,6}
→ ❌ Fails max_length

3. Wrong type:
values={"a", "b"}
→ ❌ int parsing fails

======================
📌 KEY TAKEAWAYS
======================

✔ Set enforces uniqueness automatically  
✔ Deduplication happens before validation  
✔ Field constraints apply to collection size  
✔ Clean way to enforce unique + bounded data  

======================
📌 INTERVIEW INSIGHT
======================

Use Set when:
→ You need uniqueness + validation

Common use cases:
- Tags
- IDs
- Unique items in request payloads
'''