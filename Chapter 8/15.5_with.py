# f = open("15.2_myfile.txt")
# print(f.read())
# f.close()

# The same can be written using with statement
# we don't need to write f.close() if we use with statement

with open("15.2_myfile.txt") as f:
    print(f.read())

# you don't need to close the file explicitly