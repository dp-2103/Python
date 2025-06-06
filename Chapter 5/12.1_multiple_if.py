a = int(input("Enter your age: "))

#if statement no: 1
if(a%2 == 0):
    print("a is even")

else:
    print("a is odd")
#end of if statement no: 1


#if statement no: 2
if(a>=18):
    print("you are above the age of consent")

elif(a<0):
    print("invlid age")

elif(a==0):
    print("invalid")

else:
    print("you are below the age of consent")
#end of if statement no: 1

print("end of program")