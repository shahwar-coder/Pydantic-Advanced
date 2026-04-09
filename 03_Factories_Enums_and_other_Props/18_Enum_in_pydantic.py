from pydantic import BaseModel, ValidationError, Field
from enum import Enum


class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"


class Order(BaseModel):
    item: str
    status: OrderStatus = Field(..., description="Order status must be a valid enum value")


# ✅ Valid
order1 = Order(item="Laptop", status="shipped")
print("✅ Valid Order:", order1)
print("Status value:", order1.status)
print("Raw value:", order1.status.value)


# ❌ Invalid
try:
    order2 = Order(item="Phone", status="in_transit")
except ValidationError as e:
    print("\n❌ Validation Error:")
    print(e)




'''
======================
📌 OVERALL PURPOSE
======================
Demonstrates how Pydantic uses Enum to:
- Restrict values to a fixed set
- Validate inputs against allowed choices
- Provide safer, predictable data

======================
📌 CORE CONCEPTS
======================

class OrderStatus(str, Enum):
→ Enum defining allowed values:
   - pending
   - shipped
   - delivered

⚠️ Inheriting from str:
→ Enum behaves like string (important for JSON/APIs)

----------------------

status: OrderStatus
→ Field must be one of the enum values

Field(...)
→ Makes it required + adds metadata

======================
📌 EXECUTION FLOW
======================

VALID CASE:
order1 = Order(item="Laptop", status="shipped")

STEP 1:
Input "shipped" (string)

STEP 2:
Pydantic checks OrderStatus enum

STEP 3:
Matches → OrderStatus.shipped

STEP 4:
Stores as enum object:
status = OrderStatus.shipped

----------------------

ACCESS:

order1.status
→ OrderStatus.shipped (enum object)

order1.status.value
→ "shipped" (raw string)

⚠️ Key difference:
- .status → enum member
- .status.value → actual value

======================
📌 INVALID CASE
======================

status="in_transit"

→ Not in enum:
   ["pending", "shipped", "delivered"]

→ ❌ ValidationError raised

Error includes:
- allowed values
- invalid input
- exact field path

======================
📌 INTERNAL FLOW
======================

Input string
      ↓
Check against Enum members
      ↓
✔ Match → convert to Enum object
❌ No match → raise error

======================
📌 KEY TAKEAWAYS
======================

✔ Enum restricts values to predefined choices  
✔ Pydantic auto-converts string → Enum member  
✔ Invalid values raise clear errors  
✔ .value gives raw string for APIs  

======================
📌 INTERVIEW INSIGHT
======================

Use Enum when:
→ Field must have limited valid options

Benefits:
- Prevents invalid states
- Self-documenting code
- Safer API contracts

'''