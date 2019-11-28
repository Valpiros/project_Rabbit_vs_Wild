from class_Fox import Fox
from class_Rabbits import Rabbit
from Enumerations import Type
import random


def reproduction(x, y, type):
    nb_childs = random.randrange(5)+1
    print("nb enfants:", nb_childs)
    for index in range(0, nb_childs):
        # on détermine la position du nouveau né, différente de celle de la mère
        pos_x, pos_y = define_pos(x, y)
        # on le génère
        if type == Type(0).name:
            Rabbit(pos_x, pos_y)
        else:
            Fox(pos_x, pos_y)
        print(index, ":", pos_x, pos_y)


def define_pos(x, y):
    pos_x = x-2 + random.randrange(5)
    pos_y = y-2 + random.randrange(5)
    while mother_pos(x, y, pos_x, pos_y):
        pos_x = x - 2 + random.randrange(5)
        pos_y = y - 2 + random.randrange(5)
    return pos_x, pos_y


def mother_pos(x, y, pos_x, pos_y):
    if x == pos_x & y == pos_y:
        return True
    else:
        return False
