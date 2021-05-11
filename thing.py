from datetime import datetime
from datetime import date
import pytz

### ASTRAL STUFF
# https://astral.readthedocs.io/en/latest/index.html
from astral import LocationInfo
from astral.sun import dawn, sunrise, sunset, dusk

# define test location
testloc_lat = 43.651070
testloc_long = -79.347015
testloc_tz = 'US/Eastern'
testdate=date(2021,5,9)

# set location
loc = LocationInfo("name", "region", testloc_tz, testloc_lat, testloc_long)
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


#>init the calendar
cal = Calendar()
#>compliance properties
cal.add('prodid', '-//sunscript//h4n1//')
cal.add('version', '0.1')

#foo1 = dawn(loc.observer, testdate, tzinfo=testloc_tz)
#print("one is ", foo1)
#foo2 = vDatetime(foo1  ).to_ical()
#print("two is ", foo2)
#foo3 = vDatetime(foo1)
#print("three is ", foo3)


daystart = Event()
daystart.add('summary', 'dusk to sunrise')

daystart.add('dtstart', dawn(loc.observer, testdate, tzinfo=testloc_tz))
daystart.add('dtend', sunrise(loc.observer, testdate, tzinfo=testloc_tz))

#>add the event to the calendar
cal.add_component(daystart)

print("cal is ", cal)

#>write to disk
#import tempfile, os
#directory = tempfile.mkdtemp()
#f = open(os.path.join(directory, 'test.ics'), 'wb')
#f.write(cal.to_ical())
#f.close()

# write to disk
import os
f=open('test4.txt', 'wb')
f.write(cal.to_ical())

















