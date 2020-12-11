import json
from difflib import get_close_matches
import datetime
#IntroBasix


print("A DICTIONARY")
print("The date and time right now is",datetime.datetime.now())
mytext=("This is a Dictionary for 'A' words")
print(mytext)  

#User Input
#UserInputProcessing with First Name and Last Name
NameMessage= input("First Name:")
LastName= input("Last Name:")
When = input("date")
message= f"Hello {NameMessage} {LastName}!! today is {When}, please try the dictionary!"  
print("the date and time now is",datetime.datetime.now())
print(message) 
plstry= input("How are you?:")
if plstry == "good":
    print( "glad you are well")
else: 
    print( "uh oh")
messagetwo= f"{plstry}"



#calling json file
data = json.load(open("data_lesssize.json"))

#translate 1
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


#translate 2
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter another word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

 #translate 3
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter another word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)






