# print multiplication table

n = int(input("Enter number: "))

def multiply(n):
    for i in range(1, 11):
        print(f"{n} * {i} = { n * i}")

multiply(n) 