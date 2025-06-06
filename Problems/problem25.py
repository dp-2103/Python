'''
Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.
'''
f = open("poem.txt")
c = f.read()
if ("twinkle" in c):
    print("the word twinkle is present in the content")
else:
    print("the word twinkle is not present in the content")
    
f.close()
