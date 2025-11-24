class Inventory:

    def __init__(self):
        self.__items = []

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
        if len(self.__items) >= 6:
            return False

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

        if self.__items[index-1].get('quantity', 1) > 1:
            self.__items[index-1]['quantity'] -= 1
            return True

        del self.__items[index-1]
        return True

    def use_item(self, index):
        if index > len(self.__items) or index < 0 or index == '':
            print('There is no item to use')
            return None

        effect = self.__items[index-1].get('stats')
        return effect

    def drop_all_items(self):
        count = 0
        for item in self.__items:
            if item.get('quantity', 1) > 1:
                count += item['quantity']
            else:
                count += 1
        self.__items = []
        return count