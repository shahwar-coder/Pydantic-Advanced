from pydantic import BaseModel, ValidationError
from typing import Dict


class Order(BaseModel):
    product_id: str
    quantity: int


class OrderBook(BaseModel):
    orders: Dict[str, Dict[str, Order]]


try:
    order_book = OrderBook(
        orders={
            "user1": {
                "order1": {"product_id": "p1", "quantity": 2},
                "order2": {"product_id": "p2", "quantity": 1}
            },
            "user2": {
                "order3": {"product_id": "p3", "quantity": 5}
            }
        }
    )

    print("✅ OrderBook:", order_book)

    print("\n--- Access Data ---")
    print("All orders:", order_book.orders)
    print("User1 Orders:", order_book.orders["user1"])
    print("Specific Order:", order_book.orders["user1"]["order1"])
    print("Product ID:", order_book.orders["user1"]["order1"].product_id)

except ValidationError as e:
    print("❌ Validation Error:")
    print(e)



# -=-=-=-=-=-=-=-=



'''
======================
📌 OVERALL PURPOSE
======================
This code demonstrates how Pydantic handles:
1. Deeply nested data structures
2. Dictionaries of dictionaries
3. Automatic conversion of nested dicts into Pydantic models

It simulates a real-world scenario:
👉 Order management system (like e-commerce)

Structure:
User → Orders → Individual Order details

======================
📌 DATA STRUCTURE OVERVIEW
======================

orders = {
    "user_id": {
        "order_id": Order(...)
    }
}

So the hierarchy is:

OrderBook
  └── orders (Dict)
        └── user_id (str)
              └── order_id (str)
                    └── Order (Pydantic Model)

======================
📌 STEP-BY-STEP FLOW
======================

1. IMPORTS
-----------
from pydantic import BaseModel, ValidationError
from typing import Dict

→ Dict is used for defining nested mappings


2. ORDER MODEL (INNER MODEL)
----------------------------
class Order(BaseModel):
    product_id: str
    quantity: int

→ Represents a single order

Fields:
- product_id → string (e.g., "p1")
- quantity → integer

⚠️ This is the "leaf node" in the data structure


3. ORDERBOOK MODEL (OUTER MODEL)
--------------------------------
class OrderBook(BaseModel):
    orders: Dict[str, Dict[str, Order]]

Breakdown of type:

Dict[
    str,                 → user_id
    Dict[
        str,             → order_id
        Order            → actual order object
    ]
]

So:
orders["user1"]["order1"] → Order object

⚠️ Important:
Pydantic will automatically convert inner dictionaries into Order objects.


4. OBJECT CREATION
------------------
order_book = OrderBook(
    orders={
        "user1": {
            "order1": {"product_id": "p1", "quantity": 2},
            "order2": {"product_id": "p2", "quantity": 1}
        },
        "user2": {
            "order3": {"product_id": "p3", "quantity": 5}
        }
    }
)

→ Input is PURE DICTIONARY (like JSON from API)

→ Pydantic does recursive parsing:

STEP 1: Validate "orders" is a dict
STEP 2: Iterate over each user (user1, user2)
STEP 3: For each user:
        - Validate inner dict
        - For each order:
            Convert dict → Order object

Example conversion:
{"product_id": "p1", "quantity": 2}
        ↓
Order(product_id="p1", quantity=2)


5. INTERNAL CONVERSION FLOW
---------------------------

Raw Input (Nested Dict)
        ↓
OrderBook initialization
        ↓
Validate outer dict (users)
        ↓
Validate inner dict (orders)
        ↓
Convert each order dict → Order model
        ↓
Store structured data


6. PRINTING FULL OBJECT
-----------------------
print(order_book)

→ Output shows:
OrderBook(
    orders={
        'user1': {'order1': Order(...), ...},
        ...
    }
)

⚠️ Notice:
Inner dict values are now Order objects (NOT raw dicts)


7. ACCESSING DATA
-----------------

(A) All orders:
order_book.orders

→ Returns full nested dictionary

(B) User1 Orders:
order_book.orders["user1"]

→ Dict of that user's orders

(C) Specific Order:
order_book.orders["user1"]["order1"]

→ Returns an Order object

(D) Access field:
order_book.orders["user1"]["order1"].product_id

→ "p1"

⚠️ Key Insight:
Deep access works seamlessly because Pydantic converted everything properly.


8. ERROR HANDLING
-----------------

If invalid data is passed:

Examples:
- quantity="two" ❌ (should be int)
- missing product_id ❌
- wrong structure ❌

→ Pydantic raises ValidationError with detailed path:

Example error path:
orders → user1 → order1 → quantity

This makes debugging extremely easy.


======================
📌 WHY THIS IS IMPORTANT (INTERVIEW GOLD)
======================

1. Handles COMPLEX JSON structures
   → Very common in APIs, microservices, configs

2. Recursive validation
   → Deep validation without manual loops

3. Automatic model conversion
   → Dict → Model (nested)

4. Strong typing at every level
   → Prevents bad data deep inside structures

5. Real-world use cases:
   - Order systems
   - User activity logs
   - Nested API responses
   - Config management


======================
📌 KEY TAKEAWAYS
======================

✔ Pydantic supports deeply nested dictionaries  
✔ Automatically converts inner dicts → BaseModel instances  
✔ Recursive validation ensures full data integrity  
✔ Accessing nested data is clean and type-safe  
✔ Errors include full path (very useful in debugging)  

======================
📌 ADVANCED INSIGHT
======================

Under the hood (Pydantic v2):

→ Uses pydantic-core (Rust engine)
→ Builds a validation schema for nested structures
→ Applies validation recursively with high performance

This is why even deeply nested structures are:
✔ Fast
✔ Reliable
✔ Scalable
'''