a = int(input("Enter your age: "))

if(a>=18):
    print("you are above the age of consent")

elif(a<0):
    print("invlid age")

elif(a==0):
    print("invalid")

else:
    print("you are below the age of consent")

print("end of program")