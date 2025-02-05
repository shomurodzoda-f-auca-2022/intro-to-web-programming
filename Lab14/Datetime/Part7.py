from datetime import datetime

eventDate = datetime(2025, 12, 12)
daysRemaining = eventDate - datetime.now()

print("Days until event:", daysRemaining.days)