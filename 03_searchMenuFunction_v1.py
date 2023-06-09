"""""
03_searchMenuFunction_v1
This function allows the menu function (02) to search the creatyres from the creature dictionary.
"""
import easygui

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


# Function to search for a creature
def search_creature():
    creature_name = easygui.enterbox("Enter the name of the creature you want to search for:", "Search")  # Allows user to search for the ceature using a enterbox gui
    if creature_name is None:
        return
    if creature_name in creatures:
        creature_stats = creatures[creature_name]
        easygui.msgbox("Creature Found!")
    else:
        easygui.msgbox("Creature not found.")
        pass

# Testing
search_creature()
