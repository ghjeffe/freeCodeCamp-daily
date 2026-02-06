import time #time.time to get unix timestamp
from datetime import datetime, timedelta

def odd_or_even_day(timestamp: float) -> str:
    date_object = datetime.fromtimestamp(timestamp)

    if date_object.day % 2 > 0:
        return "odd"
    else:
        return "even"

print(odd_or_even_day(1769472000000))
print(odd_or_even_day(1769444440000))