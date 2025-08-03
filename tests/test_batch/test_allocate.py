import pytest
from datetime import date

from backend.core import Batch, OrderLine
from backend.core.domain_model.services import allocate
from backend.core.domain_model.exceptions import OutOfStock


def test_raises_out_of_stock_exception_if_connot_allocate():
    batch = Batch("batch1", "SMALL-FORK", 10, eta=date.today())
    allocate(OrderLine("order1", "SMALL-FORK", 10), [batch])

    with pytest.raises(OutOfStock, match=r"SMALL-FORK"):
        allocate(OrderLine("order2", "SMALL-FORK", 1), [batch])
