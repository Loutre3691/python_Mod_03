import random


def list_achievement() -> list:
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
    return all_achievement


def gen_player_achievements() -> set:
    all_achievement = list_achievement()

    nb = random.randint(1, len(all_achievement))
    list_random = set(random.sample(all_achievement, nb))
    return list_random
# create a achievement list and choose a random achievement


def common_achievement(data_players: dict) -> set:
    common = set.intersection(*data_players.values())
    return common
# search and compare the dict to find common achievements
# * = depacking


def find_unique_achievement(data_players: dict) -> None:
    for player in data_players:
        data_set = data_players[player]

        other_set = []
        for o in data_players:
            if o != player:
                other_set.append(data_players[o])
# collect all other players achievements in a list

        unique = data_set.difference(*other_set)
# find achievements that belong only to this player

        print(f"only {player} has: {unique}")


def missing_achievement(data_players: dict) -> None:
    all_achievement = list_achievement()
    for player in data_players:
        data_set = data_players[player]
        missing = set(all_achievement).difference(data_set)
        print(f"{player} is missing: {missing}")
# convert all_achievement list to set and find what each player is missing


if __name__ == "__main__":
    print("\033[1;35m\n=== Achievement Tracker System ===\033[0m\n")
    players = [
        "\033[1;32mFlora\033[0m",
        "\033[1;36mPierre\033[0m",
        "\033[1;33mChloe\033[0m",
        "\033[1;31mPaco\033[0m"
    ]
    data_players = {}
    for p in players:
        data_players[p] = gen_player_achievements()
        print(f"{p} : {data_players[p]}")

    common = common_achievement(data_players)
    print(f"\n\033[1;35mCommon achievement:\033[0m {common}\n")
    find_unique_achievement(data_players)
    print()
    missing_achievement(data_players)
