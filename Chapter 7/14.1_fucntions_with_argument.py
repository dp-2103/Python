def goodday(name, ending):                      # Define a function that takes two arguments: 'name' and 'ending
    print("Good day, " + name)                 # Print "goodday" with the given name
    print(ending)                              #print ending message
    return "Done"

goodday("Cosmos", "Have a good time")            #call goodday fucntion with name 'cosmos' and ending 'Have a good time'

goodday("dear", "thanks")           

a = goodday("darling", "i love you")          #call goodday fucntion and store return value in a
print(a)                                    #print retured value, which is 'Done'
