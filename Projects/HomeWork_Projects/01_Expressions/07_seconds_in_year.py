"""
Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):
There are 5 seconds in a year!
You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.
"""




def seconds_in_year():
    DaysInYear = 365
    HoursInDay = 24
    MinutesInHour = 60
    SecondsInMinute = 60
    SecondsInYear = str(DaysInYear * HoursInDay * MinutesInHour * SecondsInMinute)
    print(f"There is {SecondsInYear} seconds in one year.") 
    
seconds_in_year()