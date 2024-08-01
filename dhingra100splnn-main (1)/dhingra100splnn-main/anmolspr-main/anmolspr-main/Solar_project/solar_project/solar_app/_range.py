from datetime import date
from solar_app.models import Event

# Define your date range
start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)

# Query to fetch events between start_date and end_date
events = Event.objects.filter(date__range=(start_date, end_date))

for event in events:
    print(event.name, event.date)
