from player import Player
import time

races = ('Human', 'Dwarf', 'Elf')

def debug_menu(player: Player):
    from dungeon import Dungeon
    print('Entering debug mode...')
    while True:
        print(f'Loading player...')
        print("""DEBUG! Select an option:
        1. Generate dungeon
        2. DUNGEON TEST!!!
        q. Quit""")

        option = input('Select an option: ')
        match option:
            case '1':
                dungeon = Dungeon(player)
                print(dungeon.build_dungeon())
                del dungeon
            case '2':
                dungeon = Dungeon(player)
                dungeon.dungeon_menu()
                del dungeon
            case 'q':
                break

def create_player():
    while True:
        name = input("Enter your name: ")
        race = input("""Select your race:
        1. Human
        2. Dwarf
        3. Elf
        """)
        if race not in "123" or race == '':
            print("Failed to create character. Try again...\n")
            continue
        return Player(name, races[int(race)-1])

def inventory_menu(player):
    print("Let's see, what in your bag...\n")
    while True:
        all_items = player.get_all_items()
        if not all_items:
            print("Your bag is empty...\n")
            break
        print("""Select an option:
        1. View all items
        2. Use item
        3. Close bag""")
        option = input('Select an option: ')
        match option:
            case '1':
                print(all_items)
            case '2':
                option = input('What item would you choose? \n')
                if option == '':
                    print('Something went wrong... Try again')
                    return
                player.use_item(int(option))
            case '3':
                break
            case _:
                print('Sorry, I don\'t understand that')
                continue

def battle_start(monster, player):
    from dungeon import Dungeon
    turn = 'player'
    Dungeon.delayed_print('Watch out!!!', 1)
    Dungeon.delayed_print(f"This is\033[97;1m {monster.get_name()}\033[0m!!! He is a \033[97;43;1m {monster.get_lvl()} \033[0m LVL.")
    Dungeon.delayed_print(f"Now you must to fight!!!")
    while True:
        if turn == 'player':
            print(f"""It's your turn. What you want to do?
            1. Attack monster. Your attack is \033[97;41;1m {player.attack} \033[0m
            2. Show monster info
            3. Try to escape (You wil loose \033[97;41;1m {monster.get_atk()} \033[0m HP)""")
            option = input('Your option: ')
            match option:
                case '1':
                    print('BAM!!!')
                    monster.hp = monster.hp - player.attack
                    Dungeon.delayed_print(f"You deal \033[97;41;1m {player.attack} \033[0mHP to the monster!")
                    if check_win_condition(monster, player):
                        break
                    turn = 'monster'
                case '2':
                    monster.get_info()
                case '3':
                    Dungeon.delayed_print('You are running with shame from the monster...', 1)
                    del monster
                    return True
                case _:
                    print('Sorry, I didn\'t understand that')
                    continue
        elif turn == 'monster':
            Dungeon.delayed_print(f"Now it's \033[97;47;1m {monster.get_name()}'s \033[0m turn!", 1)
            player.take_damage(monster.get_atk())
            if check_win_condition(monster, player):
                return False
            Dungeon.delayed_print(
                f"He's kicked you on \033[97;41;1m {monster.get_atk()} \033[0m HP!. Your HP is {player.hp}", 1)
            turn = 'player'
    return True

def check_win_condition(monster, player):
    from dungeon import Dungeon
    if monster.hp <= 0:
        Dungeon.delayed_print(f"The \033[97;47;1m {monster.get_name()} \033[0m is defeated!", 1)
        Dungeon.delayed_print(f"You get an {monster.get_lvl() + monster.get_max_hp()} EXP!")
        player.add_exp(monster.get_lvl() + monster.get_max_hp())
        return True
    elif player.hp <= 0:
        Dungeon.delayed_print(f"Oh! The \033[97;47;1m {monster.get_name()} \033[0m is defeat you!", 1)
        Dungeon.delayed_print("Return into the village...")
        player.restore()
        return True
    else:
        return False

def dungeon_entering(player):
    from dungeon import Dungeon
    dungeon = Dungeon(player)
    dungeon.dungeon_menu()
    del dungeon

def main_game(player):
    print(f"Welcome, {player.name}, your race is {player.race}. ")
    while True:
        print("""Select, what you would to do:
            1. Your stats
            2. Shop
            3. Your inventory
            4. Go to the dungeon...
            5. Return to main menu""")
        option = input("Enter your option: ")

        match option:
            case "1":
                player.get_info()
            case "2":
                print('Shop is closed right now...')
            case "3":
                inventory_menu(player)
            case "4":
                dungeon_entering(player)
            case "5":
                print("Returning to menu...")
                time.sleep(1)
                break
            case "6":
                debug_menu(player)
            case _:
                print("Invalid option, please try again.")
