

# 0 : bas, 1 : droite, 2 : haut, 3 : gauche
def move(pos_x, pos_y, choice):
    if choice == 0:
        pos_y += 1
    elif choice == 1:
        pos_x += 1
    elif choice == 2:
        pos_y -= 1
    elif choice == 3:
        pos_x -= 1
    return pos_x, pos_y


def eat(faim, soif, food):   # 0->salade, 1->carottes, 2->lapin
    if food == 0:
        faim -= 50
        soif -= 25
    elif food == 1:
        faim -= 75
    elif food == 2:
        faim == 0
    return faim, soif


def drink():
    return 0
