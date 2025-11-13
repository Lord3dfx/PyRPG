from monsters import Monster
from engine import inventory_menu, battle_start
import textbase
import random
import items
import time
class Dungeon:

    def __init__(self, player):
        self.player = player
        self.monster = []
        self.events = []
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

    def generate_monster(self):
        self.events.append({'type':'monster'})

    def build_dungeon(self):
        for i in range(random.randint(1, 5)):
            dice = random.randint(1, 3)
            match dice:
                case 1:
                    self.generate_trap()
                case 2:
                    self.generate_chest()
                case 3:
                    self.generate_monster()
        print('***Dungeon builded...')

    def react_to_choice(self, event, monster_number):
        print(event)
        if event == 'chest':
            item = items.get_consumable_item(random.randint(1, 6))
            print(f'You get a \033[106;1m {item['name']} \033[0m')
            self.player.add_item(item)
            return True
        elif event == 'chest_mimic':
            item = items.get_consumable_item(random.randint(1, 6))
            self.player.add_item(item)
            self.player.take_damage(2)
            print(f"Oh, it was mimic! You got \033[106;1m {item['name']} \033[0m and \033[97;41;1m 2 \033[0m damage!")
            return True
        elif event == 'trap':
            print(f"You stuck in trap! You got \033[97;41;1m 4 \033[0m damage!")
            self.player.take_damage(4)
            return True
        elif event == 'monster':
            battle_start(self.monster[monster_number-1], self.player)
            return True
        elif event == 'next':
            return False
        return False

    def clear_events(self):
        self.events = []
        self.monster = []

    @staticmethod
    def print_list_menu(list_menu, option_number):
        for item in list_menu:
            print(f'{option_number}. {item}')
            option_number += 1

    def dungeon_menu(self):
        list_menu = []
        monster_number = 0
        while True:
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
                        monster_number += 1
                        list_menu.append(f'\033[97;1m{self.monster[monster_number-1].get_name()} \033[0m is here and he is \033[97;43;1m {self.monster[monster_number-1].get_lvl()} \033[0m LVL!')

            monster_number = 0

            while True:
                has_monsters = any(event.get('type') == 'monster' for event in self.events)

                if not has_monsters:
                    self.events.append({'type': 'next'})
                    list_menu.append('Going to the next room...')

                print(f'\033[3m{room_name}\033[0m')
                self.print_list_menu(list_menu, 1)
                print("'e' for leaving dungeon")
                print("'i' for open inventory")
                option = input('Your choice: ')

                if option == 'e':
                    return False
                if option == 'i':
                    inventory_menu(self.player)
                    continue

                result = self.react_to_choice(self.events[int(option)-1]['type'], monster_number)

                if result:
                    self.events.pop(int(option)-1)
                    list_menu.pop(int(option)-1)
                    continue
                else:
                    list_menu = []
                    self.clear_events()
                    break





