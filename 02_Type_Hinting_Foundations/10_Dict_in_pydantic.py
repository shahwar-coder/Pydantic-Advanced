from pydantic import BaseModel, ValidationError
from typing import Dict


class Product(BaseModel):
    name: str
    price: float


class ProductCatalog(BaseModel):
    products: Dict[str, Product]


try:
    catalog = ProductCatalog(
        products={
            "p1": {"name": "tea", "price": 4.99},
            "p2": {"name": "coffee", "price": 3.99}
        }
    )

    print("✅ Catalog:", catalog)

    print("\n--- Access Data ---")
    print("All products:", catalog.products)
    print("Single product:", catalog.products["p1"])
    print("Product name:", catalog.products["p1"].name)

except ValidationError as e:
    print("❌ Validation Error:")
    print(e)


# Dict[str, Model] = dynamic keys + structured values