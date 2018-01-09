import random
female_name=['Anna', 'Katarzyna', 'Zofia', 'Karolina']
male_name=['Adam', 'Karol', 'Piotr', 'Tomasz']
last_name=['Brzęczyszczykiewicz', 'Regis', 'Kowalski', 'Kerman', 'White']
choice= (input('chcesz wygenerować imię męskie - m/ żeńskie - f? '))
while True:
    if choice=='m':
        print(random.choice(male_name)+' '+random.choice(last_name))
        break
    elif choice=='f':
        print(random.choice(female_name) + ' ' + random.choice(last_name))
        break
