from datetime import datetime, date, timezone, timedelta
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
from icalendar import Calendar, Event, vDatetime, vText

# maybe change the whole thing to use variables instead of calculating within the function, if it's going to be duplicated as strings in event descriptions anyway

#>init the calendar
cal = Calendar()
#>compliance properties
# https://www.kanzaki.com/docs/ical/prodid.html
cal.add('prodid', '-//sunscript//h4n1//')
# https://www.kanzaki.com/docs/ical/version.html
cal.add('version', '2.0')

# info vars
dawntime = dawn(loc.observer, loc_date, tzinfo=loc_tz)
risetime = sunrise(loc.observer, loc_date, tzinfo=loc_tz)
settime = sunset(loc.observer, loc_date, tzinfo=loc_tz)
dusktime = dusk(loc.observer, loc_date, tzinfo=loc_tz)
locstring = vText('{0}, {1}'.format(loc_lat, loc_long))
#suntime = settime - risetime
# timedelta doesn't allow strftime, find a way to format it better
risedesc = 'Dawn at {0}, sunrise at {1}. Total sunlight time {2}'.format(dawntime.strftime("%H:%M"), risetime.strftime("%H:%M"), str(settime - risetime))

setdesc = 'Sunset at {0}, dusk at {1}. Total sunlight time {2}'.format(settime.strftime("%H:%M"), dusktime.strftime("%H:%M"), str(settime - risetime))


# dawn to sunrise
daystart = Event()

daystart.add('summary', '↑ {0}'.format(risetime.strftime("%H:%M")))
daystart['uid'] = '{0}/SUNSCRIPT/RISE'.format(loc_date)
daystart.add('dtstamp', datetime.now(timezone.utc))
daystart['location'] = locstring
daystart['description'] = risedesc
daystart.add('dtstart', dawn(loc.observer, loc_date, tzinfo=loc_tz))
daystart.add('dtend', sunrise(loc.observer, loc_date, tzinfo=loc_tz))


#>add the event to the calendar
cal.add_component(daystart)

dayend = Event()
dayend.add('summary', '↓ {0}'.format(settime.strftime("%H:%M")))
dayend['uid'] = '{0}/SUNSCRIPT/SET'.format(loc_date)
dayend.add('dtstamp', datetime.now(timezone.utc))
dayend['location'] = locstring
dayend['description'] = setdesc
dayend.add('dtstart', sunset(loc.observer, loc_date, tzinfo=loc_tz))
dayend.add('dtend', dusk(loc.observer, loc_date, tzinfo=loc_tz))


cal.add_component(dayend)

print("cal is ", cal)

# write to disk
import os
# change to .ics
f=open('test.ics.txt', 'wb')
f.write(cal.to_ical())

















