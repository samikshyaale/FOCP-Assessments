name = input("What is your name ? ")
if name.capitalize() == "Arthur": # Check for the name if it is king or not
    print("My! liege! You may pass\n") 
else:
    quest = input("What is your quest? ")
    if "grail" in quest or "Grail" in quest: # Checking for the name if grail is in the sentence or not.   
        color= input("What is your favourite color? ")
        if name[0].lower() == color[0].lower(): # Checking if the first letters of name and colour is same or not.
            print("You may pass!")
        else:
            print("Incorrect! you must now face the gorge of Eternal Peril")
    else:
        print("Only those who seek the Grail may pass.\n")
    
        