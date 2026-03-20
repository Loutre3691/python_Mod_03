import sys


def calcul_stats(list: list) -> None:
    total_score = sum(list)
    print(f"\033[1;37;31mScores processed:\033[0m {list}")

    print(f"\033[1;37;32mTotal players:\033[0m {len(list)}")

    print(f"\033[1;37;33mTotal score:\033[0m {total_score}")

    average_score = total_score / len(list)
    print(f"\033[1;37;34mAverage score:\033[0m {average_score}")

    print(f"\033[1;37;35mHigh score:\033[0m {max(list)} ")
    print(f"\033[1;37;36mLow score:\033[0m {min(list)} ")

    score_range = max(list) - min(list)
    print(f"\033[1;35mScore range:\033[0m {score_range}")


def main() -> None:
    new_list = []
    print("\033[1;35m\n=== Player Score Analytics ===\033[0m\n")
    if len(sys.argv) < 2:
        print("\033[0;31mNo scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...\n\033[0m")
        return
    for av in sys.argv[1:]:
        try:
            valid = int(av)
            new_list.append(valid)
        except ValueError:
            print(f"Invalid parameter: '{av}'")
    if not new_list:
        print("\033[0;31mNo scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...\033[0m")
        return
    calcul_stats(new_list)


if __name__ == "__main__":
    main()
