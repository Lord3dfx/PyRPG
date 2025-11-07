import items
from player import *
from monsters import *
import time
import random

races = ('Human', 'Dwarf', 'Elf')

def debug_menu(player: Player):
    print('Entering debug mode...')
    while True:
        print(f'Loading player...')
        print("""DEBUG! Select an option:
        1. Add item
        2. Get all items
        3. Get item
        q. Quit""")

        option = input('Select an option: ')
        match option:
            case '1':
                player.add_item(items.get_consumable_item(1))
            case '2':
                if player.get_all_items():
                    print(player.get_all_items())
                else:
                    print("Your bag is empty...")
            case '3':
                if player.get_all_items():
                    option = input('What item would you choose? \n')
                    print(player.get_item(int(option)))
                else:
                    print("Your bag is empty...")
            case 'q':
                break

def inventory_menu(player: Player):
    print("Let's see, what in your bag...")
    while True:
        all_items = player.get_all_items()
        if not all_items:
            print("Your bag is empty...")
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


def delayed_print(text, delayed=0.5):
    print(text)
    time.sleep(delayed)

def moving_in_dungeon():
    delayed_print("""There is two ways, where you can go... What would you choose?
            1. Turn left
            2. Turn right
            3. Exit the dungeon
            4. Get my info""")
    result = input('Your option: ')
    return result

def check_player_lvlup(player):
    if player.exp >= player.lvl * 5:
        player.level_up()
        print(f"Congratulations, your level is up! Now it's\033[97;43;1m {player.lvl} \033[0mlevel.")

def check_win_condition(monster: Monster, player: Player):
    if monster.hp <= 0:
        delayed_print(f"The \033[97;47;1m {monster.get_name()} \033[0m is defeated!", 1)
        delayed_print(f"You get an {monster.get_lvl() + monster.get_max_hp()} EXP!")
        player.add_exp(monster.get_lvl() + monster.get_max_hp())
        check_player_lvlup(player)
        return True
    elif player.hp <= 0:
        delayed_print(f"Oh! The \033[97;47;1m {monster.get_name()} \033[0m is defeat you!", 1)
        delayed_print("Return into the village...")
        player.healing(player.max_hp)
        return True
    else:
        return False

def battle_start(player: Player):
    monster = Monster(player)
    turn = 'player'
    delayed_print('Watch out!!!', 1)
    delayed_print(f"This is \033[97;47;1m {monster.get_name()} \033[0m!!! He is a \033[97;43;1m {monster.get_lvl()} \033[0m LVL.")
    delayed_print(f"Now you must to fight!!!")
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
                    delayed_print(f"You deal \033[97;41;1m {player.attack} \033[0mHP to the monster!")
                    if check_win_condition(monster, player):
                        break
                    turn = 'monster'
                case '2':
                    monster.get_info()
                case '3':
                    delayed_print('You are running with shame from the monster...', 1)
                    del monster
                    break
                case _:
                    print('Sorry, I didn\'t understand that')
                    continue
        elif turn == 'monster':
            delayed_print(f"Now it's \033[97;47;1m {monster.get_name()}'s \033[0m turn!", 1)
            player.take_damage(monster.get_atk())
            if check_win_condition(monster, player):
                return False
            delayed_print(f"He's kicked you on \033[97;41;1m {monster.get_atk()} \033[0m HP!. Your HP is {player.hp}", 2)
            turn = 'player'
    return True

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

def dungeon_entering(player):
    delayed_print('Entering the dungeon...')
    while True:
        option = moving_in_dungeon()
        if option == '1':
            dice = random.randint(1, 10)
            if dice in range(1, 4):
                delayed_print('You found a treasure!')
            elif dice in range(4, 7):
                delayed_print('You see some skelets...')
            elif dice in range(7, 11):
               result = battle_start(player)
               if result:
                   continue
               else:
                   break
        elif option == '2':
            dice = random.randint(1, 10)
            if dice in range(1, 4):
                delayed_print('Oh. Some cute shrooms...')
            elif dice in range(4, 7):
                delayed_print('Some sticky mud on the floor... Ewww...')
            elif dice in range(7, 11):
                battle_start(player)
        elif option == '3':
            delayed_print('Returning to the village...')
            return
        elif option == '4':
            print(player.get_info())
        else:
            print('Failed to enter the dungeon. Try again...\n')

def main_game(player):
    print(f"Welcome, {player.name}, your race is {player.race}. ")
    while True:
        print("""Select, what you would to do:
            1. Your stats
            2. Shop
            3. Your inventory
            4. Go to the dungeon...
            5. Return to main menu
            6. DEBUG Menu""")
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
