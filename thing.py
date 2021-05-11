from datetime import datetime
from datetime import date
import pytz

### ASTRAL STUFF
# https://astral.readthedocs.io/en/latest/index.html
from astral import LocationInfo
from astral.sun import dawn, sunrise, sunset, dusk

# define test location
loc_lat = 43.651070
loc_long = -79.347015
loc_tz = 'US/Eastern'
loc_date=date(2021,5,9)

# set location
loc = LocationInfo("name", "region", loc_tz, loc_lat, loc_long)
#>timezone – The location’s time zone (a list of time zone names can be obtained from pytz.all_timezones)

### ASTRAL TESTS
#print (dawn(loc.observer, testdate, tzinfo=testloc_tz))
#print (sunrise(loc.observer, testdate, tzinfo=testloc_tz))
# print (sunset(loc.observer, testdate, tzinfo=testloc_tz))
# print (dusk(loc.observer, testdate, tzinfo=testloc_tz))
# this works ^

### ICAL STUFF

# https://icalendar.readthedocs.io/en/latest/usage.html#example
from icalendar import Calendar, Event, vDatetime

# maybe change the whole thing to use variables instead of calculating within the function, if it's going to be duplicated as strings in event descriptions anyway

#>init the calendar
cal = Calendar()
#>compliance properties
cal.add('prodid', '-//sunscript//h4n1//')
cal.add('version', '0.1')

# info vars
risetime = sunrise(loc.observer, loc_date, tzinfo=loc_tz).strftime("%H:%M:%S")
settime = sunset(loc.observer, loc_date, tzinfo=loc_tz).strftime("%H:%M:%S")

# dawn to sunrise
daystart = Event()
daystart.add('summary', '↑ {0}'.format(risetime))
daystart.add('dtstart', dawn(loc.observer, loc_date, tzinfo=loc_tz))
daystart.add('dtend', sunrise(loc.observer, loc_date, tzinfo=loc_tz))

#>add the event to the calendar
cal.add_component(daystart)

dayend = Event()
dayend.add('summary', '↓ {0}'.format(settime))
dayend.add('dtstart', sunset(loc.observer, loc_date, tzinfo=loc_tz))
dayend.add('dtend', dusk(loc.observer, loc_date, tzinfo=loc_tz))
cal.add_component(dayend)

print("cal is ", cal)

# write to disk
import os
# change to .ics
f=open('test.txt', 'wb')
f.write(cal.to_ical())

















