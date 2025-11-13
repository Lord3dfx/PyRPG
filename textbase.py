import random

ROOMS = [
    'This is just empty room, with some web in corners',
    'A dark room with the strange smell...',
    'A narrow room with a torch on the wall',
    'A room full of skulls. Looks disgusting',
    'A big, bright room with a pedestal in the center',
    'Hm... There is must be a room, but here is just an empty space...'
]

CHEST = ['Simple wooden chest',
         'Big metal chest',
         'Suspicious chest...',
         'Old rusty chest',
         'Chest with a sticky slime',
         'Golden chest']

TRAP = {
    1: ['Shifted slab***', 'Wooden arrows in the wall***', 'The pit with the peaks***', 'Tight rope***'],
    2: ['Looks like a simple wooden chest', 'Great helmet on the floor', '300 gold coins on the rag', 'Biggest healing potion'],
    3: ['Simple wooden chest',
         'Big metal chest',
         'Suspicious chest...',
         'Old rusty chest',
         'Chest with a sticky slime',
         'Golden chest']
}

def get_room_name():
    return random.choice(ROOMS)

def get_chest_name():
    return random.choice(CHEST)

def get_trap_name(trap):
    return random.choice(TRAP[trap['difficulty']])