from pydantic import BaseModel
from enum import Enum


class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"


class Order(BaseModel):
    item: str
    status: OrderStatus


class Shipment(BaseModel):
    tracking_id: str
    status: OrderStatus   # ✅ reused here


order = Order(item="Laptop", status="pending")
shipment = Shipment(tracking_id="TRK123", status="shipped")

print(order)
print(shipment)