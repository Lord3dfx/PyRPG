from monsters import Monster
from engine import inventory_menu, battle_start, player_is_dead
import textbase
import random
import items
import time
class Dungeon:

    def __init__(self, player):
        self.player = player
        self.monster = []
        self.events = []

    def __del__(self):
        print('Dungeon is deleted!')

    @staticmethod
    def delayed_print(text, delayed=0.5):
        print(text)
        time.sleep(delayed)

    def generate_chest(self):
        dice = random.randint(1, 4)
        match dice:
            case 1:
                self.events.append({'type':'chest', 'reward': True})
            case 2:
                self.events.append({'type':'chest', 'reward': False})
            case 3:
                self.events.append({'type':'chest_mimic', 'reward': True})
            case 4:
                self.events.append({'type':'chest_mimic', 'reward': False})

    def generate_trap(self):
        dice = random.randint(1, 3)
        self.events.append({'type':'trap', 'difficulty': dice})

    def generate_monster(self, pos=0):
        self.events.append({'type':'monster', 'position': pos})

    def build_dungeon(self):
        monster_position = 0
        for i in range(random.randint(1, 5)):
            dice = random.randint(1, 3)
            match dice:
                case 1:
                    self.generate_trap()
                case 2:
                    self.generate_chest()
                case 3:
                    self.generate_monster(monster_position)
                    monster_position += 1

    def react_to_choice(self, event):
        if event['type'] == 'chest':
            item = items.get_consumable_item(random.randint(1, 6))
            print(f'You get a \033[106;1m {item['name']} \033[0m')
            self.player.add_item(item)
            return True
        elif event['type'] == 'chest_mimic':
            item = items.get_consumable_item(random.randint(1, 6))
            self.player.add_item(item)
            self.player.take_true_damage(2)
            result = self.player.hp <= 0
            print(f"Oh, it was mimic! You got \033[106;1m {item['name']} \033[0m and \033[97;41;1m 2 \033[0m damage!")
            if result:
                return 'Player_dead'
            return True
        elif ['type'] == 'trap':
            print(f"You stuck in trap! You got \033[97;41;1m 4 \033[0m damage!")
            self.player.take_true_damage(4)
            result = self.player.hp <= 0

            if result:
                return 'Player_dead'

            return True
        elif event['type'] == 'monster':
            result = battle_start(self.monster[event['position']], self.player)

            if not result:
                return 'Player_dead'

            return True
        elif event == 'next':
            return False
        return False

    def clear_events(self):
        self.events = []
        self.monster = []

    @staticmethod
    def print_list_menu(list_menu, number):
        option_number = number
        for item in list_menu:
            print(f'    {option_number}. {item}')
            option_number += 1

    def dungeon_menu(self):
        print('Dungeon menu')
        while True:
            list_menu = []
            self.build_dungeon()
            room_name = textbase.get_room_name()
            if not list_menu:
                for event in self.events:
                    if event['type'] == 'chest':
                        list_menu.append(textbase.get_chest_name())
                    elif event['type'] == 'trap':
                        list_menu.append(textbase.get_trap_name(event))
                    elif event['type'] == 'chest_mimic':
                        list_menu.append(textbase.get_chest_name())
                    elif event['type'] == 'monster':
                        self.monster.append(Monster(self.player))
                        list_menu.append(f'\033[97;1m{self.monster[event['position']].get_name()} \033[0mis here and he is \033[97;43;1m {self.monster[event['position']].get_lvl()} \033[0m LVL!')


            while True:
                has_monsters = any(event.get('type') == 'monster' for event in self.events)

                if not has_monsters:
                    if not any(event.get('type') == 'next' for event in self.events):
                        self.events.append({'type': 'next'})
                        list_menu.append('Going to the next room...')

                print(f'\033[3m{room_name}\033[0m')
                self.print_list_menu(list_menu, 1)
                print("    'e' for leaving dungeon")
                print("    'i' for open inventory")
                print("    's' for your stats")
                option = input('Your choice: ')

                if option == 'e':
                    self.delayed_print('Return to village...')
                    return False
                if option == 'i':
                    inventory_menu(self.player)
                    continue
                if option == 's':
                    self.player.get_info()
                    continue

                result = self.react_to_choice(self.events[int(option)-1])

                if result == 'Player_dead':
                    player_is_dead(self.player)
                    return False

                if result:
                    self.events.pop(int(option)-1)
                    list_menu.pop(int(option)-1)
                    continue

                else:
                    self.clear_events()

                    break





