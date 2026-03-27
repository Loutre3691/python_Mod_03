import sys


def parse_argv(argv: list) -> dict:
    inventory = {}
    for av in argv:
        items = av.split(":")

        if len(items) != 2:
            print(f"\033[0;31mError - invalid parameter '{av}'\033[0m")
            continue
        if items[0] in inventory:
            print(f"\033[0;31mRedundant item '{items[0]}' - discarding\033[0m")
            continue

        try:
            int(items[1])
        except ValueError:
            print(f"\033[0;31mQuantity error for '{items[0]}': invalid literal"
                  f" for int() with base 10: '{items[1]}'\033[0m")
            continue

        inventory[items[0]] = int(items[1])

    return inventory
# parsing argument


def percent_represent(inventory: dict, total_items: int) -> None:
    for key, value in zip(list(inventory.keys()), list(inventory.values())):
        percent_item = (value * 100) / total_items
        print(f"Item {key} represents: {percent_item:.1f}%")
# zip allows you to browse keys and values ​​at the same time but
# separately and calculates %


def most_least_quantity(inventory: dict) -> None:
    values_inventory = list(inventory.values())
    keys_inventory = list(inventory.keys())
    max_value = values_inventory[0]
    key_max = keys_inventory[0]
    min_value = values_inventory[0]
    key_min = keys_inventory[0]

    for key, value in zip(keys_inventory, values_inventory):
        if value > max_value:
            key_max = key
            max_value = value
        elif value < min_value:
            key_min = key
            min_value = value

    print(f"\033[1;37m\nItem most abundant: \033[0m{key_max} with quantity"
          f" {max_value}")
    print(f"\033[1;37mItem least abundant: \033[0m{key_min} with quantity "
          f"{min_value}")


def add_new_item(inventory: dict) -> None:
    inventory.update({"magic_item": 1})
    print(f"\n\033[1;37mUpdated inventory:\033[0m {inventory}")


if __name__ == "__main__":
    print("\033[1;35m\n==== Inventory system Analysis ===\033[0m\n")

    if len(sys.argv) < 2:
        print("\033[0;31mNo arguments provied!\033[0m\n")
        exit()
    inventory = parse_argv(sys.argv[1:])

    if len(inventory) == 0:
        exit()

    print(f"\n\033[1;37mGot inventory:\033[0m {inventory}")

    print(f"\033[1;37mItem list:\033[0m {list(inventory.keys())}\n")

    total_items = sum(inventory.values())
    print(f"\033[1;37mTotal quantity of the 5 items: \033[0m{total_items}\n")

    percent_represent(inventory, total_items)

    most_least_quantity(inventory)

    add_new_item(inventory)
