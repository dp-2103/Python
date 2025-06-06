# Write a program using functions to find greatest of three number

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

print(greatest(a, b, c))