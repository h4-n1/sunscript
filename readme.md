 
# sunscript

Generates an ical file containing events for sunrise and sunset for a given range of dates.

To use, change the variables defined at the beginning. Location is input as coordinates in `loc_lat` and `loc_long`, the only function of `loc_name` is formatting. It also needs the [timezone as defined by `pytz`](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

## Dependencies:

- Python 3
- [astral](https://pypi.org/project/astral/)
- [icalendar](https://pypi.org/project/icalendar/)

## Todo:

- [ ] Better daylight time formatting in event description
- More scripts for [astral's other features](https://astral.readthedocs.io/en/latest/index.html):
	- [ ] Solar noon
	- [ ] Moon phase