# Lists are containers to store a set of values of any data type

friends = ["apple", "orange", 10, 3505, False, "akash", "rohan"] 

friends[0] = "Grapes"
print(friends)

#list methods

friends.append("cosmos")   #append means to add at the end
print(friends)

l1= [1, 5, 10, 45, 6, 9]   #[0,1,2,3,4,5] index position
print(l1) 

l1.sort()           #sort the list
print(l1) 

l1.reverse()
print(l1)

l1.insert(2, 3333)  #insert 3333 to the index position of 2
print(l1) 

l1.pop(4)           #pop means remove the value of the correspointind index
print(l1)
print(l1.pop(2))    #show the value of pop

l1.remove(10)     #will remove 10 from the list
print(l1)


