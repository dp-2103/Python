# Write a program to calculate the factorial of a given number using for loop

# taking input from the user
n = int(input("Enter nmber: "))

# initializing factorial 
fact = 1

#start counter i from 1
i = 1

# making for loop 
for num in range(1, n+1):
    fact = fact * i
    i += 1

print(f"the factorial of {n} is {fact}")
