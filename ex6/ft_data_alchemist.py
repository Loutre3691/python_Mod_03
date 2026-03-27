import random

players = [
    "Flora",
    "pierre",
    "Chloe",
    "Julie",
    "mariane",
    "Agathe",
    "julie",
    "Thomas"
]


if __name__ == "__main__":
    print("\033[1;35m\n==== Game Data Alchemist ===\033[0m\n")
    print(f"\033[1;37mInitial list of players:\033[0m {players}\n")

    capitalize_list = [p.capitalize() for p in players]
    print(f"\033[1;37mNew list with all names capitalized: \033[0m"
          f"{capitalize_list}\n")

    isupper_list = [p for p in players if p[0].isupper()]
    print(f"\033[1;37mNew list of capitalized names only: \033[0m"
          f"{isupper_list}\n")

    score_dict = {p: random.randint(0, 1000) for p in capitalize_list}
    print(f"\033[1;37mScore dict: \033[0m"
          f"{score_dict}\n")

    score_average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {score_average:.2f}")

    high_scores = {
        p: score_dict[p] for p in score_dict if score_dict[p] > score_average}
    print(f"\033[1;37mHigh scores:\033[0m {high_scores}: ")
