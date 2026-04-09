from pydantic import BaseModel, Field
from typing import Any


class APIResponse(BaseModel):
    status: str = Field(..., description="Response status")
    data: Any = Field(..., description="Dynamic response payload")


# ✅ Different types of responses
res1 = APIResponse(status="success", data={"user": "Rahul", "age": 25})
res2 = APIResponse(status="success", data=[1, 2, 3, 4])
res3 = APIResponse(status="success", data="Operation completed")

print(res1)
print(res2)
print(res3)


'''
======================
📌 OVERALL PURPOSE
======================
Demonstrates use of:
- Any type for flexible/dynamic data
- Field(...) to mark required fields + add metadata

Useful for generic API response wrappers.

======================
📌 CORE CONCEPTS
======================

status: str = Field(...)
→ Required field ("..." means mandatory)

data: Any
→ Accepts ANY type:
   - dict
   - list
   - string
   - etc.

⚠️ No validation on structure of "data"

======================
📌 EXECUTION FLOW
======================

res1 → data = dict
res2 → data = list
res3 → data = string

→ Pydantic:
   - Validates "status" is str ✔
   - Accepts "data" as-is (no strict checks)

======================
📌 OUTPUT
======================

APIResponse(status='success', data={'user': 'Rahul', 'age': 25})
APIResponse(status='success', data=[1, 2, 3, 4])
APIResponse(status='success', data='Operation completed')

======================
📌 KEY TAKEAWAYS
======================

✔ Any allows fully flexible payloads  
✔ Field(...) makes fields required  
✔ No validation inside "data" → use carefully  
✔ Common pattern for API responses  

======================
📌 INTERVIEW INSIGHT
======================

Use Any when:
→ Response structure is dynamic

Avoid when:
→ You need strict validation (use models instead)
'''