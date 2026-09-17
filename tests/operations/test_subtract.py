from calculator import subtract


def test_subtract():
    """Subtracting two integers returns their difference."""
    result = subtract(10, 4)
    assert result == 6