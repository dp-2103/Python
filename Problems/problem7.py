a1 = int(input("ENTER NUMBER ONE: "))
a2 = int(input("ENTER NUMBER SECOND: "))
a3 = int(input("ENTER NUMBER THIRD: "))
a4 = int(input("ENTER NUMBER FOURTH: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("greatest number is first:", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("greatest number is second:", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("greatest number is third:", a3)

else:
    print("greatest number is fourth:", a4) 