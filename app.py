import os
from random import randint 

# Dates to generate commits for
dates = ["2025-01-10", "2025-01-11"]

for date in dates:
    for _ in range(0, randint(1, 10)):  # Random number of commits per day
        with open('file.txt', 'a') as file:
            file.write(f"Commit for {date}\n")  # Write date info to file
        os.system('git add .')
        os.system(f'git commit --date="{date}" -m "update"')

os.system('git push -u origin main')
