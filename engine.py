from player import Player
import time

races = ('Human', 'Dwarf', 'Elf')

def debug_menu(player: Player):
    from items import get_equipped_item
    print('Entering debug mode...')
    while True:
        print(f'Loading player...')
        print("""DEBUG! Select an option:
        1. Add sword
        2. Add dagger
        3. Add helm
        4. Equip
        5. Print bonus stats
        6. Get inventory
        7. Get my stats
        q. Quit""")

        option = input('Select an option: ')
        match option:
            case '1':
                result = player.add_item(get_equipped_item(1))
                print(f'Get {result} item')
            case '2':
                result = player.add_item(get_equipped_item(2))
                print(f'Get {result} item')
            case '3':
                result = player.add_item(get_equipped_item(3))
                print(f'Get {result} item')
            case '4':
                option = input('Select an option: ')
                player.use_item(int(option))
            case '5':
                print(player.get_bonus_stats())
            case '6':
                all_items = player.get_all_items()
                if not all_items:
                    print("Your bag is empty...\n")
                print(all_items)
            case '7':
                print(player.get_info())
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
                    if monster.hp <= 0:
                        monster.hp = 0
                    Dungeon.delayed_print(f"You deal \033[97;41;1m {player.attack} \033[0mHP to the monster! Monster hp is \033[97;42;1m {monster.hp} \033[0m")
                    if check_win_condition(monster, player):
                        return True
                    turn = 'monster'
                case '2':
                    monster.get_info()
                case '3':
                    Dungeon.delayed_print('You are running with shame from the monster...', 1)
                    player.take_damage(monster.get_atk())
                    if check_win_condition(monster, player):
                        return False
                    del monster
                    return True
                case _:
                    print('Sorry, I didn\'t understand that')
                    continue
        elif turn == 'monster':
            Dungeon.delayed_print(f"Now it's \033[97;47;1m {monster.get_name()}'s \033[0m turn!", 1)
            player_dmg = player.take_damage(monster.get_atk())
            if check_win_condition(monster, player):
                return False
            Dungeon.delayed_print(f"He's kicked you on \033[97;41;1m {monster.get_atk()} \033[0m HP!. You get \033[97;41;1m {player_dmg} \033[0m damage! Your HP is \033[97;42;1m {player.hp} \033[0m", 1)
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
        return True
    return False

def player_is_dead(player):
    from dungeon import Dungeon
    result = player.drop_all_items()
    Dungeon.delayed_print(f"Oops! It seems like you died and lost {result} items from your inventory...!", 1)
    Dungeon.delayed_print("Return into the village...")
    player.restore()


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
