from backend.utils.services import division
import pytest


@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        (10, 5, 2),
        (20, 4, 5),
        (9, 2, 4.5),
        (-30, 3, -10),
    ],
)
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize(
    "expected_exception, diveder",
    [
        (ZeroDivisionError, 0),
        (TypeError, "3"),
    ],
)
def test_division_with_error(expected_exception, diveder):
    with pytest.raises(expected_exception):
        division(7, diveder)
