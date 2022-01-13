import random
def validate(email): # Check for the email format if the format is right it returns True else  it returns False
    if (email.count("@") == 1) and (email.split('@')[1]== "pop.ac.uk") and (len(email.split('@')[0])>=3):
        return True
    else:
        return False

def network_error(name): # It creates network error with 10% chances.
    if random.choice([i for i in range(10)]) == 1:
        print("*** NETWORK ERROR ***")
        print("Thanks",name," for using PopChat. See you again soon!")
        exit()

def answer(question, name): # It answers the question according to the word
    if "library" in question:
        print("The library is closed today.")
    elif "wifi" in question.lower():
        print("WiFi is excellent across the campus.")
    elif "deadline" in question.lower():
        print("Your deadline has been extended by two working days.")
    elif "garden" in question.lower():
        print("Garden is near from your home.")
    elif "colleage" in question.lower():
        print("Your colleage is closed.")
    elif "coffee" in question.lower():
        print("Today we have special in coffee menu.")
    elif any(char in question.lower() for char in ["bye", "exit", "goodbye", "help"]):
        print("Thanks!",name,"for using PopChat. See you again soon!")
        exit()
    else:
        print(random.choice(["Hmm.", "Oh, yes, I see", "Tell me more.", "I like it.", "Yes.", "Is it ?"]))

print("Welcome to Pop Chat System! \nOne of Our Operators will be pleased to help you today.")

email = input("Enter your email address : ")

if validate(email) == False:
    exit("Invalid Email Address!")

name = email.split('@')[0].capitalize()
Operator = random.choice(['Jimmy', 'Joe', 'John', 'Fiona', 'Friday', 'Siri'])
print(f"Hi, {name}! Thank you, and Welcome to PopChat! \nMy name is {Operator}, and it will be my pleasure to help you.")
while True:
    network_error(name)
    question = input("--->")
    answer(question, name)