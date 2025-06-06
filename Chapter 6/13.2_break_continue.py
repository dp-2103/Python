print("break statement:")

for i in range(10):
    if(i == 4):
        break #exit the loop right now
    print(i)

print("  ")
print("continue statement:")

for i in range(10):
    if(i == 1):
        continue #skip this iteration
    print(i)


# ‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now. 
# 'continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”. 

print("  ")
print("pass statement:")
for i in range(10):
    pass                    # null statement in python. instructs to “do nothing”. 

i = 3
while(i<10):
    print(i)
    i += 3
