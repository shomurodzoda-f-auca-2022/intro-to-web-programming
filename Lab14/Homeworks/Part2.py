from datetime import datetime

eventDate = datetime(datetime.now().year, 12, 31)
now = datetime.now()
daysRemaining = eventDate - now
print("Days Remaining to New Year:", daysRemaining.days)