from datetime import date
print ("Calculate Age in Second")
inp = input("Would you like calculate how many seconds have you been alive: Y / N ")
if inp == "Y":
    print ("How old are you?")

    year = int(input("What year were you born in?:"))
    month = int(input("What month were you born in? (write a number):")) 
    day= int(input("What day were you born in?:"))
    your_birthday = date(year, month, day)
    print (your_birthday)
    today = date.today()
    print (today)
    age_days = today - your_birthday
    age_days = age_days.days
    print ("you are {} days old.".format(age_days))
    age_seconds=age_days*86400
    print ("You are abour {} second old.".format(age_seconds))
elif inp == "N":
    print (":( bye")
