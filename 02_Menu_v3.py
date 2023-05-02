"""""
02_menu_v3.py
This version of the menu function will fix any problems before adding it to the base code
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
        easygui.msgbox("Search Option Pressed")  # Place holder
    elif option == "Add":
        easygui.msgbox("Add Option Pressed")  # Place holder
    elif option == "Delete":
        easygui.msgbox("Delete Option Pressed")  # Place holder
    else:
        raise Exception("Invalid option selected")
    return


# Running the menu code to see if it works
display_menu()
