CONSUMABLE_ITEMS = {
    1:{'name': 'Small healing potion',
       'type': 'consumable',
       'stackable': True,
       'max_stack': 5,
       'stats': {'healing': 5},
       'value': 5},
    2:{'name': 'Medium healing potion',
       'type': 'consumable',
       'stackable': True,
       'max_stack': 5,
       'stats': {'healing': 10},
       'value': 8},
    3:{'name': 'Big healing potion',
       'type': 'consumable',
       'stackable': True,
       'max_stack': 5,
       'stats': {'healing': 5},
       'value': 12},
    4: {'name': 'Small exp potion',
        'type': 'consumable',
        'stackable': True,
        'max_stack': 5,
        'stats': {'add_exp': 2},
        'value': 3},
    5: {'name': 'Medium exp potion',
        'type': 'consumable',
        'stackable': True,
        'max_stack': 5,
        'stats': {'add_exp': 3},
        'value': 6},
    6: {'name': 'Big exp potion',
        'type': 'consumable',
        'stackable': True,
        'max_stack': 5,
        'stats': {'add_exp': 5},
        'value': 9},
}
EQUIPPED_ITEMS = {
    1:{ 'name': 'Long sword',
        'type': 'equipped',
        'stackable': False,
        'slot': 'weapon',
        'stats': {'attack': 2},
        'value': 6
        },
    2:{ 'name': 'Dagger',
        'type': 'equipped',
        'stackable': False,
        'slot': 'weapon',
        'stats': {'attack': 1},
        'value': 3
        },
    3:{ 'name': 'Iron helm',
        'type': 'equipped',
        'stackable': False,
        'slot': 'head',
        'stats': {'health': 2, 'armour': 1},
        'value': 2
        },
}

def get_consumable_item(item_id):
    return CONSUMABLE_ITEMS[item_id].copy() if item_id in CONSUMABLE_ITEMS else None

def get_equipped_item(item_id):
    return EQUIPPED_ITEMS[item_id].copy() if item_id in CONSUMABLE_ITEMS else None