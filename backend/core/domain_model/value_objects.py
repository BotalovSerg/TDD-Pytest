from typing import NewType
from dataclasses import dataclass

Sku = NewType("Sku", str)  # stock-keeping unit
Quantity = NewType("Quantity", int)  # количество (quantity)
Reference = NewType("Reference", str)  # ссылкой на заказ (order reference)


@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: Sku
    qty: Quantity
