# Write a program to print multiplication table
#  of a given number using for loop. 

n = int(input("Enter a number: "))


for i in range(1, 11):
    print(f"{n} * {i} = {n * i} ")

l = ["harry", "shubh", "sachin", "DP"]

for name in l:
    if(name.startswith("s")):
        print("hello", name)      #use f string in print print(f"hello {name}")