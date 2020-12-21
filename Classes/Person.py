import random
from math import ceil
from math import floor

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:

    def __init__(self, name, hp, mp, atk, defense, magic=None, items=None):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.defense = defense
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Items"]

    def generate_attack(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, damage):
        real_dmg = damage - int(self.defense/10) if damage - self.defense/10 > 0 else 0
        self.hp = self.hp - real_dmg if self.hp - real_dmg > 0 else 0
        # if self.hp < 0:
        #     self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def mana_recover(self, amount):
        self.mp += amount
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_defense(self):
        return self.defense

    def is_inventory_empty(self):
        for item in self.items:
            if item.quantity > 0:
                return False
        return True

    def can_cast_spell(self, mp):
        for spell in self.magic:
            if spell.cost <= mp:
                return True
        return False

    def reduce_mp(self, cost) -> int:
        self.mp -= cost
        return 1

    def choose_action(self):
        i = 1
        print("\n" + " " + bcolors.BOLD + bcolors.HEADER + self.name + bcolors.ENDC + "\n" + bcolors.BOLD + bcolors.OKBLUE,
              "    ACTIONS", bcolors.ENDC)
        for option in self.action:
            print("        " + str(i) + ".", option)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD, "    MAGICS", bcolors.ENDC)
        for spell in self.magic:
            if spell.magic_type == "black":
                print("        " + str(i) + ".",
                      spell.name + " (cost: " + str(spell.cost) + "  |  damage: " + str(spell.dmg) + ")")
            else:
                print("        " + str(i) + ".",
                      spell.name + " (cost: " + str(spell.cost) + "  |  heal: " + str(spell.dmg) + ")")

            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD, "    ITEMS", bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item.name + "  :  " + str(item.description) +
                  "  (x" + str(item.quantity) + ")")
            i += 1

    def choose_enemy(self, enemies):
        i = 1
        print("\n" + " " + bcolors.BOLD + bcolors.OKBLUE, "    TARGETS", bcolors.ENDC)
        for option in enemies:
            print("        " + str(i) + ".", option.name)
            i += 1


    def print_stats(self):

        hp_bar_display = ""                          # calculate how many █ need to be in HP/MP bar
        mp_bar_display = ""
        blocks_counter = floor((self.hp/self.maxhp)*100/4)
        empty_blocks_counter = ceil(25 - ((self.hp / self.maxhp) * 100 / 4))
        for i in range(blocks_counter):
            hp_bar_display += "█"
        for i in range(empty_blocks_counter):
            hp_bar_display += " "
        blocks_counter = floor((self.mp / self.maxmp) * 100 / 10)
        empty_blocks_counter = ceil(10 - ((self.mp / self.maxmp) * 100 / 10))
        for i in range(blocks_counter):
            mp_bar_display += "█"
        for i in range(empty_blocks_counter):
            mp_bar_display += " "

        initial_hp_string_len = len(str(self.maxhp) + "/" + str(self.maxhp))  # white space in HP
        current_hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp_string_len = len(current_hp_string)
        for i in range(current_hp_string_len, initial_hp_string_len):
            current_hp_string = " " + current_hp_string

        initial_mp_string_len = len(str(self.maxmp) + "/" + str(self.maxmp))  # white space in MP
        current_mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp_string_len = len(current_mp_string)
        for i in range(current_mp_string_len, initial_mp_string_len):
            current_mp_string = " " + current_mp_string

        print("                    _________________________               __________")
        print(bcolors.BOLD + self.name + "    " + current_hp_string + " |" + bcolors.OKGREEN +
              hp_bar_display + bcolors.ENDC + bcolors.BOLD + "|     " +
              current_mp_string + " |" + bcolors.OKBLUE + mp_bar_display + bcolors.ENDC + "|")

    def enemy_print_stats(self):
        hp_bar_display = ""        # calculate how many █ need to be in HP/MP bar
        blocks_counter = floor((self.hp / self.maxhp) * 100 / 2)
        empty_blocks_counter = ceil(50 - ((self.hp / self.maxhp) * 100 / 2))
        for i in range(blocks_counter):
            hp_bar_display += "█"
        for i in range(empty_blocks_counter):
            hp_bar_display += " "

        initial_hp_string_len = len(str(self.maxhp) + "/" + str(self.maxhp))  # white space in HP
        current_hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp_string_len = len(current_hp_string)
        for i in range(current_hp_string_len, initial_hp_string_len):
            current_hp_string = " " + current_hp_string

        print("                    __________________________________________________")
        print(bcolors.BOLD + self.name + "    " + current_hp_string + " |" + bcolors.FAIL +
              hp_bar_display + bcolors.ENDC + bcolors.BOLD + "|" + bcolors.ENDC)







