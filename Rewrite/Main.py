
# TODO:
    # Complete the PrintStats() function
    # Complete the TimeLogic() function
    # Complete the GetScenario() function
    # Add screen clear in a windows AND linux mode
    # Port scenarios
    # Write documentsation

# CHANGE THESE
Directory = "Documents/RubenSim/"


# Imports
import os   # Use to make directories automatically and clear screen
import pickle   # Use for saving stats later prob

# Set Variables
Trouble = 0
Focus = 0
Happiness = 0
Money = 0
Energy = 0

Period = 1
Day = "Monday"


# Define Main Functions

# Generate the scenario based on time, last lesson, day, etc.
def GetScenario():

    # Set globals
    global ScenarioName

    # Set scenario name
    ScenarioName = "Co-1"

# Load the senario
def MainScenario():

    # Set gloabls
    global Directory
    global ScenarioName
    global StatChanges
    global FollowOnScenario

    # Load it

    # Co-1
    if ScenarioName in ["Co-1"]:
        # Question
        print("Test Question")
        # Options
        print("Test Opt 1")
        print("Test Opt 2")
        print("Test Opt 3")
        Option = str(input(">>>"))

        # Change vars for applying
        if Option.lower() in ["1"]:
            # [Trouble, Focus, Happiness, Money, Energy] 
            StatChanges = [1, 2, 3, -4, 2]
            FollowOnScenario = "null"

        elif Option.lower() in ["2"]:
            # [Trouble, Focus, Happiness, Money, Energy] 
            StatChanges = [1, 2, 3, -4, 2]
            FollowOnScenario = "null"

        elif Option.lower() in ["3"]:
            # [Trouble, Focus, Happiness, Money, Energy] 
            StatChanges = [1, 2, 3, -4, 2]
            FollowOnScenario = "null"

    # Apply changes
    ApplyScenarioStatChanges()

# Load nessesary vars for changing vars or selecting the next scenario
# After a option is selected
def ApplyScenarioStatChanges():

    # Get globals ofc
    global StatChanges
    global FollowOnScenario
    global Trouble
    global Focus
    global Happiness
    global Money
    global Energy

    # Applying var changes from var: 'stat changes'
    Trouble = Trouble + StatChanges[0]
    Focus = Focus + StatChanges[1]
    Happiness = Happiness + StatChanges[2]
    Money = Money + StatChanges[3]
    Energy = Energy + StatChanges[4]

    # Load follow on scenario if there is one
    if FollowOnScenario.lower() != "null":

        # Set new scenario to use
        ScenarioName = FollowOnScenario

        # Rerun mainscenario
        MainScenario()

# Handle moving on time, Period and day
def TimeLogic():
    print("do this l a t e r .")

# Print stats
def PrintStats():
    
    # USE BARS FOR ALL STATS
    # STATS GO FROM -10 to 10
    # Example of 4 focus
    # | 4 | ----------|====------
    #
    # Example of -4 focus
    # |-4 | ------====|---------- 
    #
    # On the left number display - notice how the space dissapears to make room for the minus

    print("STATS:")

# Game Loop
# Look above for explaination
while True:
    GetScenario()
    MainScenario()
