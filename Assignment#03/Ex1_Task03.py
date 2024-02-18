#  Python program to extract year, month, date and time using Lambda.
from datetime import datetime

dateTime = datetime.now()
print (dateTime)


currYear = lambda dt: dt.year # .year k through year nikal lnge usme se
currMonth = lambda dt: dt.month
currDay = lambda dt: dt.day
currTime = lambda dt: dt.time() # baghair () k problem arhi --> maam se pochna


year = currYear(dateTime)
month = currMonth(dateTime)
day = currDay(dateTime)
time = currTime(dateTime)

print("Current Year:", year)
print("Current Month:", month)
print("Current Day:", day)
print("Current Time:", time)
