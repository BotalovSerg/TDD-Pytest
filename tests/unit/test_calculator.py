"""Tests for calculator module."""

from src.tdd_project.calculator import add


def test_add_positive_numbers():
    """Test addition of positive numbers."""
    result = add(2, 3)
    assert result == 5


def test_add_negative_numbers():
    """Test addition of negative numbers."""
    result = add(-1, -2)
    assert result == -3


def test_add_zero():
    """Test addition with zero."""
    result = add(5, 0)
    assert result == 5
