
# Todo:
# Port scenarios - 25%
# Add a save feature using configparser

# Imports
import os   # Use to make directories automatically and clear screen
import random   # Get random lessons and stats
import configparser     # Scenarios and saving

# Get config
Config = configparser.ConfigParser()
Config.read("Ruben-Sim/config.ini")

Directory = Config.get("Main", "Directory")
Linux = Config.get("Main", "Linux")

# Set Variables
Trouble = 0.0
Focus = 0.0
Happiness = 0.0
Money = 0.0
Energy = 0.0
Period = 1
Day = "Mon"
Lesson = "Co"

# Generate the scenario based on time, last lesson, day, etc.
def GetScenario():

    # Set globals
    global ScenarioName
    global Period
    global Energy
    global Trouble
    global Period
    global Day
    global Lesson

    # Get config
    ScenarioConfig = configparser.ConfigParser()
    ScenarioConfig.read(Directory + "Scenarios/Info.ini")

    # Get random lesson
    NumberOfLessons = random.randint(1, int(ScenarioConfig.get("Main", "NumberOfScenarios")))
    
    # Break
    if Period == "B":
        ScenarioName = "B"
    # Lunch
    elif Period == "L":
        ScenarioName = "L"
    # Computing
    elif NumberOfLessons == 1:
        ScenarioName = "Co"
    # DT
    elif NumberOfLessons == 2:
        ScenarioName = "Dt"
    # English
    elif NumberOfLessons == 3:
        ScenarioName = "En"
    # Spanish
    elif NumberOfLessons == 4:
        ScenarioName = "Sp"
    # History
    elif NumberOfLessons == 5:
        ScenarioName = "Hi"
    # Science
    else:
        ScenarioName = "Sc"

    # Main Part
    Number = random.randint(1, int(ScenarioConfig.get(ScenarioName, "NumberOfScenarios")))
    Lesson = ScenarioName
    # Add prefix
    ScenarioName = ScenarioName + "-" + str(Number)
            
# Load the senario
def MainScenario():

    # Set gloabls
    global Directory
    global ScenarioName
    global StatChanges
    global FollowOnScenario
    global AfterMessage
    global Lesson

    # Print the firt bit of ui
    Clear()
    PrintStats()

    # Load the scenario from the corresponding ini file in 'Directory' using configparser
    Scenario = configparser.ConfigParser()
    Scenario.read(Directory + "Scenarios/" + Lesson + "/" + ScenarioName + ".ini")

    # Print question from file
    print("| [-] | QUESTION:")
    print("| [?] | " + Scenario.get("Main", "Question"))

    # Get the number of options to print the correct amount
    NumberOfOptions = int(Scenario.get("Main", "NumberOfOptions"))

    # Option Print
    for x in range(NumberOfOptions):
         print("| ["+str(x + 1)+"] | - " + Scenario.get("Main", "Option" + str(x)))

    # Take option
    Option = str(input("| [!] | >>>"))

    # Get temp store of option
    TempStoreOfOption = "Option"
    TempStoreOfOption = TempStoreOfOption + Option # This should result in something like 'Option3' 

    # Test for random
    Random = Scenario.get(TempStoreOfOption, "Random")

    # Do random if enabled
    if Random in ["True", "true", "t", "T"]:

        # Gen random no. between 1 and 10 and get RandomNumber var
        GenericRandom = random.randint(1, 10)
        RandomNumber = Scenario.get(TempStoreOfOption, "RandomNumber")
        RandomNumber = int(RandomNumber)

        # Compare
        # a in this instance refers to the number put before the fectched vars ETC. [a]StatChanges could mean 1StatChanges
        if GenericRandom > RandomNumber:
            a = "1"
        else:
            a = "2"
        
        # Proceed with setting variables as normal but with the 'a' var
        StatChangesTemp = Scenario.get(TempStoreOfOption, a+"StatChanges")    # This needs formatting
        StatChanges = StatChangesTemp.split()  # Formatted into a list
        FollowOnScenario = Scenario.get(TempStoreOfOption, a+"FollowOnScenario")
        AfterMessage = Scenario.get(TempStoreOfOption, a+"AfterMessage")
        
    # Continue as normal
    else:
        # Set variables based on option
        StatChangesTemp = Scenario.get(TempStoreOfOption, "StatChanges")    # This needs formatting
        StatChanges = StatChangesTemp.split()  # Formatted into a list
        FollowOnScenario = Scenario.get(TempStoreOfOption, "FollowOnScenario")
        AfterMessage = Scenario.get(TempStoreOfOption, "AfterMessage")

    # After Message
    AfterMessagePrint()

    # Apply changes
    ApplyScenarioStatChanges()

# Load nessesary vars for changing vars or selecting the next scenario after a option is selected
def ApplyScenarioStatChanges():

    # Get globals ofc
    global ScenarioName
    global StatChanges
    global FollowOnScenario
    global Trouble
    global Focus
    global Happiness
    global Money
    global Energy

    # Float
    Trouble = float(Trouble)
    Focus = float(Focus)
    Happiness = float(Happiness)
    Money = float(Money)
    Energy = float(Energy)

    # Applying var changes from var: 'stat changes'
    Temp = float(StatChanges[0])
    Trouble = Trouble + Temp
    Temp = float(StatChanges[1])
    Focus = Focus + Temp
    Temp = float(StatChanges[2])
    Happiness = Happiness + Temp
    Temp = float(StatChanges[3])
    Money = Money + Temp
    Temp = float(StatChanges[4])
    Energy = Energy + Temp

    # Round the numbers
    Trouble = round(Trouble, 1)
    Focus = round(Focus, 1)
    Happiness = round(Happiness, 1)
    Money = round(Money, 1)
    Energy = round(Energy, 1)
    # Correct if higher
    if Trouble > 10:
        Trouble = 10
    if Focus > 10:
        Focus = 10
    if Happiness > 10:
        Happiness = 10
    if Money > 10:
        Money = 10
    if Energy > 10:
        Energy = 10
    # Correct if lower
    if Trouble < -10:
        Trouble = -10
    if Focus < -10:
        Focus = -10
    if Happiness < -10:
        Happiness = -10
    if Money < -10:
        Money = -10
    if Energy < -10:
        Energy = -10

    # Load follow on scenario if there is one
    if FollowOnScenario.lower() != "none":

        # Set new scenario to use
        ScenarioName = FollowOnScenario

        # Rerun mainscenario
        MainScenario()

# Handle moving on time, Period, day and autosave 
def TimeLogic(): 

    # Globals again
    global Day
    global Period

    # End of day
    if str(Period) == "6": 
        
        # Move on day
        if Day in ["Mon"]:
            Day =  "Tue"
        elif Day in ["Tue"]:
            Day =  "Wed"
        elif Day in ["Wed"]:
            Day =  "Thu"
        elif Day in ["Thu"]:
            Day =  "Fri"
        elif Day in ["Fri"]:
            Day =  "Mon"
        
        # Reset period 
        Period = 1

        # Save game
        WriteSave()
    
    # Not end of day
    else:

        # EXPLANATION: 
        # Period Var Can be: 1, 2, B, 3, 4, L, 5, 6
        # 'B' and 'L' mean break and lunch

        # Norm
        if Period == 1:
            Period = 2
        # Break
        elif Period == 2:
            Period = "B"
        # Break to norm
        elif Period == "B":
            Period = 3
        # Norm
        elif Period == 3:
            Period = 4
        # Lunch
        elif Period == 4:
            Period = "L"
        # Lunch to norm
        elif Period == "L":
            Period = 5   
        # Norm
        elif Period == 5:
            Period = 6     

# Print stats
def PrintStats():

    # Globals go brr
    global Trouble
    global Focus
    global Happiness
    global Money
    global Energy
    
    # USE BARS FOR ALL STATS
    # STATS GO FROM -10 to 10
    # Example of 4 focus
    # | 4 | ----------|====------
    #
    # Example of - + " - " + DisplayName4 focus
    # |-4 | ------====|---------- 
    #
    # On the left number display - notice how the space dissapears to make room for the minus
    # Print stats
    print("| [-] | STATS:")

    # Loop start
    for x in range(5):

        # Define TempPlaceholder
        if x == 0:
            TempPlaceholder = Trouble
            DisplayName = "Trouble"
        elif x == 1:
            TempPlaceholder = Focus
            DisplayName = "Focus"
        elif x == 2:
            TempPlaceholder = Happiness
            DisplayName = "Happiness"
        elif x == 3:
            TempPlaceholder = Money
            DisplayName = "Money"
        else: 
            TempPlaceholder = Energy
            DisplayName = "Energy"

        # IMPORTANT: Decided not to do an algorithm here as it would be too much work
        if TempPlaceholder < -10:
            print("huh that value does not seem to be inside the normal range of -10 to 10")
        elif TempPlaceholder == -10:
            print("|" + str(TempPlaceholder) + " | ==========|----------" + " - " + DisplayName)
        elif TempPlaceholder <= -9:
            print("|" + str(TempPlaceholder) + " | -=========|----------" + " - " + DisplayName)
        elif TempPlaceholder <= -8:
            print("|" + str(TempPlaceholder) + " | --========|----------" + " - " + DisplayName)
        elif TempPlaceholder <= -7:
            print("|" + str(TempPlaceholder) + " | ---=======|----------" + " - " + DisplayName)
        elif TempPlaceholder <= -6:
            print("|" + str(TempPlaceholder) + " | ----======|----------" + " - " + DisplayName)
        elif TempPlaceholder <= -5:
            print("|" + str(TempPlaceholder) + " | -----=====|----------" + " - " + DisplayName)
        elif TempPlaceholder <= -4:
            print("|" + str(TempPlaceholder) + " | ------====|----------" + " - " + DisplayName)
        elif TempPlaceholder <= -3:
            print("|" + str(TempPlaceholder) + " | -------===|----------" + " - " + DisplayName)
        elif TempPlaceholder <= -2:
            print("|" + str(TempPlaceholder) + " | --------==|----------" + " - " + DisplayName)
        elif TempPlaceholder <= -1:
            print("|" + str(TempPlaceholder) + " | ---------=|----------" + " - " + DisplayName)
        elif TempPlaceholder < 0:
            print("|" + str(TempPlaceholder) + " | ---------=|----------" + " - " + DisplayName)
        elif TempPlaceholder == 0:
            print("|", TempPlaceholder, "| ----------|----------" + " - " + DisplayName)
        elif TempPlaceholder <= 1:
            print("|", TempPlaceholder, "| ----------|=---------" + " - " + DisplayName)
        elif TempPlaceholder <= 2:
            print("|", TempPlaceholder, "| ----------|==--------" + " - " + DisplayName)
        elif TempPlaceholder <= 3:
            print("|", TempPlaceholder, "| ----------|===-------" + " - " + DisplayName)
        elif TempPlaceholder <= 4:
            print("|", TempPlaceholder, "| ----------|====------" + " - " + DisplayName)
        elif TempPlaceholder <= 5:
            print("|", TempPlaceholder, "| ----------|=====-----" + " - " + DisplayName)
        elif TempPlaceholder <= 6:
            print("|", TempPlaceholder, "| ----------|======----" + " - " + DisplayName)
        elif TempPlaceholder <= 7:
            print("|", TempPlaceholder, "| ----------|=======---" + " - " + DisplayName)
        elif TempPlaceholder <= 8:
            print("|", TempPlaceholder, "| ----------|========--" + " - " + DisplayName)
        elif TempPlaceholder <= 9:
            print("|", TempPlaceholder, "| ----------|=========-" + " - " + DisplayName)
        elif TempPlaceholder <= 10:
            print("|", TempPlaceholder, "| ----------|==========" + " - " + DisplayName)
        else:
            print("huh that value does not seem to be inside the normal range of -10 to 10")

# Clear the screen
def Clear():
    # Globals
    global Linux
    # Clear
    if Linux:
        os.system("clear")
    else:
        os.system("cls")

# After messgae
def AfterMessagePrint():

    # Does this need explaining tho?
    global AfterMessage
    if AfterMessage != "none":
        Clear()
        print("| [-] | - " + AfterMessage)
        input("| [!] | >>>")

def DebugInput():
    
    # DEBUG
    input("Debug Input!")

# Save
def WriteSave():

    # Globals
    global Directory
    global Trouble
    global Focus
    global Happiness
    global Money
    global Energy
    global Period
    global Day
    global Lesson

    # Open save in configparser
    Save = configparser.ConfigParser()
    Save.read(Directory + "Saves/Save.ini")

    # Write vars using configparser 
    Save.set("Time", "period", str(Period))
    Save.set("Time", "day", str(Day))
    Save.set("Stats", "trouble", str(Trouble))
    Save.set("Stats", "focus", str(Focus))
    Save.set("Stats", "happiness", str(Happiness))
    Save.set("Stats", "money", str(Money))
    Save.set("Stats", "energy", str(Energy))

    # Save to file
    with open(Directory + "Saves/Save.ini", "w") as File:
        Save.write(File)

def LoadSave():

    # Globals
    global Directory
    global Trouble
    global Focus
    global Happiness
    global Money
    global Energy
    global Period
    global Day
    global Lesson

    # Open save in configparser
    Save = configparser.ConfigParser()
    Save.read(Directory + "Saves/Save.ini")

    # Read vars using configparser 
    Period = Save["Time"]["period"]
    Day = Save["Time"]["day"]
    Trouble = float(Save.get("Stats", "trouble"))
    Focus = float(Save.get("Stats","focus"))
    Happiness = float(Save.get("Stats","happiness"))
    Money = float(Save.get("Stats","money"))
    Energy = float(Save.get("Stats","energy"))

# Launch / Pre loop
print("| [?] | SAVE MENU\n| [1] | - Load\n| [2] | - New")
Option = str(input("| [?] | >>>"))
if Option == "1":
    LoadSave()
else:
    WriteSave()

# Game Loop
while True:

    GetScenario()
    MainScenario()
    TimeLogic()
