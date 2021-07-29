
Roman Numeral Conversion Utilities
==================================

This is a utility module for converting from and to Roman numerals. It supports
numbers upto 3,999,999, using the vinculum_ to denote multiplication by
``1000``. (i.e.: ``X`` is ``10`` while ``X̅`` is ``10000``.) The only letter
that this does not apply to is ``I``, as ``M`` already existed for ``1000``.

Special credit goes to Paul M. Winkler, for the original basis for a large
chunk of the core converter functions as written in the `Python Cookbook`_.


Quick Start
-----------

Install the package::

    pip3 install romanicize

Once installed, a command line utility is available to your shell::

    $ romanicize 2021
    MMXXI
    $ romanicize MMXIX
    2019

With a Python script, convert from an integer to a Roman numeral::

    from romanicize import to_numeral

    print(to_numeral(2021))  # Outputs: MMXXI

Within a Python script, convert from a Roman numeral to an integer::

    from romanicize import to_int

    print(to_int('MV̅DLXXVIII'))  # Outputs: 4578

.. _vinculum: https://en.wikipedia.org/wiki/Roman_numerals#Vinculum
.. _Python Cookbook: https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html
