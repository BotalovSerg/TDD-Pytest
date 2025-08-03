from backend.core import OrderLine, Batch
from backend.core.domain_model.exceptions import OutOfStock


def allocate(line: OrderLine, batches: list[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Артикула {line.sku} нет в наличии")
