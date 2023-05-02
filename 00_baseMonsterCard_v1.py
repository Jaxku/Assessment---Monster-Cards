"""""
00_baseMonsterCard_v1.py
Base v1
"""


import easygui

# Dictionary to store the details of monster cards
creatures = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

# Function to display the menu



# Function to search for a creature (used by the display menu function
def search_creature():
    creature_name = easygui.enterbox("Enter the name of the creature you want to search for:", "Search")
    # Allows user to search for the creature using an enter-box gui
    if creature_name is None:
        return
    if creature_name in creatures:
        creature_stats = creatures[creature_name]
        easygui.msgbox("Creature: {}\nStrength: {}\nSpeed: {}\nStealth: {}\nCunning: {}".format(creature_name, creature_stats["Strength"], creature_stats["Speed"], creature_stats["Stealth"], creature_stats["Cunning"]))
    else:
        easygui.msgbox("Creature not found.")
        pass