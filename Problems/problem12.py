n = int(input("enter a number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break

else:
    print("number is prime")

counts = 0
for i in range(2, n):
    if n%i == 0:
        print(i)
        counts += 1

    if counts == 3:
        break