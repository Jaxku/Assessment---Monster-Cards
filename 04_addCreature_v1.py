



# Function to add a creature
def add_creature():
    creature_name = easygui.enterbox("Enter the name of the creature you want to add:", "Add")
    if creature_name is None:
        return
    creature_stats = {}
    creature_stats["Strength"] = easygui.integerbox("Enter the strength of the creature:", "Add", lowerbound=1, upperbound=100)
    creature_stats["Speed"] = easygui.integerbox("Enter the speed of the creature:", "Add", lowerbound=1, upperbound=100)
    creature_stats["Stealth"] = easygui.integerbox("Enter the stealth of the creature:", "Add", lowerbound=1
