from cmath import polar, rect
from math import degrees, radians

def complex(x, y, z=0):
    if z is 0:
        b = rect(x, radians(y))
        a= round(b.real,6)+round(b.imag,6)*1j
        return(a)

    elif z is 1:
        b = polar(x+y*1j)
        return(round(b[0],2),round(degrees(b[1]),2))

    else :
        print("input error")