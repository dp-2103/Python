p1 = "Buy this"
p2 = "click this"
p3 = "subscribe this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("this is spam")

else:
    print("this is not spam")