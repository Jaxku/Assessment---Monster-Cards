"""""
06_printConsole_v1.py
First version of the print console function. My take on the function as the project brief is a bit vague.
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

session_creatures = {}


def print_menu():
    easygui.msgbox("Press 'ok' to print the list of creatures to console.", "Print Creatures")
    menu = "Menu:"
    # Print creatures from the dictionary
    for creature, stats in creatures.items():
        menu += f"{creature}: Strength={stats['Strength']}, " \
                f"Speed={stats['Speed']}, " \
                f"Stealth={stats['Stealth']}, " \
                f"Cunning={stats['Cunning']}\n"

    # Print creatures from the session
    menu += "Temporary Creatures:\n"
    for creature, stats in session_creatures.items():
        menu += f"{creature}: Strength={stats['Strength']}, " \
                f"Speed={stats['Speed']}, " \
                f"Stealth={stats['Stealth']}, " \
                f"Cunning={stats['Cunning']}\n"

    print(menu)


print_menu()
