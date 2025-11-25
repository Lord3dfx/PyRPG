from engine import engine

while True:
    print("Welcome to PyRPG v0.1.3! Press 'n' to New game, or 'q' to Quit")
    option = input("Enter your option: ")
    match option:
        case "n":
            player = engine.create_player()
            if player:
                engine.main_game(player)
        case "q":
            print("Thank you for playing!")
            break
        case _:
            print("Invalid option, please try again.")
            continue

