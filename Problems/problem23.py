#  Write a python function which converts inches to cms

n = int(input("enter value of inch: "))

def inch(n):
    return n * 2.54 

print(f"the value in cm is {inch(n)} cm")