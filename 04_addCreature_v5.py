"""""
04_addCreature_v5.py
Making the language used in the messageboxes more general and cool.
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


def add_creature():
    creature_name = easygui.enterbox("Enter the name of the creature you want to add:", "Add")
    if creature_name is None:
        return
    creature_stats = dict()
    creature_stats["Strength"] = {}
    creature_stats["Speed"] = {}
    creature_stats["Stealth"] = {}
    creature_stats["Cunning"] = {}

    creature_stats["Strength"] = easygui.integerbox("Enter the strength of the creature:", "Add", lowerbound=1, upperbound=25)
    creature_stats["Speed"] = easygui.integerbox("Enter the speed of the creature:", "Add", lowerbound=1, upperbound=25)
    creature_stats["Stealth"] = easygui.integerbox("Enter the stealth of the creature:", "Add", lowerbound=1, upperbound=25)
    creature_stats["Cunning"] = easygui.integerbox("Enter the cunning of the creature:", "Add", lowerbound=1, upperbound=25)

    creatures[creature_name] = creature_stats

    # Display the newly added creature
    message = f"The following creature has been added:\n\nName: {creature_name}\nStrength: {creature_stats['Strength']}\nSpeed: {creature_stats['Speed']}\nStealth: {creature_stats['Stealth']}\nCunning: {creature_stats['Cunning']}"
    while True:
        choice = easygui.ynbox(f"{message}\n\nAre these details correct?", "Confirm Details")
        if choice:
            easygui.msgbox("Creature added successfully!")
            display_menu()  # Go back to the main menu
        else:
            field = easygui.buttonbox("Which field would you like to change?", "Edit Field", choices=["Strength", "Speed", "Stealth", "Cunning"])
            new_value = easygui.integerbox(f"Enter the new value for {field}:", "Edit Field", lowerbound=1, upperbound=25)
            creature_stats[field] = new_value
            message = f"The following creature has been added:\n\nName: {creature_name}\nStrength: {creature_stats['Strength']}\nSpeed: {creature_stats['Speed']}\nStealth: {creature_stats['Stealth']}\nCunning: {creature_stats['Cunning']}"
    return

add_creature()
