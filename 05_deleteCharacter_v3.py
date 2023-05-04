"""""
05_deleteCharacter_v3.py
This verison adds a cancel button so if the user accidentally presses the delete button they can cancel the action.
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


def delete_creature(creature_list):
    while True:
        creature = easygui.enterbox(msg="Enter the name of the creature to delete:", title="Delete Creature", default="")
        if creature is None:
            return None  # user clicked cancel

        if creature.lower() in [name.lower() for name in creature_list]:
            creature_list.remove([name for name in creature_list if name.lower() == creature.lower()][0])  # remove the first instance of the creature
            easygui.msgbox(f"{creature} has been deleted from the creature list.", title="Delete Creature")
            return creature_list  # return the updated list
        else:
            msg = f"{creature} was not found in the creature list. Would you like to try again?"
            response = easygui.buttonbox(msg, title="Delete Creature", choices=["Try Again", "Cancel"])  # returns the text of the button clicked
            if response == "Cancel":
                return None
