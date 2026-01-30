def is_leap_year(year):
    if year % 400 == 0: #all years divisable by 400 are leap years
        return True
    elif year % 100 == 0: #years not divisable by 400, but divisable by 100 are NOT leap years
        return False
    elif year % 4 == 0: #what's left is a leap year if divisable by 4
        return True
    else: #what's left is not a leap year
        return False

for num in sorted(set([
    2004
    ,6767
    ,2026
    ,2100
    ,1999
    ,1999
    ,1999
    ,1999
    ,6767
    ,6768
    ,2028
    ,2103
    ,2003
    ,2004
    ,2005
    ,2006
    ,2034
    ,2109
    ,2009
    ,2010
    ,2011
    ,2012
])):
    print((f'{num}:{is_leap_year(num)}'))