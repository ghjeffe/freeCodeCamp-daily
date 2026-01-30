def is_leap_year(year):
    if year % 400 != 0:
        return False
    if year % 100 != 0:
        return False
        
    if year % 4 != 0:
        return False
        
    else:
        return True 
for num in [2004,6767,2026,2100,1999]:
    print((f'{num}:{is_leap_year(num)}'))