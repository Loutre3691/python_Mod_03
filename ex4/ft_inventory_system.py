import sys

def parse_argv(argv : list) -> dict:
    inventory = {}
    for av in argv:
        items = av.split(":")

        if len(items) != 2:
            print("\033[0;31mError: invalid parameter\n\033[0m")

        try:
            int(items[1])
        except:
            print("\033[0;31mError: second parameter is not a number\n\033[0m")

        inventory[av] = items[1]




    return inventory


if __name__ == "__main__":
    print("\033[1;35m\n==== Inventory system Analysis ===\033[0m\n")

    if len(sys.argv) < 2:
        print("\033[0;31mNo arguments provied!\033[0m\n")

    inventory = parse_argv(sys.argv[1:])



# creation dun inventaire
# - utiliation d'un dictionnaire pour stocker les donnees d'inventaires
# - le code devrai parse les parametre de la ligne de commande pour remplir 
#  l'inventaire
#
#  parametre formats :
# - <item_names>  and <quantity>
#
# paramatere invalide avec messge d'erreur +  placer les valides dans un dictionnaire
# - syntaxe incorrect
# - paramatere dedondant
#
# Les valeurs <quantite> devront etre des int pour les calucls
#
# gestion inventaire:
# - afficher l'invetaire
# - creer et afficher la list de tous les objets en stock
# - calculer et imprimer la quqntite tota de tous les onbjets de l inventaire
# - afficher pour chaque objet le % de quantite qu il represente dans l inventaire
# - indiquer les articles les plus et les moins abondants(chosir le 1er resultat sur la
#   ligne de commande en cas d'egalite)
# - enfin ajoueter un nouvel rticle a ton inventaire et l'afficher a nouveau