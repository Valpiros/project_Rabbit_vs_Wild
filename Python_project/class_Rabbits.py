import random
from enum import Enum


class Sexe(Enum):
    Male = False
    Female = True


class Rabbit:

    def __init__(self):
        self.faim = 0
        self.soif = 0
        self.sexe = Sexe(bool(random.getrandbits(1))).name
        print("lapin stats : ")
        print("faim :", self.faim, "/ 100")
        print("soif :", self.soif, "/ 100")
        print("sexe :", self.sexe)


""" 
rabbit1 = Rabbit()  # init d'un lapin
if rabbit1.sexe == Sexe(False).name:    # utilisation de l'info M/F
    print ("c'est un male !")
else:
    print("c'est une femelle !")
"""
