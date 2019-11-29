

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
