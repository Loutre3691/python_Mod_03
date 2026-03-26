import typing
import random


players = [
    "Flora",
    "Chloe",
    "Pierre",
    "Julie",
    "Mariane",
    "Paco",
    "Ethan",
    "Thomas",
    "Noah",
    "Emilie",
    "Louis"
    ]


actions = [
    "shake her ass 🍑",
    "climb macchu picchu ⛰️🦙",
    "eat kebabsauceblanche 🥙",
    "swim with shark 🦈",
    "sleep ZZzzZZzzz 😴",
    "nothing 🕳️",
    "run like a turtle 🐢 ",
    "duck dance 🦆",
    "hassle people 🖕",
    "poop 💩",
    "speak mewww 🐈",
    "sing Beyonce 🐝👑",
    "blackall 🚨"
]

def gen_event(players: list, actions: list):
    while True:
        random_player = random.choice(players)
        random_action = random.choice(actions)
        yield (random_player, random_action)



# def consume_event() -> None:

if __name__ == "__main__":
    print("\033[1;35m\n==== Game Data Stream Processor ===\033[0m\n")

    my_gen = gen_event(players, actions)

    for event in range(1000):
        player, action = next(my_gen)
        print(f"Event {event}: Player {player} did action {action}")






# GENERATEURS : Pour economiser de la memoire
# utilisation de generateurs avec le mot cle "yield" pour creer des fluxs de donnees
# implemeter des fonctions generatrices qui produisent des valeurs a la demande
# 
# fonction gen_event(fonction generatrice):
# - choisi un nom aleatoire dans une liste de joueurs ok 
# - choisi une action aleatoire dans une liste d'action ok 
# - a chaque appel de 'next()' sur ce generateur -> renvoie tuple (nom + action)
#
# Boucler 1000 x et afficher 1000 evenements creer grace a gen_event() ok
# 
# Creer une liste de 10 tuples generer par gen_event()
# Creer une nouvelle fonction generatrice 'consume_event' que prend la liste des 10 tuples cree avant
#
# Choisir aleatoirement un element de la liste tuple, le retirer de la liste et le renvoyer
# jusqu'a que la liste soit vide.