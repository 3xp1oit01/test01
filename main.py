import os
import subprocess
import random
import time

def make_commit(days: int):
    # Base case: stop recursion when no more commits are needed
    if days < 1:
        # Push the changes once all commits have been made
        subprocess.run(['git', 'push'], check=True)
        print("Pushed all changes to remote repository.")
        return

    # Create the file if it doesn't exist (this ensures 'data.txt' is present)
    if not os.path.exists('data.txt'):
        with open('data.txt', 'w') as file:
            file.write("Initial commit content\n")

    # Randomly decide if we should skip this day (e.g., 30% chance of skipping)
    if random.random() < 0.3:  # 30% chance of no commit
        print(f"Skipping day {days}")
        make_commit(days - 1)
        return

    # Randomly decide how many commits to make on this day (between 1 and 5 commits)
    num_commits = random.randint(1, 5)
    print(f"Making {num_commits} commits for day {days}")

    for _ in range(num_commits):
        # Format the date string with some random variation
        date_str = f'{days} days ago'

        # Add a random text to the file to simulate different commit changes
        with open('data.txt', 'a') as file:
            file.write(f"Commit content for {date_str}: {random.randint(1000, 9999)}\n")

        # Stage the changes
        subprocess.run(['git', 'add', 'data.txt'], check=True)

        # Commit the changes with the specific date
        commit_message = f"Commit for {date_str}"
        subprocess.run(['git', 'commit', '--date', date_str, '-m', commit_message], check=True)

        # Add a small random delay to simulate real-world commit intervals (0.5 to 2 seconds)
        time.sleep(random.uniform(0.5, 2))

    # Recur for the next day
    make_commit(days - 1)

# Start the commit process from day 300
make_commit(300)
