import random


def gen_player_achievements() -> set:
    all_achievement = [
        "Crafting Genius",
        "Strategist",
        "World Savior, Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First",
        "Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer"
    ]
    nb = random.randint(1, len(all_achievement))
    list_random = set(random.sample(all_achievement, nb))
    return list_random


def common_achievement(list: set) -> list:

        set.union(list)


if __name__ == "__main__":
    print("\033[1;35m\n=== Achievement Tracker System ===\033[0m\n")
    players = [
        "\033[0;95mFlora\033[0m",
        "\033[0;96mPierre\033[0m",
        "\033[0;33mChloe\033[0m",
        "\033[0;91mPaco\033[0m"
    ]
    for p in players:
        list_random = gen_player_achievements()
        print(f"{p} : {list_random}")
    common = common_achievement(list_random)
    print(f"\nCommon achievement: {'common'}\n")





















# creation d'un system qui repertories les succes des joueurs
# fonction gen_player_achivement:
# - utilisera une longue list fixe de succes
# - choisir aleatoirement un nombre de succes
# 
# il faudra: 
# generer des sets de succes pour min 4 joueurs
# trouver les succes uniques parmis tous les joueurs
# trouver les succes partages par tous les joueurs
# pour chaque joueur, reperer les succes qu il est le seul a avoir
# pour chaque joueur, lister les succes qui lui manque pour les avoir tous