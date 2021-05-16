from datetime import datetime, date, timezone, timedelta
import pytz

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
output_filename = 'noon_{0}_{1}_{2}.ics'.format(loc_name.lower(), date_start, date_end)
# how long before and after the moment of noon should the calendar event last?
### look up which format this should be in
### how are times added and subtracted in python
### maybe use time at certain angles near noon instead
#event_time_before = 
#event_time_after = 

### ASTRAL STUFF
# https://astral.readthedocs.io/en/latest/index.html
from astral import LocationInfo
from astral.sun import noon

# set location
loc = LocationInfo(loc_name, loc_region, loc_tz, loc_lat, loc_long)

### ICAL STUFF
# https://icalendar.readthedocs.io/en/latest/usage.html#example
from icalendar import Calendar, Event, vDatetime, vText

#>init the calendar
cal = Calendar()
#>compliance properties
# https://www.kanzaki.com/docs/ical/prodid.html
cal.add('prodid', '-//sunscript//h4n1//')
# https://www.kanzaki.com/docs/ical/version.html
cal.add('version', '2.0')

# from https://stackoverflow.com/a/1060330
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

for loc_date in daterange(date_start, date_end):
    
    time_noon = noon(loc.observer, loc_date, tzinfo=loc_tz)
    
    ### event description vars
    
    event_title_noon = "☼ {0}".format(time_noon.strftime("%H:%M"))
    event_location = vText('{0} / {1}, {2}'.format(loc_name, loc_lat, loc_long))
    # add something about time at certain angles
    event_desc_noon = "Solar noon at {0}".format(time_noon.strftime("%H:%M"))
    
    daynoon = Event()
    daynoon.add('summary', event_title_noon)
    daynoon['uid'] = '{0}/SUNSCRIPT/SOLARNOON/{1}'.format(loc_date, loc_name.upper())
    daynoon.add('dtstamp', datetime.now(timezone.utc))
    daynoon['location'] = event_location
    daynoon['description'] = event_desc_noon
    # fix below
    daynoon.add('dtstart', time_noon)
    daynoon.add('dtend', time_noon)
    cal.add_component(daynoon)

# write to disk
import os
f=open(output_filename, 'wb')
f.write(cal.to_ical())
