import random
from Enumerations import Sexe


class Rabbit:

    def __init__(self, x, y):
        self.faim = 100
        self.soif = 50
        self.sexe = Sexe(bool(random.getrandbits(1))).name
        print("lapin stats : ")
        print("faim :", self.faim, "/ 100")
        print("soif :", self.soif, "/ 100")
        print("sexe :", self.sexe)
        # ajouter la partie placement sur la carte
        # ajouter à une liste de lapins à parcourir pendant le main() je pense
        self.x = x
        self.y = y


""" 
rabbit1 = Rabbit()  # init d'un lapin
if rabbit1.sexe == Sexe(False).name:    # utilisation de l'info M/F
     print ("c'est un male !")
else:
   print("c'est une femelle !")
"""
