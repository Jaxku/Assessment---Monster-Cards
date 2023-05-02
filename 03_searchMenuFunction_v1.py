"""""
03_searchMenuFunction_v1
This function allows the menu function (02) to search the creatyres from the creature dictionary.
"""
import easygui

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
