from datetime import datetime, timedelta

futureDate = datetime.now() + timedelta(days=5)
print("Future Date in 5 days:", futureDate)

pastDate = datetime.now() - timedelta(days=5)
print("Past date:", pastDate)