import random
from data.monsters_data import get_monster, get_monster_abilities

class Monster:

    def __init__(self, player):
        self.__monster_data = get_monster(1)
        self.__monster_abilities = get_monster_abilities(self.__monster_data['abilities'])
        self.__name = self.__monster_data['name']
        self.__lvl = random.randint(player.lvl, player.lvl + 1)
        self.__atk = self.__lvl + 1
        self.__hp = self.__lvl * 2
        self.__max_hp = self.__lvl * 2
        self.__armor = 0
        self.__mana = 0

        self.__additional_atk = 0
        self.__heal = 0
        self.__piercing = 0
        self.__double_damage = False

    def __del__(self):
        print('Object deleted...')

    def get_name(self):
        return self.__name

    def get_max_hp(self):
        return self.__max_hp

    def get_lvl(self):
        return self.__lvl

    def get_atk(self):
        return self.__atk

    def get_abilities(self):
        return self.__monster_abilities

    def attack(self, player):

        if self.__monster_abilities == 'none':
            pass

        elif self.__monster_abilities['type'] == 'passive':
            print('if for passive')
            for key, value in self.__monster_abilities['actions'].items():
                if key == 'damage':
                    self.__additional_atk += value + self.__lvl // 2

                elif key == 'heal':
                    self.__heal += value + self.__lvl // 2

                elif key == 'pierce':
                    self.__piercing += value

                elif key == 'amount':
                    print('Is double damaged!')
                    result = random.randint(1, 100)
                    self.__double_damage = result < value

        elif self.__monster_abilities['type'] == 'active':
            print('if for active')
            if self.__monster_abilities['actions']['mana'] > self.__mana:
                print(f'Need mana {self.__monster_abilities['actions']['mana']}')
                print(f'Total mana is {self.__mana}.')
                self.__mana += 1
            else:
                for key, value in self.__monster_abilities['actions'].items():
                    if key == 'damage':
                        self.__additional_atk += value + self.__lvl // 2

                    elif key == 'heal':
                        self.__heal += value + self.__lvl // 2

                    elif key == 'pierce':
                        self.__piercing += value

                    elif key == 'dot':
                        player.set_dot(value, self.__monster_abilities['name'])

                    elif key == 'amount':
                        print('Is double damaged!')
                        result = random.randint(1, 100)
                        self.__double_damage = result < value

                self.__mana = 0


        self.hp += self.__heal

        if self.__double_damage:
            overall_dmg = (self.__atk * 2) + self.__additional_atk
            player.take_damage(overall_dmg, self.__piercing)
        else:
            overall_dmg = self.__atk + self.__additional_atk
            player.take_damage(overall_dmg, self.__piercing)


        self.__additional_atk = 0
        self.__heal = 0
        self.__piercing = 0
        self.__double_damage = False

        return overall_dmg

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        self.__hp = value

    def get_info(self):
        print(f"""\033[97;1mName: {self.__name}\033[0m, \033[97;43;1mlvl: {self.__lvl}\033[0m, \033[97;41;1mattack: {self.__atk}\033[0m. \033[97;42;1mCurrent hp: {self.__hp}/{self.__max_hp}\033[0m""")

    def get_battle_info(self):
        if self.__monster_abilities == 'none':
            print(f"""\033[97;1mName: {self.__name}\033[0m, \033[97;41;1mattack: {self.__atk}\033[0m. \033[97;42;1mCurrent hp: {self.__hp}/{self.__max_hp}\033[0m
Ability: no abilities!""")
        else:
            print(f"""\033[97;1mName: {self.__name}\033[0m, \033[97;41;1mattack: {self.__atk}\033[0m. \033[97;42;1mCurrent hp: {self.__hp}/{self.__max_hp}\033[0m
\033[3mAbility: {self.__monster_abilities['name']}, {self.__monster_abilities['description']}\033[0m""")