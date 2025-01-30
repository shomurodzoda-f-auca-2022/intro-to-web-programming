from datetime import datetime, timedelta

now = datetime.now()
print(f"Current time: {now}")

future = now + timedelta(days=1)
print(f"Future time: {future}")