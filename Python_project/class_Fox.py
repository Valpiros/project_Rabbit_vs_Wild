import random
import Enumerations
from Enumerations import Sexe


class Fox:

    def __init__(self):
        self.faim = 0
        self.soif = 0
        self.sexe = Sexe(bool(random.getrandbits(1))).name
        print("renards stats : ")
        print("faim :", self.faim, "/ 100")
        print("soif :", self.soif, "/ 100")
        print("sexe :", self.sexe)
