def start_game():
    print("Welcome to the Adventure!")
    print("You are standing in a dark forest.")
    print("Do you want to go left or right?")

    choice = input("Enter 'left' or 'right': ").strip().lower()

    if choice == "left":
        print("You found a hidden path.")
    elif choice == "right":
        print("You found a river and must turn back.")
    else:
        print("Invalid choice.")


start_game()
