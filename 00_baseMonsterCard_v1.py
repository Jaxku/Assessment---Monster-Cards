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
def display_menu():
    list_of_food = []
    for key in creatures.keys():
        list_of_food.append(key)
    option = easygui.buttonbox("What would you like to do?", choices=["Search", "Add", "Delete", "Menu"])  # launches GUI menu
    if option == "Search":
        search_creature()  # Launches the search function
    elif option == "Add":
        add_creature()  # Launches the add function
    elif option == "Delete":
        delete_creature(creatures)  # Launches the delete function
    else:
        raise Exception("Invalid option selected")
    return


# Function to search for a creature
def search_creature():
    creature_name = easygui.enterbox("Enter the name of the creature you want to search for:", "Search")
    # Allows user to search for the creature using an enter-box gui
    if creature_name is None:
        return
    if creature_name in creatures:
        creature_stats = creatures[creature_name]
        easygui.msgbox("Creature: {}\nStrength: {}\nSpeed: {}\nStealth: {}\nCunning: {}".format(creature_name, creature_stats["Strength"], creature_stats["Speed"], creature_stats["Stealth"], creature_stats["Cunning"]))
        display_menu()  # Returns to main menu
    else:
        easygui.msgbox("Creature not found.")
        display_menu()  # Returns to main menu


# Function to add a creature
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
            break
        else:
            field = easygui.buttonbox("Which field would you like to change?", "Edit Field", choices=["Strength", "Speed", "Stealth", "Cunning"])
            new_value = easygui.integerbox(f"Enter the new value for {field}:", "Edit Field", lowerbound=1, upperbound=25)
            creature_stats[field] = new_value
            message = f"The following creature has been added:\n\nName: {creature_name}\nStrength: {creature_stats['Strength']}\nSpeed: {creature_stats['Speed']}\nStealth: {creature_stats['Stealth']}\nCunning: {creature_stats['Cunning']}"
    display_menu()  # Returns to main menu


def delete_creature(creature_list):  # function to delete a creature from the list
    while True:
        creature = easygui.enterbox(msg="Enter the name of the creature to delete:", title="Delete Creature", default="")
        if creature is None:
            return None  # user clicked cancel

        if creature.lower() in [name.lower() for name in creature_list]:
            creature_list.remove([name for name in creature_list if name.lower() == creature.lower()][0])  # remove the first instance of the creature from the list
            easygui.msgbox(f"{creature} has been deleted from the creature list.", title="Delete Creature")
            return creature_list  # return the updated list
        else:
            msg = f"{creature} was not found in the creature list. Would you like to try again?"
            response = easygui.buttonbox(msg, title="Delete Creature", choices=["Try Again", "Cancel"])  # returns the text of the button clicked
            if response == "Cancel":
                return None  # user clicked cancel  #


display_menu()  # Displays menu
