import sys


def main() -> None:
    count = 1
    print("\033[1;35m\n=== Command Quest ===\033[0m")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provied!")
    else:
        print(f"arguments receveid: {len(sys.argv) - 1}")
    for av in sys.argv[1:]:
        print(f"Argument {count}: {av}")
        count += 1
    print(f"Total arguments: {count}")


if __name__ == "__main__":
    main()
