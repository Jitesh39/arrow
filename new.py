from datetime import datetime, timedelta

# Current date and time
now = datetime.now()

# Specific date and time
specific_date = datetime(2023, 10, 29, 15, 45)

# Formatting dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# Parsing dates from strings
parsed_date = datetime.strptime("2023-10-29 15:45:00", "%Y-%m-%d %H:%M:%S")
