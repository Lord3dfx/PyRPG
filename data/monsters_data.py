import random

MONSTERS = {
    1: [
        {
            'name': 'Skeleton',
            'have_armor': False,
            'abilities': '',
        },
        {
            'name': 'Rat',
            'have_armor': False,
            'abilities': 'poison_bite'
        },
        {
            'name': 'Goblin worker',
            'have_armor': True,
            'abilities': ''
        },
        {
            'name': 'Wurm',
            'have_armor': False,
            'abilities': 'wurm_life_drain'
        },
        {
            'name': 'Bat',
            'have_armor': False,
            'abilities': 'rabid'
        },
        ],
    2: [
        {
            'name': 'Skeleton-archer',
            'have_armor': False,
            'abilities': 'pierce_shot',
        },
        {
            'name': 'Skeleton-mage',
            'have_armor': False,
            'abilities': 'magic_blast',
        },
        {
            'name': 'Skeleton-twins',
            'have_armor': True,
            'abilities': 'double_strike',
        },
    ]
}

MONSTERS_ABILITIES = {
    'poison_bite': {
        'name': 'Poison bite',
        'description': 'Deal poison damage with every attack',
        'type': 'passive',
        'actions': {
            'damage': 1,
        }
    },
    'wurm_life_drain': {
        'name': 'Wurm life drain',
        'description': 'Restore life with attack',
        'type': 'active',
        'actions': {
            'damage': 1,
            'heal': 1,
            'mana': 5
        }
    },
    'rabid': {
        'name': 'Rabid',
        'description': 'Deal damage every turn',
        'type': 'active',
        'actions': {
            'dot': 5,
            'mana': 5
        }
    },
    'pierce_shot': {
        'name': 'Pierce shot',
        'description': 'Ignore some value of your armor',
        'type': 'passive',
        'actions': {
            'pierce': 1,
        }
    },
    'magic_blast': {
        'name': 'Magic blast',
        'description': 'Deal magic damage',
        'type': 'active',
        'actions': {
            'attack': 1,
            'mana': 8
        }
    },
    'double_strike': {
        'name': 'Double strike',
        'description': 'Chance to deal 2x damage',
        'type': 'passive',
        'actions': {
            'chance': 25,
        }
    }
}

def get_monster(level):
    result = random.choice(MONSTERS[level].copy())
    return result


def get_monster_abilities(ability):
    if not ability:
        return 'none'
    result = MONSTERS_ABILITIES[ability].copy()
    return result