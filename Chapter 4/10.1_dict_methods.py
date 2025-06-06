#creat a dictionary
a = {
    'name': "Bob",
    'age': 21,
    'city': 'Anand'
}

print(a)

#access value by key
print(a['name'])

#get value safely(return none if key not found)
print(a.get('age'))
print(a.get('email'))


# Add or Update a key-value pair
a['email'] = 'bob@gmail.com'
a['age'] = 31
print(a)

# Remove a key or get its value
remove_city = a.pop('city')
print(remove_city)
print(a)

# Get all key value, and items
print(a.keys())
print(a.values())
print(a.items())

# Clear all items in the dictionary
a.clear()
print(a)

a.update({"uff": 12})
print(a)

