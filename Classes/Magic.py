import random


class Magic:

    def __init__(self, name, cost, dmg, magic_type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.magic_type = magic_type

    def generate_spell_damage(self):
        spell_damage_l = self.dmg - 15
        spell_damage_h = self.dmg + 15
        return random.randrange(spell_damage_l, spell_damage_h)
