#problem to creat star pattern starting from the center as shown below

'''
for n =3
  *
 ***
*****
'''

n = int(input("enter number: "))
for i in range(1, n+1):
    # Print (n - i) spaces to align stars to the cente
    print(" "*(n-i), end="")      #, end=""keeps the cursor on the same line
   
    # Print (2*i - 1) stars to form the pyramid pattern
    print("*"*(2*i-1), end="")

    # Print newline to move to the next row
    print("")
