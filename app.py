import os
from random import randint
from datetime import datetime, timedelta

# Start and end dates
start_date = datetime(2025, 1, 12)
end_date = datetime.now()

# Calculate the number of days in the range
days_diff = (end_date - start_date).days

# Loop through each day in the range
for i in range(0, days_diff + 1):
    # Calculate the specific date
    commit_date = start_date + timedelta(days=i)
    formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    # Random number of commits for the day
    for j in range(randint(1, 10)):
        with open('file.txt', 'a') as file:
            file.write(formatted_date + '\n')

        # Commit with the specific date
        os.system(f'git add .')
        os.system(f'git commit --date="{formatted_date}" -m "update"')

# Push the commits
os.system('git push -u origin main')
