"""""
00_baseMonsterCard_v1.py
V2 using updated versions of functions
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
def display_menu():
    list_of_food = []
    for key in creatures.keys():
        list_of_food.append(key)
    option = easygui.buttonbox("What would you like to do?", choices=["Search", "Add", "Delete", "Menu"])  # launches GUI menu
    if option == "Search":
        search_creature()
    elif option == "Add":
        add_creature()  # Place holder
    elif option == "Delete":
        delete_creature(easygui.enterbox(msg="Enter the name of the creature to delete:", title="Delete Creature", default=""))  # Place holder
    else:
        raise Exception("Invalid option selected")
    return


# Function to search for a creature
def search_creature():
    creature_name = easygui.enterbox("Enter the name of the creature you want to search for:", "Search")

    if creature_name is None:
        return

    # capitalize the first letter of the creature_name input
    creature_name = creature_name.capitalize()

    # check if the creature_name exists in the creatures dictionary
    if creature_name in list(creatures.keys()):
        creature_stats = creatures[creature_name]

        message = f"Creature: {creature_name}\nStrength: {creature_stats['Strength']}\nSpeed: {creature_stats['Speed']}\nStealth: {creature_stats['Stealth']}\nCunning: {creature_stats['Cunning']}"

        while True:
            choice = easygui.buttonbox(f"{message}\n\nWhat would you like to do?", "Creature Details", choices=["Return to Main Menu", "Edit Stats"])

            if choice == "Return to Main Menu":
                display_menu()  # Return to main menu

            elif choice == "Edit Stats":
                field = easygui.buttonbox("Which stat would you like to edit?", "Edit Stat", choices=["Strength", "Speed", "Stealth", "Cunning"])
                new_value = easygui.integerbox(f"Enter the new value for {field}:", "Edit Stat", lowerbound=1, upperbound=25)
                creature_stats[field] = new_value
                message = f"Creature: {creature_name}\nStrength: {creature_stats['Strength']}\nSpeed: {creature_stats['Speed']}\nStealth: {creature_stats['Stealth']}\nCunning: {creature_stats['Cunning']}"
                easygui.msgbox("Stat updated successfully!")
            else:
                easygui.msgbox("Creature not found.")

    return


# Function to add a creature
def add_creature():
    creature_name = easygui.enterbox("Enter the name of the creature you want to add:", "Add")
    if creature_name is None:
        return
    creature_stats = {}

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


# Function to delete a creature
def delete_creature(creature_list):
    while True:
        if creatures is None:
            display_menu()  # user clicked cancel

        if creatures.lower() in [name.lower() for name in creatures]:
            del creatures[creatures.capitalize()]
            easygui.msgbox(f"{creatures} has been deleted from the creature list.", title="Delete Creature")
            return creatures  # return the updated list
            pass
        else:
            msg = f"{creatures} was not found in the creature list. Would you like to try again?"
            response = easygui.buttonbox(msg, title="Delete Creature", choices=["Try Again", "Cancel"])
            # returns the text of the button clicked
            if response == "Cancel":
                return None
        display_menu()  # Return to main menurr


display_menu()  # Displays menu
