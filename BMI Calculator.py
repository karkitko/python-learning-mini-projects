print ("Kalulator BMI")
inp = input("Chcesz sprawdzić BMI? T/N:")
if inp == "T":
    print ("podaj wzrost i wagę")
    wzrost = float(input("wzrost:"))
    waga = float(input("waga:"))
    BMI = waga/wzrost **2
    print (BMI)

    if BMI <= 18.5:
        print('Zjedz ciasteczko')
    elif BMI > 18.5 and BMI < 25:
        print('Jest dobrze')
    elif BMI > 25 and BMI < 30:
        print('10 pompek i zero cukierków.')
    elif BMI > 30:
        print('Zmieniasz się w kulkę.')

elif inp == "N":
    print ("potrafię tylko liczyć BMI")


