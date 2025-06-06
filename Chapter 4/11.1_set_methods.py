#creat set
a = {"apple", "banana", "mango"}
b = {"cherry", "orange", "banana"}

print(a)
print(b)

#length
print(len(a))

#add an element to the set
a.add("orange")
print(a)

# remove an element; raises  error if not found
a.remove('banana')
print(a)

# discard() -- remove if present; no error if not found
a.discard('watermellon')
print(a)

# union() -- return a new set with all elements from both set
all_fruits = a.union(b)
print(all_fruits)

# intersection() -- return common elements
common = a.intersection(b)
print(common)

# difference() -- elements in first set but not in second
diff = b.difference(a)
print(diff)

# symmetric_difference() -- elements in either set, but not both
sym_diff = a.symmetric_difference(b)
print(sym_diff)

# update elemtns
a.update({'1', '5'})
print(a)

# pop()--- remove and return an arbitary random element
item = a.pop()
print(item)
print(a)



# clear()--- remove all elements
a.clear()
print(a)


