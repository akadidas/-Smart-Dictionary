import json;
from difflib import get_close_matches

data= json.load(open("data.json"))
word=""
def get_mean(word):



    if(word in data):
        return data[word]

    elif len(get_close_matches(word,data.keys()))>0:

        decision= input("Did you mean %s instead ? Type Y for yes and N for no :"%get_close_matches(word,data.keys())[0])
        decision=decision.upper()

        if(decision=="Y"):
            return data[get_close_matches(word,data.keys())[0]]


        elif(decision=="N"):
            wo=input(" Word not exist in database Pls enter  another word  ")
            return data[wo]



    else:
        return "word does not exist in dictionary please check the word and enter again "




word=str(input("enter the word to get meaning : ")).lower()


mean= (get_mean(word))

if(type(mean)==list):
    for item in mean:
        print(item)

else:
    print(mean)



