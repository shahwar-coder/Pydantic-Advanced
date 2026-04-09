from pydantic import BaseModel, Field

class Product(BaseModel):
    price: float = Field(gt=0, le=1000)

Product(price=500)   # ✅
Product(price=-10)   # ❌

# gt = greater than
# le = less than or equal