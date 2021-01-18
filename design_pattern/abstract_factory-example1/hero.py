from character import Character
from ironman import IronMan
from captainamerica import CaptainAmerica
import random

class Hero:
    heroes = ['Iron Man','Captain America']

    power_bonus = {
        'laser' : 10,
        'strength': 8,
        'strategy':3
    }

    defense_bonus = {
        'armor': 5,
        'shield':4,
        'movement':2
    }

    @classmethod
    def get_hero(cls):
        return random.choice(cls.heroes)

    @staticmethod
    def factory(hero_type,name):
        if hero_type == 'Iron Man':
            return IronMan(name)
        elif hero_type == 'Captain America':
            return CaptainAmerica(name)
        else:
            return None
    