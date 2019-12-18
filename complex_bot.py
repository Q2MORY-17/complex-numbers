"""The point of this module is to provide quick complexconversion using
degrees rather than radians to speed up calculations.
a recommendation would be do import the functions like so:

>>> from complex_bot import rect_form as rf
>>> from complex_bot import polar_form as pf

thus, making the functions faster to use
ex:

>>> rf(5, 53.13)
(3+4j)

In this document, we will use the actual functions name as to not confuse
the reader.
"""

from cmath import polar, rect
from math import degrees, radians

def rect_form(x, y):
    """
    This function takes in two inputs and returns a complex number.
    x = magnitude
    y = angle in degrees
    ex:

    >>> y = rect_form(5, 53.13)
    >>> y
    (3+4j)

    This function returns a complex number so it is suitable for further
    calculations.
    However, it is truncated for quick representation and therefore not
    very precise. you may increase the resolution as you wish by changing the
    rounding resolution to a larger number if you seek precision.
    ex:

    a = round(z.real,4)+round(z.imag,4)*1j
    will give you:
    >>> y = rect_form(6, 73.13)
    >>> y
    (1.7412+5.7418j)
    """
    z = rect(x, radians(y))
    a = round(z.real,2)+round(z.imag,2)*1j
    return(a)

def polar_form(x):
    """
    This function takes in a complex expression and returns its polar form.
    >>> polar_form(y) #where y is a complex number
    
    This function can also return a complex input to show its polar
    representation.
    ex:
    
    >>> polar_form(3+4j)
    (5.0, 53.13)

    WARNING: this function generates a tuple as answer and is therefore not
    suited for further calculations. unless you want to manipulate
    it as a tuple.
    """
    z = polar(x)
    return(round(z[0],2),round(degrees(z[1]),2))
    
