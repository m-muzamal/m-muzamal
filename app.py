import os
from random import randint 

# Loop for November (30 days) and December (31 days) of 2024
for month in [11, 12]:
    # Define the number of days for each month
    days_in_month = 30 if month == 11 else 31

    for day in range(1, days_in_month + 1):
        date_str = f"2024-{month:02d}-{day:02d}"  # Format as YYYY-MM-DD
        
        for j in range(0, randint(1, 10)):  # Random number of commits per day
            d = f"{date_str} days ago"  # Create the commit date string
            with open('file.txt', 'a') as file:
                file.write(d + '\n')  # Append to file with a newline after each entry

            os.system('git add .')
            os.system(f'git commit --date="{d}" -m "update"')

# Finally push all changes
os.system('git push -u origin main')
