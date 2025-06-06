name = "abcdefgh"   #strings

nameshort = name[0:3] #start from 0 all the way till 3(excluding 3)
print(nameshort)
character1 = name[1]
print(character1)

#negative slicing
print(name[0:4])
#or
print(name[-4:-1])

#skip value 
print(name[1:8:2])

''' in short [starting, ending, skip jump]'''

#string fucntions
print(len(name))
print(name.endswith("efh"))   #true or false
print(name.startswith("abc")) #true or false
print(name.capitalize())      #capitalize first word
print(name.upper())           #capiitalize whole word
print(name.zfill(10))         #add zeros to make it 10 size
print(name.replace("abc","xyz")) #replace the characters 
print(name.find("b"))           #to find the number

#escape sequence
a = "Cosmos is a spiritual universe\n not a regular \"universe\""

'''
"\n"is sed to break a line in a string as you cannot break a line in sinngle string"
'''

print(a) 

''' to type double quote you need to use \" '''