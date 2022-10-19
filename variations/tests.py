from django.test import TestCase
from datetime import datetime
# Create your tests here.
# current_date = datetime.today().strftime('%Y-%m-%d')


from datetime import datetime
start_date = "5/10/2022 8:00:00"
end_date = "20/10/2022 8:59:00"

# format of date/time strings; assuming dd/mm/yyyy
date_format = "%d/%m/%Y %H:%M:%S"

# create datetime objects from the strings
start = datetime.strptime(start_date, date_format)
end = datetime.strptime(end_date, date_format)
now = datetime.now()

if end < now:
    # event in past
    print('past')
elif start > now:
    # event in future
    print('future')
else:
    # event occuring now
    print('now')