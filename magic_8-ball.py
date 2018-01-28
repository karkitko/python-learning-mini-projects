# magic ball

import random

answers = [" It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

print("It is Magic 8 Ball. If you don't know what to do, ask yes or no question. ")
while True:
    user = input("Do you want to play? Y / N: ")
    
    if user == "Y":
        user = input("Write a question here: ")
        answer = random.choice(answers)
        print (answer)
        
    elif user == "N":
        print ("Bye")
        break
    else:
        print ("Something went wrong.")
        
    
    
