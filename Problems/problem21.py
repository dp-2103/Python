# Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(n) = 1 + 2 + 3 + 4 + ... + n
'''

n = int(input("Enter Number till which you want sum: "))

def sum(n):                              
    if (n == 1):                                   # Base case: if n is 1, return 1
         return 1                                  # This stops the recursion from continuing forever
    return sum(n-1) + n

print(f"the sum of first {n} natural number is {sum(n)}")

