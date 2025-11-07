class Inventory:

    def __init__(self):
        self.__items = [{'name': 'Small healing potion',
       'type': 'consumable',
       'stackable': True,
       'max_stack': 5,
       'stats': {'healing': 5},
       'value': 5}]
        print('Inventory is created')

    def get_all_items(self):
        if not self.__items:
            return None
        result = []
        for i, item in enumerate(self.__items, 1):
            if item.get('quantity', 1) > 1:
                result.append(f"{i}. {item['name']} (x{item['quantity']})")
            else:
                result.append(f"{i}. {item['name']}")

        return "\n".join(result)

    def get_item(self, index):
        try:
            return self.__items[index-1]
        except IndexError:
            return None
        except ValueError:
            return None

    def add_item(self, item):
        if item.get('stackable', True):
            for is_exist in self.__items:
                if is_exist.get('name') == item['name']:
                    is_exist['quantity'] += 1
                    return True

        item['quantity'] = 1
        self.__items.append(item)
        return True

    def remove_item(self, index):
        if index > len(self.__items):
            return None
        del self.__items[index-1]
        return True

    def use_item(self, index):
        if index > len(self.__items) or index < 0 or index == '':
            print('There is no item to use')
            return None

        effect = self.__items[index-1].get('stats')
        return effect

