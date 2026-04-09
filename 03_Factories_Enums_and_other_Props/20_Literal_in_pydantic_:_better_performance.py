'''
Same code, which was used for Enum, but with Literal here.
'''
from pydantic import BaseModel, ValidationError, Field
from typing import Literal


class Order(BaseModel):
    item: str
    status: Literal["pending", "shipped", "delivered"] = Field(
        ..., description="Order status must be one of the allowed values"
    )


# ✅ Valid
order1 = Order(item="Laptop", status="shipped")
print("✅ Valid Order:", order1)
print("Status:", order1.status)


# ❌ Invalid
try:
    order2 = Order(item="Phone", status="in_transit")
except ValidationError as e:
    print("\n❌ Validation Error:")
    print(e)


'''
📌 PURPOSE
Restricts a field to fixed values using Literal.

📌 CORE
status: Literal["pending", "shipped", "delivered"]

→ Only these exact strings are allowed  
→ No other value accepted

📌 FLOW
Input "shipped"
→ Matches allowed values ✔
→ Stored as plain string (not Enum)

Input "in_transit"
→ Not in allowed list ❌
→ ValidationError

📌 KEY DIFFERENCE (vs Enum)
Literal:
✔ Simpler
✔ Stored as raw string

Enum:
✔ More structured
✔ Has .value, methods

📌 TAKEAWAYS
✔ Literal enforces strict allowed values  
✔ Lightweight alternative to Enum  
✔ Useful for simple fixed options  

'''