from typing import Generator
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
    "Louis",
    "killian"
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
    "blackhole 🚨",
    "paye bbq 🍖"
]


def gen_event() -> Generator:
    while True:
        random_player = random.choice(players)
        random_action = random.choice(actions)
        yield (random_player, random_action)
# Random choice in list player and action


def consume_event(new_list: list) -> Generator:
    while len(new_list) > 0:
        choice = random.choice(new_list)
        new_list.remove(choice)
        yield choice
# random choice in list 10 tuple in the before list


if __name__ == "__main__":
    print("\033[1;35m\n==== Game Data Stream Processor ===\033[0m\n")

    my_gen = gen_event()

    for i in range(1000):
        player, action = next(my_gen)
        print(f"\033[1;37mEvent {i}\033[0m: Player {player} did action "
              f"{action}")

    new_list = []
    for event in range(10):
        p, a = next(my_gen)
        new_list.append((p, a))
    print(f"\n\033[1;31m\nBuilt list of 10 events:\033[0m{new_list}\n")

    for i in range(10):
        choice = next(consume_event(new_list))
        print(f"\033[1;31mGot event from list: \033[0m{choice}")
        print(f"\033[1;32mRemains in list:\033[0m {new_list}\n")
