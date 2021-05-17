### ALL USER INPUT HERE
# define location and date range
loc_name = 'Toronto'
loc_region = 'Ontario'
loc_lat = 43.651070
loc_long = -79.347015
loc_tz = 'America/Toronto'
date_start = date(2021, 1, 1)
# daterange function is exclusive of end date
date_end = date(2022, 1, 1)
output_filename = 'sun_{0}_{1}_{2}.ics'.format(loc_name.lower(), date_start, date_end)

### ASTRAL STUFF
# https://astral.readthedocs.io/en/latest/index.html
from astral import LocationInfo
from astral.moon import phase

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

#########
#indent:#
#########

moon_phase_val = phase(loc_date)

if moon_phase_val < 7:
    moon_phase = "New moon"
elif moon_phase_val < 14:
    moon_phase = "First quarter"
elif moon_phase_val < 21:
    moon_phase = "Full moon"
elif moon_phase_val < 28:
    moon_phase = "Last quarter"
elif moon_phase_val > 28:
    moon_phase = "ERROR"
    print("ERROR : moon_phase_val over 28.00")

### how to return the day the phase changes?


























