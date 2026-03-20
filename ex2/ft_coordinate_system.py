import math
import sys

def get_player_pos() -> None:
    print("\033[1;35m\n=== Game Coordinate System ===\033[0m\n")
    print("Get a first set of coordinates")
    while True:
        try:
            new_c = input("Enter new coordinates as floats in format 'x,y,z':")
            list = []
            for i in list:
                if new_c == ",":
                    list.append(float(i))
            print(f"{list}")

        except ValueError:
            print("Invalid syntax")
       


if __name__ == "__main__":
    get_player_pos()


# tuples pour stocker les coordonnees 3D (x, y, z)
#
# fonction get_player_pos:
# - demande a l user les new coordonnes du joueur au format x, y, z
# - gerer les entrees incorrectes
# - resseaie jusqua ce quun ensemble de coordonnees vqlides soient fournis
# - renvoie un tuples contenant les coordonnes 3d actuelles du joueur
#
# Obtenir un premier ensemble de coordonnes
# afficher le tuple, puis chaque coordonnee separement
# calculer la distance au cente 3D(0,0,0)
#
# Obtenir un nouvel ensemble de coordonnes
# Calculer la distance entre le deuxieme et le premier ensemble de coordonnee
# formule de distance pour calculer la distance entre 2 points 3d:
# voir formule sujet

