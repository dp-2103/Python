'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

n = int(input("Enter number: "))

def star(n):
    if (n == 0):        #Base condition
        return 
    print("*" * n)
    star(n-1)

star(n)