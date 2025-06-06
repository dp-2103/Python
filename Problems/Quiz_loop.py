# Write a program to print the content of a list using while loops

#while loop with list
l = ["Devansh", "Shubh", "Ved", False, 2]

i = 0                 # if i = 1 it will start from 1st index number that is shubh

while(i<len(l)):
    print(l[i])
    i +=1

#for loop with list
print("example with for loop:")
for i in l:
    print(i)

# for loop example with string
s = "DP"
for i in s:
    print(i)

#for loop with tuples
t = (1, 4, 10, 45)
for i in t:
    print(i)
