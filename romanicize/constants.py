"""
romanicize.constants

These are all the constants being used by this library
"""

# In theory, you could provide bigger numbers by addition of extra letters, but if you're
# really trying to write a roman numeral 4,000,000 or above, perhaps you should rethink life.
MAX_INTEGER = 3999999
OVERLINE = '\u0305'

LETTERS_TO_NUMERALS = {
    'M̅': 1000000,
    'D̅': 500000,
    'C̅': 100000,
    'L̅': 50000,
    'X̅': 10000,
    'V̅': 5000,
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

# These are formatted this way for ease of reviewing the core numbers/letters
BASE_INTEGERS = (
    1000000, 900000,
    500000,  400000,
    100000,  90000,
    50000,   40000,
    10000,   9000,
    5000,    4000,
    1000,    900,
    500,     400,
    100,     90,
    50,      40,
    10,      9,
    5,       4,
    1
)

BASE_NUMERALS = (
    'M̅', 'C̅M̅',
    'D̅', 'C̅D̅',
    'C̅', 'X̅C̅',
    'L̅', 'X̅L̅',
    'X̅', 'MX̅',
    'V̅', 'MV̅',
    'M', 'CM',
    'D', 'CD',
    'C', 'XC',
    'L', 'XL',
    'X', 'IX',
    'V', 'IV',
    'I'
)
