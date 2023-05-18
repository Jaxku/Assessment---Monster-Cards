"""""
00_baseMonsterCard_v3.py
v3
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

# Dictionary to store the details of monster cards added during the current session
session_creatures = {}


# Function to display the menu
def display_menu():
    option = easygui.buttonbox("What would you like to do?", "Main Menu", choices=["Search", "Add", "Delete", "Menu"])

    if option == "Search":
        search_creature()
    elif option == "Add":
        add_creature()
    elif option == "Delete":
        delete_creature()
    else:
        raise Exception("Invalid option selected")


# Function to search for a creature
def search_creature():
    while True:
        creature_name = easygui.enterbox("Enter the name of the creature you want to search for:", "Search")

        if creature_name is None:
            display_menu()
            return

        creature_name = creature_name.capitalize()

        if creature_name in creatures or creature_name in session_creatures:
            creature_stats = creatures.get(creature_name) or session_creatures.get(creature_name)

            message = f"Creature: {creature_name}\n" \
                      f"Strength: {creature_stats['Strength']}\n" \
                      f"Speed: {creature_stats['Speed']}\n" \
                      f"Stealth: {creature_stats['Stealth']}\n" \
                      f"Cunning: {creature_stats['Cunning']}"

            while True:
                choice = easygui.buttonbox(
                    f"{message}\n\nWhat would you like to do?",
                    "Creature Details",
                    choices=["OK", "Edit Stats", "Return to Main Menu"]
                )

                if choice == "Return to Main Menu":
                    display_menu()
                    return

                elif choice == "Edit Stats":
                    field = easygui.buttonbox(
                        "Which stat would you like to edit?",
                        "Edit Stat",
                        choices=["Strength", "Speed", "Stealth", "Cunning"]
                    )
                    new_value = easygui.integerbox(
                        f"Enter the new value for {field}:",
                        "Edit Stat",
                        lowerbound=1,
                        upperbound=25
                    )
                    creature_stats[field] = new_value
                    message = f"Creature: {creature_name}\n" \
                              f"Strength: {creature_stats['Strength']}\n" \
                              f"Speed: {creature_stats['Speed']}\n" \
                              f"Stealth: {creature_stats['Stealth']}\n" \
                              f"Cunning: {creature_stats['Cunning']}"
                    easygui.msgbox("Stat updated successfully!")
                elif choice == "OK":
                    break
        else:
            easygui.msgbox("Creature not found.")


# Function to add a creature
def add_creature():
    while True:
        creature_name = easygui.enterbox("Enter the name of the creature you want to add:", "Add Creature")
        if creature_name is None:
            display_menu()
            return

        creature_name = creature_name.capitalize()

        if creature_name in creatures or creature_name in session_creatures:
            easygui.msgbox("Creature already exists.")
            continue

        creature_stats = {
            "Strength": easygui.integerbox("Enter the strength of the creature:", "Add", lowerbound=1, upperbound=25),
            "Speed": easygui.integerbox("Enter the speed of the creature:", "Add", lowerbound=1, upperbound=25),
            "Stealth": easygui.integerbox("Enter the stealth of the creature:", "Add", lowerbound=1, upperbound=25),
            "Cunning": easygui.integerbox("Enter the cunning of the creature:", "Add", lowerbound=1, upperbound=25)
        }

        session_creatures[creature_name] = creature_stats

        message = f"The following creature has been added:\n" \
                  f"\nName: {creature_name}" \
                  f"\nStrength: {creature_stats['Strength']}" \
                  f"\nSpeed: {creature_stats['Speed']}" \
                  f"\nStealth: {creature_stats['Stealth']}" \
                  f"\nCunning: {creature_stats['Cunning']}"

        while True:
            choice = easygui.ynbox(f"{message}\n\nAre these details correct?", "Confirm Details")
            if choice:
                easygui.msgbox("Creature added successfully!")
                display_menu()
                return
            else:
                field = easygui.buttonbox(
                    "Which field would you like to change?",
                    "Edit Field",
                    choices=["Strength", "Speed", "Stealth", "Cunning"]
                )
                new_value = easygui.integerbox(
                    f"Enter the new value for {field}:",
                    "Edit Field",
                    lowerbound=1,
                    upperbound=25
                )
                creature_stats[field] = new_value
                message = f"The following creature has been added:\n" \
                          f"\nName: {creature_name}" \
                          f"\nStrength: {creature_stats['Strength']}" \
                          f"\nSpeed: {creature_stats['Speed']}" \
                          f"\nStealth: {creature_stats['Stealth']}" \
                          f"\nCunning: {creature_stats['Cunning']}"
                easygui.msgbox("Creature added successfully!")
                display_menu()


# Function to delete a creature
def delete_creature():
    while True:
        creature_name = easygui.enterbox("Enter the name of the creature you want to delete:", "Delete Creature")

        if creature_name is None:
            display_menu()
            return

        creature_name = creature_name.capitalize()

        if creature_name in creatures:
            del creatures[creature_name]
            easygui.msgbox(f"{creature_name} has been deleted from the creature list.")
        elif creature_name in session_creatures:
            del session_creatures[creature_name]
            easygui.msgbox(f"{creature_name} has been deleted from the current session.")
        else:
            easygui.msgbox("Creature not found.")

        display_menu()


display_menu()
