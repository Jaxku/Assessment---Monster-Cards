"""""
03_searchMenuFunction_v4
Verison that can be used in base function with search feature enabled.
"""

import easygui

creatures = {  # Dictionary of creatures
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


def search_creature():
    creature_name = easygui.enterbox("Enter the name of the creature you want to search for:", "Search")

    if creature_name is None:
        return

    # capitalize the first letter of the creature_name input
    creature_name = creature_name.capitalize()

    # check if the creature_name exists in the creatures dictionary
    if creature_name in creatures:
        creature_stats = creatures[creature_name]

        message = f"Creature: {creature_name}\nStrength: {creature_stats['Strength']}\nSpeed: {creature_stats['Speed']}\nStealth: {creature_stats['Stealth']}\nCunning: {creature_stats['Cunning']}"

        while True:
            choice = easygui.buttonbox(f"{message}\n\nWhat would you like to do?", "Creature Details", choices=["OK", "Edit Stats"])

            if choice == "Return to Main Menu":
                display_menu()  # Return to main menu

            elif choice == "Edit Stats":
                field = easygui.buttonbox("Which stat would you like to edit?", "Edit Stat", choices=["Strength", "Speed", "Stealth", "Cunning"])
                new_value = easygui.integerbox(f"Enter the new value for {field}:", "Edit Stat", lowerbound=1, upperbound=25)
                creature_stats[field] = new_value
                message = f"Creature: {creature_name}\nStrength: {creature_stats['Strength']}\nSpeed: {creature_stats['Speed']}\nStealth: {creature_stats['Stealth']}\nCunning: {creature_stats['Cunning']}"
                easygui.msgbox("Stat updated successfully!")

        display_menu()

    else:
        easygui.msgbox("Creature not found.")



# Testing
search_creature()
