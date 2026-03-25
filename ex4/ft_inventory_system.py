import sys

def parse_argv(argv : list) -> dict:
    inventory = {}
    for av in argv:
        items = av.split(":")

    return inventory


if __name__ == "__main__":
    print("\033[1;35m\n==== Inventory system Analysis ===\033[0m\n")

    if len(sys.argv) < 2:
        print("No arguments provied!")

    parse_argv(sys.argv)

        

            
    
      


  
    





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