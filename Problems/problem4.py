# Step 1: Import the 'os' module, which lets you interact with the operating system
import os

# Step 2: Use os.listdir() to get a list of files and folders in the current directory
# Then, use a for loop to go through each item in that list
for item in os.listdir():
    # Step 3: Print each item (file or folder name)
    print(item)

print('''note:
problem 5 is same as 4 just with comments so haven't  written''')