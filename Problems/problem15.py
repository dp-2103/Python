#problem to creat star pattern

n = int(input("enter number: "))
for i in range(1, n+1):
    print("*"*(i), end="")    #1
    print("")                 #2
   
    #1 Print (2*i - 1) stars to form the pyramid pattern
    #2 Print newline to move to the next row
    