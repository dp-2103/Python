def factorial(n):                                            # Define a function 'factorial' that takes one argument 'n'
    if(n == 1 or n == 0):                                    # Base case: if 'n' is 0 or 1, return 1
        return 1                                             # Return 1 for 0! or 1!
    return n * factorial(n - 1)                              # Recursive case: n! = n × (n-1)!

n = int(input("enter number: "))                             # Take integer input from the user and store it in 'n'
print(f"factorial of this nuber is {factorial(n)}")          # Print the factorial of 'n' using an f-string






#watch the recurison diagram in the python handbook by codewithharry