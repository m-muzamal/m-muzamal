import os
from random import randint 

# Loop for the dates from January 1, 2025, to January 4, 2025
for day in range(1, 5):  # 1 to 4
    date_str = f"2025-01-{day:02d}"  # Format as YYYY-MM-DD
    
    for j in range(0, randint(1, 10)):  # Random number of commits per day
        d = f"{date_str} days ago"  # Create the commit date string
        with open('file.txt', 'a') as file:
            file.write(d + '\n')  # Append to file with a newline after each entry

        os.system('git add .')
        os.system(f'git commit --date="{d}" -m "update"')

# Finally push all changes
os.system('git push -u origin main')
