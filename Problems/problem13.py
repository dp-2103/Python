# Program to find the sum of first n natural numbers using while loop

# Taking input from the user
n = int(input("Enter a number: "))

# Initialize sum to 0 (starting point)
sum = 0

# Start counter i from 1 (first natural number)
i = 1

# Loop until i becomes greater than n
while i <= n:
    sum += i  # Add current value of i to sum
    i += 1    # Move to the next number

# Print the final result
print("Total sum is", sum)

