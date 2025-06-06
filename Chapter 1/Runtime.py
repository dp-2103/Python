import time  # Import the time module

# Take input from the user
n = int(input("Enter number: "))

# Initialize factorial
fact = 1
i = 1

# Start the timer just before the calculation
start_time = time.time()

# Perform the factorial calculation using for loop
for num in range(1, n + 1):
    fact = fact * i
    i += 1

# End the timer right after the calculation
end_time = time.time()

# Print the result
print(f"The factorial of {n} is {fact}")

# Calculate and print only the calculation time
runtime = end_time - start_time
print(f"Calculation time: {runtime:.8f} seconds")

