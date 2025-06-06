# -----------------------------
# Example: While Loop in Python
# -----------------------------

# Initialize a counter variable
i = 1

print("While loop example:")
# The while loop runs as long as the condition (i <= 5) is True
while i <= 5:
    print(i)   # Print the current value of i
    i += 1     # Increment i by 1 to avoid infinite loop

# Another while loop example
a = 0
while a < 5:
    print("Cosmos")  # Print "Cosmos" 5 times
    a += 1           # Increment a by 1

# --------------------------
# Example: For Loop in Python
# --------------------------

print("For loop example:")
# The range function generates numbers from 0 to 4 (5 not included)
for a in range(5):
    print(a)  # Print values from 0 to 4

# ------------------------------------------
# Understanding the 'range()' Function
# ------------------------------------------

# Syntax: range(start, stop, step)
# start - starting number (inclusive)
# stop - ending number (exclusive)
# step - the amount to increment each time

print("Range function with step size:")
for b in range(0, 10, 3):
    print(b)  # Prints: 0, 3, 6, 9

# ----------------------------
# For Loop with an Else Clause
# ----------------------------

print("For loop with else:")
# The else block in a loop runs only if the loop is not terminated by a 'break' statement
for i in range(3):
    print("Looping:", i)
else:
    print("Loop completed normally.")  # This will be printed after the loop ends normally

