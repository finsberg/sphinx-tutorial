"""
This is an example module for the sphinx tutorial
"""
__autour__ = 'Henrik Finsberg'


def add(a, b):
    """Add two numbers

    Arguments
    ---------
    a : float
        The first number
    b : float
        The second number
    
    Returns
    -------
    c : float
        The sum of the two input arguments
    """
    c = a + b
    return c


def divide(a, b):
    r"""Divide two numbers

    .. math::

        c = \frac{a}{b}

    .. note::

        If :math:`b` is zero it will raise a ZeroDivisionError

    Arguments
    ---------
    a : float
        The numerator
    b : float
        The denominator

    Returns
    -------
    c : float
        The fraction
    """
    return a / b
