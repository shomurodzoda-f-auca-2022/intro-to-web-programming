from datetime import datetime

dateStr = "05-02-2025 09:19:23"
dateObj = datetime.strptime(dateStr, "%d-%m-%Y %H:%M:%S")
print("Parsed Date Object:", dateObj)