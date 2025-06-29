"""
romanicize.converter

These are the 2 core conversion functions
"""

import typing as t

from .constants import (
    LETTERS_TO_NUMERALS,
    BASE_INTEGERS,
    BASE_NUMERALS,
    MAX_INTEGER,
    OVERLINE,
)


def to_numeral(integer: int) -> str:
    """Convert an integer to a Roman numeral."""

    if not isinstance(integer, int) or isinstance(integer, bool):
        raise ValueError(
            f"Provided integer was not an integer: {integer} {type(integer)}"
        )

    if not 0 < integer <= MAX_INTEGER:
        raise ValueError(f"Integer must be between 1 and {MAX_INTEGER}")

    # Numbers 4000 and above use a vinculum (aka: overline) above a standard letter, to denote
    # having been multiplied by 1000. However, this is difficult to produce easily with a
    # standard keyboard. If you wish to support them, be prepared for unicode pain.

    numeral = []
    for index, num in enumerate(BASE_INTEGERS):
        count = int(integer / num)
        numeral.append(BASE_NUMERALS[index] * count)
        integer -= num * count

    return "".join(numeral)


def _get_value(string: str, index: int) -> t.Tuple[int, int]:
    """
    Returns the value of the letter at the specified index, allowing for compound characters
    """

    try:
        maybe_compound_letter = string[index]
        offset = 1

    except IndexError:
        return (None, 0)

    try:
        if string[index + 1] == OVERLINE:
            offset = 2
            maybe_compound_letter = maybe_compound_letter + OVERLINE

    except IndexError:
        pass

    return (LETTERS_TO_NUMERALS[maybe_compound_letter], offset)


def to_int(numeral: str) -> int:
    """Convert a Roman numeral to an integer."""

    if not isinstance(numeral, str):
        raise ValueError(
            f"Provided numeral was not a string: {numeral} {type(numeral)}"
        )

    numeral = numeral.upper()

    integer = 0
    for index, char in enumerate(numeral):
        if char == OVERLINE:
            continue

        try:
            (value, offset) = _get_value(numeral, index)
            (next_value, offset) = _get_value(numeral, index + offset)

            # If the next place holds a larger number, this value is negative
            if next_value and next_value > value:
                integer -= value
            else:
                integer += value

        except KeyError as exc:
            raise ValueError(
                f"Provided numeral is not a valid Roman numeral: {numeral}"
            ) from exc

    # easiest test for validity...
    if to_numeral(integer) != numeral:
        raise ValueError(f"Provided numeral is not a valid Roman numeral: {numeral}")

    return integer
