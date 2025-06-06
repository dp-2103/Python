a = (1, 4, 43, 43, 434, False, "Rohan")
print(a)
print(type(a))
#we cannot change element in tuple

#tuple methods
no = a.count(43)   #number of times 43 comes
print(no)      

i = a.index(434)    #shows index position
print(i)

print(len(a)) #gives the length of a

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)


data = [(1, 2), (2, 3), (3, 4)]  # (time, position)

for t, x in data:                       #for loop
    print(f"At t={t}sec, x={x}m")
