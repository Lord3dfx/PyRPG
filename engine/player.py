from .inventory import Inventory
from .equip import Equip

class Player:

    def __init__(self, name, race):
        self.__name = name
        self.__race = race
        self.__lvl = 1
        self.__exp = 0
        self.__inventory = Inventory()
        self.__equip = Equip()

        self.__base_atk = 1
        self.__base_max_hp = 5
        self.__base_armour = 0

        self.__attack_str = 0
        self.__max_hp = 0
        self.__armour = 0
        self.__hp = self.__base_max_hp

        self.__dot = 0
        self.__debuff = ''

        self.__update()

    def __update(self):
        bonus_stats = self.get_bonus_stats()

        self.__attack_str = self.__base_atk * self.__lvl + bonus_stats['attack']
        self.__max_hp = self.__base_max_hp * self.__lvl + bonus_stats['health']
        self.__armour = self.__base_armour + bonus_stats['armour']

        if self.__hp > self.__max_hp:
            self.restore()

    def level_up(self):
        self.__lvl += 1
        self.__exp = 0
        self.__update()
        self.restore()

    def restore(self):
        self.__hp = self.__max_hp

    def check_player_lvlup(self):
        if self.exp >= self.lvl * 5:
            self.level_up()
            print(f"Congratulations, your level is up! Now it's\033[97;43;1m {self.lvl} \033[0mlevel.")

    @property
    def hp(self):
        return self.__hp

    def take_damage(self, value, pierce = 0):
        piercing_armor = self.__armour - pierce
        if piercing_armor < 0:
            piercing_armor = 0
        result = value - piercing_armor
        if result < 0:
            result = 0
        self.__hp -= result
        return result

    def take_true_damage(self, value):
        self.__hp -= value

    def clear_dot(self):
        self.__dot = 0
        self.__debuff = ''

    def set_dot(self, value, debuff):
        self.__dot += value
        self.__debuff = debuff

    def take_dot(self):
        if self.__dot > 0:
            self.__hp -= 1
            self.__dot -= 1
            print(f'Oh! you get 1 dmg from {self.__debuff}!')

    def healing(self, value):
        if self.__hp == self.__max_hp:
            print('You are already healthy')
            return False
        elif value >= self.__max_hp - self.__hp:
            print(f'You restore {self.__max_hp - self.__hp} HP!')
            self.__hp += self.__max_hp - self.__hp
            return True
        else:
            self.__hp += value
            print(f'You restore {value} HP!')
            return True

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def lvl(self):
        return self.__lvl

    @property
    def attack(self):
        return self.__attack_str

    @property
    def race(self):
        return self.__race
    @race.setter
    def race(self, value):
        self.__race = value

    @property
    def exp(self):
        return self.__exp

    def add_exp(self, value):
        self.__exp += value
        self.check_player_lvlup()
        return True

    @property
    def max_hp(self):
        return self.__max_hp

    def add_item(self, item):
        return self.__inventory.add_item(item)

    def get_all_items(self):
        return self.__inventory.get_all_items()

    def use_item(self, index):
        if self.__inventory.get_item(index) is None:
            print('There is no item')

        if self.__inventory.get_item(index)['type'] == 'consumable':
            item = self.__inventory.use_item(index)
            effect_name, value = next(iter(item.items()))
            result = getattr(self, effect_name)(value)
            if not result:
                return None
            print(f"You have used {self.__inventory.get_item(index)['name']}")
            self.__inventory.remove_item(index)
            return True

        if self.__inventory.get_item(index)['type'] == 'equipped':
            equip_item = self.__inventory.get_item(index)
            if not self.__equip.slots[equip_item['slot']]:
                print(f"You have equip {self.__inventory.get_item(index)['name']} in slot: {equip_item['slot']}")
                self.__equip.equip(equip_item['slot'], equip_item)
                self.__inventory.remove_item(index)
                self.__update()
                return True
            else:
                in_equip = self.__equip.slots[equip_item['slot']]

                print(f'You have equipped\033[97;1m {in_equip[0]['name']}\033[0m which give you \033[97;43;1m {self.normalize_stats(in_equip[0]['stats'])} \033[0m. Would you like to replace it with\033[97;1m {equip_item['name']}\033[0m which give you\033[97;43;1m {self.normalize_stats(equip_item['stats'])} \033[0m?')
                option = input('y - to replace, n - return: ').lower()

                if option == 'n':
                    return False
                elif option == 'y':
                    to_inventory = self.__equip.unequip(in_equip[0]['slot'])
                    self.__equip.equip(equip_item['slot'], equip_item)
                    self.__inventory.remove_item(index)
                    self.__inventory.add_item(to_inventory)
                    self.__update()
                    return True
        return False

    def get_info(self):
        print(f"""\033[97;1mName: {self.__name} \033[0m, \033[97;43;1m LVL: {self.__lvl} \033[0m, \033[97;44;1m Race: {self.__race} \033[0m, \033[97;41;1m Attack: {self.__attack_str} \033[0m. \033[97;42;1m Your HP:{self.__hp}\\{self.__max_hp} \033[0m, \033[97;40;1m Your armor: {self.__armour} \033[0m,\033[97;45;1m EXP: {self.__exp} \033[0m (need \033[97;35;1m{(self.__lvl * 5) - self.__exp} \033[0mEXP to level up)
\033[3mReady for adventures...\033[0m\n""")

    @staticmethod
    def normalize_stats(stats):
        stats_text = ", ".join([f"{stat} is {value}" for stat, value in stats.items()])
        return stats_text

    def get_bonus_stats(self):
        return self.__equip.get_bonus_stats()

    def drop_all_items(self):
        result = self.__inventory.drop_all_items()
        return result