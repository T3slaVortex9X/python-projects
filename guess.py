import random

def safe_int(prompt):
    while True:
        v = input(prompt).strip()
        try:
            return int(v)
        except ValueError:
            print("Invalid number!")

def choose_dif():
    print("\n---Difficulty level---")
    print("1) (10-1) Easy")
    print("2) (50-1) Medium")
    print("3) (100-1) Hard")

    while True:
        c = input("Choose:").strip()
        match c:
            case "1":
                return 1, 10, 5
            case "2":
                return 1, 50, 7
            case "3":
                return 1, 100, 10
            case _:
                print("Invalid option")
def play_game(stats):
    low, high, tries = choose_dif()
    target = random.randint(low, high)
    print(f"A number between {low} to {high} have {tries}")

    attempts = 0
    while attempts < tries:
        guess = safe_int("your guess: ")
        attempts += 1

        if guess == target:
            print("Excellent you have hit it")
            stats["wins"] += 1
            return
        if guess > target:
            print("Lower")
        else:
            print("More")
    print(f"correct number and you lose {target}")
    stats["losses"] += 1

def show_stats(stats):
    print(f"Wins: {stats["wins"]}")
    print(f"Losses: {stats["losses"]}")
def main():
    stats = {"wins": 0, "losses": 0}
    while True:
        print("__wellcome to Menue__")
        print("1) START the Game")
        print("2) Show the result")
        print("3) Exit")

        cmd = input("Choose: ").strip()
        match cmd:
            case "1":
                play_game(stats)
            case "2":
                show_stats(stats)
            case "3":
                print("Exiting ...")
                break
            case _:
                print("Invalid option")
if __name__ == "__main__":
    main()