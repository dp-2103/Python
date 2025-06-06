a1 = int(input("Enter marks of maths: "))
a2 = int(input("Enter marks of english: "))
a3 = int(input("Enter marks of science: "))

total_percentage = (a1 + a2 + a3)/300 * 100

if(total_percentage>=33):
    print("Congratuations! you 're passed with percentage...", total_percentage)

else:
    print("bettter luck next time !")
