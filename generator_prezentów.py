# generator prezentów.
import random

Bartosz = ["koszula", "słuchawki", "gra planszowa", "portfel", "okulary słoneczne"]
Karolina = ["koszula", "słuchawki", "gra planszowa", "portfel", "okulary słoneczne"]
Dominik = ["koszula", "słuchawki", "gra planszowa", "portfel", "okulary słoneczne"]
   

def losuj_prezenty(osoba, prezent):
    print("{}: {}".format(osoba,random.choice(prezent)))

losuj_prezenty("Bartosz", Bartosz)
losuj_prezenty("Karolina", Karolina)
losuj_prezenty("Dominik", Dominik)
