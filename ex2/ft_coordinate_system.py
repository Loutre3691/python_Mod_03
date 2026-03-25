import math


def get_player_pos() -> tuple:
    while True:
        try:
            new_c = input("Enter new coordinates as floats in format "
                          "'x,y,z': ")
            parties = new_c.split(",")
            if len(parties) != 3:
                print("Invalid syntax")
                continue
            for p in parties:
                try:
                    float(p)
                except ValueError:
                    raise ValueError(
                        f"\033[0;31mError on parameter '{p}': "
                        f"could not convert string to float: '{p}'\033[0m")
            return tuple(float(p) for p in parties)

        except ValueError as e:
            print(e)


def calcul_distance(parties: tuple) -> float:
    result = 0
    for p in parties:
        result = result + (p * p)
    return math.sqrt(result)


def distance_first_second(
        first_parties: tuple, second_parties: tuple) -> float:
    total = 0
    for p1, p2 in zip(first_parties, second_parties):
        total = total + (p1 - p2) ** 2
    return math.sqrt(total)


if __name__ == "__main__":
    print("\033[1;35m\n=== Game Coordinate System ===\033[0m\n")
    print("\033[1;32mGet a first set of coordinates\033[0m")
    first_parties = get_player_pos()
    print(f"Got a first tuple: {first_parties}")
    print(f"It includes: X={first_parties[0]}, Y={first_parties[1]}, "
          f"Z={first_parties[2]}")
    first_distance = calcul_distance(first_parties)
    print(f"Distance to center: {first_distance}")

    print("\n\033[1;32mGet a second set of coordinates\033[0m")
    second_parties = get_player_pos()
    second_distance = calcul_distance(second_parties)
    print(f"Got a second tuple: {second_parties}")
    print(f"Distance to center: {second_distance}")
    print(f"It includes: X={second_parties[0]}, Y={second_parties[1]}, "
          f"Z={second_parties[2]}")
    print()
    between_distance = distance_first_second(first_parties, second_parties)
    print(f"\033[1;35mDistance between the 2 sets of coordinates: "
          f"{between_distance}\n\033[0m")
