st = "Hey how are you ?"            # Your message

f = open("15.2_myfile.txt", "w")    # Open the file in write mode ("w" overwrites if file exists)

f.write(st)                         # Write the string to the file

f.close()                           # Close the file