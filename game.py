from Classes.Person import Person
from Classes.Person import bcolors
from Classes.Magic import Magic
from Classes.Inventory import Item
import random


# Create Some Magics
fire = Magic(name="Fire", cost=45, dmg=110, magic_type="black")
ice = Magic(name="Ice", cost=55, dmg=120, magic_type="black")
earth = Magic(name="Earth", cost=65, dmg=130, magic_type="black")
heal = Magic(name="Heal", cost=50, dmg=250, magic_type="white")
mass_heal = Magic(name="Mass Heal", cost=75, dmg=500, magic_type="white")
player_magics = [fire, ice, earth, heal, mass_heal]


# Create Some Items
small_hp_potion = Item(name="Small HP Potion", item_type="potion", description="Heals for 150 HP",
                       value=150, quantity=3)
medium_hp_potion = Item(name="Medium HP Potion", item_type="potion", description="Heals for 300 HP",
                        value=300, quantity=3)
large_hp_potion = Item(name="Large HP Potion", item_type="potion", description="Heals for 750 HP",
                       value=750, quantity=3)
super_elixer = Item(name="Super Elixer", item_type="elixer", description="Fully restores HP/MP",
                    value=99999, quantity=3)
mega_elixer = Item(name="Mega Elixer", item_type="elixer", description="Fully restores HP/MP of all party members",
                   value=99999, quantity=3)
grenade = Item(name="Grenade", item_type="explosive", description="Deals 500 damage", value=500, quantity=2)
player_items = [small_hp_potion, medium_hp_potion, large_hp_potion, super_elixer, mega_elixer, grenade]


# Create Some Players and Enemies
player1 = Person(name= "Belgy", hp=1500, mp=300, defense=100, atk=80, magic=player_magics, items=player_items)
player2 = Person(name= "Liron", hp=1300, mp=330, defense=100, atk=80, magic=player_magics, items=player_items)
player3 = Person(name= "Yarin", hp=1400, mp=360, defense=100, atk=90, magic=player_magics, items=player_items)
enemy1 = Person(name="Imp  ", hp=1250, mp=400, defense=200, atk=140)
enemy2 = Person(name="Magos", hp=7650, mp=400, defense=130, atk=100)
enemy3 = Person(name="Imp  ", hp=1250, mp=400, defense=200, atk=140)
players_list = [player1, player2, player3]
enemy_list = [enemy1, enemy2, enemy3]


# Some Helping Functions
def are_all_enemies_dead() -> bool:
    if len(enemy_list) == 0:
        return True
    return False


def are_all_players_dead() -> bool:
    if len(players_list) == 0:
        return True
    return False


def end_of_game_WON():
    print("====================================================================")
    print("NAME                HP                                      MP")
    for playerrr in players_list:
        playerrr.print_stats()
    print("\n")
    for enemyy in enemy_list:
        enemyy.enemy_print_stats()
    print("====================================================================")
    print("\n" + bcolors.OKGREEN + bcolors.BOLD, "\nYou Won", bcolors.ENDC)


def end_of_game_LOST():
    print("====================================================================")
    print("NAME                HP                                      MP")
    for playerrr in players_list:
        playerrr.print_stats()
    print("\n")
    print("NAME                HP")
    for enemyy in enemy_list:
        enemyy.enemy_print_stats()
    print("====================================================================")
    print("\n" + bcolors.OKGREEN + bcolors.BOLD, "\nYou Lost", bcolors.ENDC)


def main():
    running = True
    print("\n")
    while running:
        print(
            "====================================================================")  # Now we print the current state values
        print("NAME                HP                                      MP")
        for player in players_list:
            player.print_stats()
        print("\n")
        print("NAME                HP")
        for enemy in enemy_list:
            enemy.enemy_print_stats()
        print("\n")
        print("====================================================================")
        for player in players_list:
            player.choose_action()
            chosen_action = int(input("\n" + "    Choose Action: ")) - 1
            while int(chosen_action) >= len(player.action) or chosen_action < 0:  # Check input validity
                print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                chosen_action = int(input("\n" + "    Choose Action: ")) - 1
            while chosen_action == 2 and player.is_inventory_empty():  # gain access to inventory if and only if it is not empty.
                print("\n" + bcolors.FAIL, "   Inventory empty", bcolors.ENDC)
                chosen_action = int(input("\n" + "    Choose Action: ")) - 1
                while int(chosen_action) >= len(player.action) or chosen_action < 0:  # Check input validity
                    print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                    chosen_action = int(input("\n" + "    Choose Action: ")) - 1
            # gain access to magic menu if and only if player has enough mana for certain spell.
            while chosen_action == 1 and player.can_cast_spell(player.get_mp()) is False:
                print("\n" + bcolors.FAIL, "   Not enough mana for any magic.", bcolors.ENDC)
                chosen_action = int(input("\n" + "    Choose Action: ")) - 1
                while int(chosen_action) >= len(player.action) or chosen_action < 0:  # Check input validity
                    print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                    chosen_action = int(input("\n" + "    Choose Action: ")) - 1
            print("--------------------------------------")
            # player chose regular Attack.
            if chosen_action == 0:
                player.choose_enemy(enemy_list)
                chosen_target = int(input("\n" + "    Choose Target: ")) - 1
                while int(chosen_target) >= len(enemy_list) or chosen_target < 0:  # Checks input validity
                    print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                    chosen_target = int(input("\n" + "    Choose Target: ")) - 1
                print("--------------------------------------")
                dmg = player.generate_attack()
                enemy_list[chosen_target].take_damage(dmg)
                print("\n" + player.name + " attacked " + enemy_list[chosen_target].name.replace("  ", "") +
                      " for", str(dmg-int(enemy_list[chosen_target].get_defense()/10)),
                      "points of damage." + bcolors.OKBLUE + " (" + str(int(enemy_list[chosen_target].get_defense()/10))
                      + " absorbed because enemy's defense" + bcolors.ENDC)
                if enemy_list[chosen_target].get_hp() == 0:  # checks if monster died after an attack
                    print("\n" + enemy_list[chosen_target].name.replace("  ", "") + " Died.")
                    enemy_list.remove(enemy_list[chosen_target])
                if are_all_enemies_dead() == True:     # Checks if all enemies are dead
                    end_of_game_WON()
                    return 0

                print("--------------------------------------")
            # player chose to cast a Magic
            elif chosen_action == 1:
                player.choose_magic()
                chosen_magic = int(input("\n" + "    Choose Magic: ")) - 1
                # if chosen_magic == -1:
                #     continue
                while int(chosen_magic) >= len(player.magic) or chosen_magic < 0:  # Checks input validity
                    print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                    chosen_magic = int(input("\n" + "    Choose Magic: ")) - 1
                #print("--------------------------------------")
                spell = player.magic[chosen_magic]
                while spell.cost > player.get_mp():         # Checks if player has enough mp to cast the magic
                    print("\n" + bcolors.FAIL, "   Not enough Mana.", bcolors.ENDC)
                    chosen_magic = int(input("\n" + "    Choose Magic: ")) - 1
                    while int(chosen_magic) >= len(player.magic) or chosen_magic < 0:  # Checks input validity
                        print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                        chosen_magic = int(input("\n" + "    Choose Magic: ")) - 1
                    spell = player.magic[chosen_magic]

                print("--------------------------------------")
                # We got here to cast a spell
                spell_dmg = spell.generate_spell_damage()
                # If it is Black Spell
                if spell.magic_type == "black":
                    player.choose_enemy(enemy_list)
                    chosen_target = int(input("\n" + "    Choose Target: ")) - 1
                    while int(chosen_target) >= len(enemy_list) or chosen_target < 0:  # Checks input validity
                        print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                        chosen_target = int(input("\n" + "    Choose Target: ")) - 1
                    print("--------------------------------------")
                    enemy_list[chosen_target].take_damage(spell_dmg)
                    print("\n" + bcolors.OKBLUE + str(spell.name), "deals",
                          str(spell_dmg-int(enemy_list[chosen_target].get_defense()/10)), "points of damage to " +
                          enemy_list[chosen_target].name.replace("  ", "") + ". (" +
                          str(int(enemy_list[chosen_target].get_defense()/10)) + " absorbed because enemy's defense)"
                          + bcolors.ENDC)
                    if enemy_list[chosen_target].get_hp() == 0:  # checks if monster died after an attack
                        print("\n" + enemy_list[chosen_target].name.replace("  ", "") + " Died.")
                        enemy_list.remove(enemy_list[chosen_target])
                    if are_all_enemies_dead() == True:     # Checks if all enemies are dead
                        end_of_game_WON()
                        return 0
                # If it is White Spell
                elif spell.magic_type == "white":
                    player.heal(spell_dmg)
                    print("\n" + bcolors.OKBLUE + str(spell.name), "heals for", str(spell_dmg), "HP.", bcolors.ENDC)
                player.reduce_mp(spell.cost)
                print("--------------------------------------")
            # player chose to look in the inventory
            elif chosen_action == 2:
                player.choose_item()
                chosen_item = int(input("\n" + "    Choose Item: ")) - 1
                while int(chosen_item) >= len(player.items) or chosen_item < 0:  # Checks input validity
                    print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                    chosen_item = int(input("\n" + "    Choose Item: ")) - 1
                #print("--------------------------------------")
                item = player.items[chosen_item]
                while item.quantity <= 0:           # Checks if we have this item in our inventory
                    print("\n" + bcolors.FAIL, "   None left...", bcolors.ENDC)
                    chosen_item = int(input("\n" + "    Choose Item: ")) - 1
                    while int(chosen_item) >= len(player.items) or chosen_item < 0:  # Checks input validity
                        print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                        chosen_item = int(input("\n" + "    Choose Item: ")) - 1
                    item = player.items[chosen_item]

                print("--------------------------------------")
                if item.item_type == "potion":
                    player.heal(item.value)
                    print("\n" + bcolors.OKBLUE + str(item.name), "heals for", str(item.value), "HP.", bcolors.ENDC)
                elif item.item_type == "elixer":
                    if item.name == "Mega Elixer":
                        for playerr in players_list:
                            playerr.heal(item.value)
                            playerr.mana_recover(item.value)
                        print("\n" + bcolors.OKBLUE + str(item.name), "fully healed HP/MP of all party members.",
                                  bcolors.ENDC)
                    else:
                        player.heal(item.value)
                        player.mana_recover(item.value)
                        print("\n" + bcolors.OKBLUE + str(item.name), "fully healed HP/MP.", bcolors.ENDC)

                elif item.item_type == "explosive":
                    player.choose_enemy(enemy_list)
                    chosen_target = int(input("\n" + "    Choose Target: ")) - 1
                    while int(chosen_target) >= len(enemy_list) or chosen_target < -1:  # Checks input validity
                        print("\n" + bcolors.FAIL, "   Invalid Choice.", bcolors.ENDC)
                        chosen_target = int(input("\n" + "    Choose Target: ")) - 1
                    print("--------------------------------------")
                    enemy_list[chosen_target].take_damage(item.value)
                    print("\n" + bcolors.OKBLUE + str(item.name), "deals", str(item.value), "points of damage.",
                          bcolors.ENDC)
                    if enemy_list[chosen_target].get_hp() == 0:  # checks if monster died after an attack
                        print("\n" + enemy_list[chosen_target].name.replace("  ", "") + " Died.")
                        enemy_list.remove(enemy_list[chosen_target])
                    if are_all_enemies_dead() == True:           # Checks if all enemies are dead
                        end_of_game_WON()
                        return 0
                item.quantity -= 1
                print("--------------------------------------")
        # now it is enemy turn to attack us
        for enemy in enemy_list:
            enemy_dmg = enemy.generate_attack()
            target = random.randrange(0, len(players_list))
            players_list[target].take_damage(enemy_dmg)
            print(enemy.name.replace("  ", "") + " attacked " + players_list[target].name + " for",
                  str(enemy_dmg-int(players_list[target].get_defense()/10)),
                  "points of damage." + bcolors.OKBLUE + " (" + str(int(players_list[target].get_defense()/10)) +
                  " absorbed because player's defense)" + bcolors.ENDC)
            if players_list[target].get_hp() == 0:
                print("\n" + players_list[target].name + " Died.")
                players_list.remove(players_list[target])
                if are_all_players_dead() == True:      # Checks if all players are dead
                    end_of_game_LOST()
                    return 0


if __name__ == "__main__":
    main()


