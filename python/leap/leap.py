def is_leap_year(year):
    """ (int) - > bool

    Return True if year is leap and False if it's not.

    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2015)
    False
    """

    return ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0)
