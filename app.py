import os
from random import randint
from datetime import datetime, timedelta

# Starting date: July 10
start_date = datetime(2024, 7, 10)  # Change the year if needed
# Ending date: August 31
end_date = datetime(2024, 8, 31)

# Generate commits between July 10 and August 31
current_date = start_date
while current_date <= end_date:
    for _ in range(0, randint(1, 10)):  # Random commits for the same day
        d = current_date.strftime('%Y-%m-%d')  # Git requires ISO format for dates
        with open('file.txt', 'a') as file:
            file.write(f"Commit for {d}\n")  # Add a newline for clarity
        os.system('git add .')
        os.system(f'git commit --date="{d}" -m "update"')
    # Move to the next day
    current_date += timedelta(days=1)

# Push all commits
os.system('git push -u origin main')
