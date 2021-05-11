from datetime import datetime, date, timezone, timedelta
import pytz

### ASTRAL STUFF
# https://astral.readthedocs.io/en/latest/index.html
from astral import LocationInfo
from astral.sun import dawn, sunrise, sunset, dusk

### ALL USER INPUT HERE
# define location and date range
loc_name = 'Toronto'
# what's the point of the region definition?
loc_region = 'Ontario'
loc_lat = 43.651070
loc_long = -79.347015
# is there a better way to define timezone?
loc_tz = 'America/Toronto'
date_start = date(2021, 1, 1)
# daterange function is exclusive of end date
date_end = date(2022, 1, 1)
output_filename = 'sun_{0}_{1}_{2}.ics'.format(loc_name.lower(), date_start, date_end)

# set location
loc = LocationInfo(loc_name, loc_region, loc_tz, loc_lat, loc_long)
#>timezone – The location’s time zone (a list of time zone names can be obtained from pytz.all_timezones)

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

### FOR LOOP SHOULD START HERE
# from https://stackoverflow.com/a/1060330
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
# could possibly also use dateutil module

for loc_date in daterange(date_start, date_end):

    ### time vars
    
    dawntime = dawn(loc.observer, loc_date, tzinfo=loc_tz)
    risetime = sunrise(loc.observer, loc_date, tzinfo=loc_tz)
    settime = sunset(loc.observer, loc_date, tzinfo=loc_tz)
    dusktime = dusk(loc.observer, loc_date, tzinfo=loc_tz)

    ### description vars
    
    # could move coordinates to 'GEO' property, see https://www.kanzaki.com/docs/ical/geo.html
    locstring = vText('{0} / {1}, {2}'.format(loc_name, loc_lat, loc_long))
    
    # timedelta doesn't allow strftime, find a way to format it better, see https://stackoverflow.com/questions/538666/format-timedelta-to-string
    risedesc = 'Dawn at {0}, sunrise at {1}. Total sunlight time {2}'.format(dawntime.strftime("%H:%M"), risetime.strftime("%H:%M"), str(settime - risetime))

    setdesc = 'Sunset at {0}, dusk at {1}. Total sunlight time {2}'.format(settime.strftime("%H:%M"), dusktime.strftime("%H:%M"), str(settime - risetime))

    # dawn to sunrise
    daystart = Event()
    daystart.add('summary', '↑ {0}'.format(risetime.strftime("%H:%M")))
    daystart['uid'] = '{0}/SUNSCRIPT/SUNRISE/{1}'.format(loc_date, loc_name.upper())
    daystart.add('dtstamp', datetime.now(timezone.utc))
    daystart['location'] = locstring
    daystart['description'] = risedesc
    daystart.add('dtstart', dawntime)
    daystart.add('dtend', risetime)
    cal.add_component(daystart)

    # sunset to dusk
    dayend = Event()
    dayend.add('summary', '↓ {0}'.format(settime.strftime("%H:%M")))
    dayend['uid'] = '{0}/SUNSCRIPT/SUNSET/{1}'.format(loc_date, loc_name.upper())
    dayend.add('dtstamp', datetime.now(timezone.utc))
    dayend['location'] = locstring
    dayend['description'] = setdesc
    dayend.add('dtstart', settime)
    dayend.add('dtend', dusktime)
    cal.add_component(dayend)

# write to disk
import os
f=open(output_filename, 'wb')
f.write(cal.to_ical())

















