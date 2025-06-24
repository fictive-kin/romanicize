"""
tests.test_conversions

"""

import pytest
import romanicize


CORE_CONVERSIONS = [
    (1000000, "M̅"),
    (900000, "C̅M̅"),
    (500000, "D̅"),
    (400000, "C̅D̅"),
    (100000, "C̅"),
    (90000, "X̅C̅"),
    (50000, "L̅"),
    (40000, "X̅L̅"),
    (10000, "X̅"),
    (9000, "MX̅"),
    (5000, "V̅"),
    (4000, "MV̅"),
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

RANDOM_CONVERSIONS = [
    (2109, "MMCIX"),
    (23, "XXIII"),
    (6736, "V̅MDCCXXXVI"),
    (3987947, "M̅M̅M̅C̅M̅L̅X̅X̅X̅V̅MMCMXLVII"),
    (50005, "L̅V"),
    (2444444, "M̅M̅C̅D̅X̅L̅MV̅CDXLIV"),
]


@pytest.mark.parametrize("integer,numeral", CORE_CONVERSIONS + RANDOM_CONVERSIONS)
def test_to_numeral(integer, numeral):
    """Tests that the expected strings are returned from the conversion"""

    assert romanicize.to_numeral(integer) == numeral


@pytest.mark.parametrize("integer,numeral", CORE_CONVERSIONS + RANDOM_CONVERSIONS)
def test_to_int(integer, numeral):
    """Tests that the expected ints are returned from the conversion"""

    assert romanicize.to_int(numeral) == integer


@pytest.mark.parametrize("integer", [(-1,), (4000000,), (5000001,), ("XXV",)])
def test_to_int_errors(integer):
    """Tests that a ValueError is thrown for an invalid integer"""

    with pytest.raises(ValueError):
        romanicize.to_int(integer)


@pytest.mark.parametrize("numeral", [("XXIMCCM",), ("VIIR",), (25,)])
def test_to_numeral_errors(numeral):
    """Tests that a ValueError is thrown for an invalid numeral"""

    with pytest.raises(ValueError):
        romanicize.to_numeral(numeral)
