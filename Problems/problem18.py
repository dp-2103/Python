# write a program to print multiplication TABLE USING for loop in reserse order

n = int(input("enter number:"))

for i in range(10, 0, -1):
    print(f"{n}*{i} = {n*i}")