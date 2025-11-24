class Equip:

    def __init__(self):
        self.slots = {
            'head':[],
            'body':[],
            'weapon':[],
            'boots':[]
        }

    def equip(self, slot, item):
        self.slots[slot].append(item)

    def unequip(self, slot):
        return self.slots[slot].pop()

    def get_bonus_stats(self):

        bonus_stats = {'attack': 0, 'health': 0, 'armour': 0}

        for slot_name, items in self.slots.items():
            if items:
                item = items[0]
                if 'stats' in item:
                    for stat, value in item['stats'].items():
                        bonus_stats[stat] += value
        return bonus_stats