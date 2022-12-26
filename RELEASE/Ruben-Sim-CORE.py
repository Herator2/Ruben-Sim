
import random
from colorama import Fore, Style
import time

# ============================
VERSION = "V 1.1-BETA"
# ============================

x = 0
y = 0
SCREEN_WIDTH = 80   # Default
SCREEN_HEIGHT = 24     # Default
Spacer = "=" * SCREEN_WIDTH   # Default
Loop = True
while Loop:

    if True:
        # Defining Stuff JUST IN CASE OKAY?!
        if True:
            Menuloop = True     # Menu Loop
            Mainloop = False    # GameLoop
            # noinspection PyRedeclaration
            Time = 1    # Period 1
            Period = "PERIOD 1"  # Store the Period
            Day = "MONDAY"  # Store the Day
            Lesson = "Co"   # Backup lesson incase lesson gen fails
            DisplayLesson = "COMPUTING"
            IPad = True     # Have an IPad?
            Multiplier = 0.9    # Normal
            Detention = False   # Is there Detention Rn?
            Isolation = False   # Is there Isolation rn?
            DetentionLesson = "Co"  # The lesson you got detention in
            C1 = 0  # Consequence 1
            C2 = 0  # Consequence 2
            C3 = 0  # Consequence 3
            C4 = 0  # Consequence 4
            Lessonloop = True   # Make
            CoLessonCounter = 0     # How many of this lesson today?
            DtLessonCounter = 0     # How many of this lesson today?
            EnLessonCounter = 0     # How many of this lesson today?
            SpLessonCounter = 0     # How many of this lesson today?
            HiLessonCounter = 0     # How many of this lesson today?
            ScLessonCounter = 0     # How many of this lesson today?
            LastLesson = "None"     # Lesson Used For Doubles In P2, P4 and P6 (SET IN P1, P3 and P5)
            OldPopularity = 0   # For end of day screen and some calculations
            OldFocus = 0   # For end of day screen and some calculations
            OldHappiness = 0   # For end of day screen and some calculations
            OldEnergy = 0   # For end of day screen and some calculations
            OldBattery = 0   # For end of day screen and some calculations
            Dead = False    # SELF EXPLANATORY
            Dev = False     # Developer mode
            WasThereAIsolationToday = False     # Are you an idiot   READ THE NAME


        def render():
            print(Spacer)
            print(Fore.LIGHTMAGENTA_EX + "STATS:")

            # Popularity Colour
            if Popularity < 3:
                print(Style.BRIGHT + Fore.LIGHTRED_EX + "|" + str(Popularity) + " - Popularity")
            elif Popularity > 7:
                print(Fore.LIGHTGREEN_EX + "|" + str(Popularity) + " - Popularity")
            else:
                print(Fore.LIGHTCYAN_EX + "|" + str(Popularity) + " - Popularity")

            # Focus Colour
            if Focus < 3:
                print(Fore.LIGHTRED_EX + "|" + str(Focus) + " - Focus")
            elif Focus > 7:
                print(Fore.LIGHTGREEN_EX + "|" + str(Focus) + " - Focus")
            else:
                print(Fore.LIGHTCYAN_EX + "|" + str(Focus) + " - Focus")

            # Happiness Colour
            if Happiness < 3:
                print(Fore.LIGHTRED_EX + "|" + str(Happiness) + " - Happiness")
            elif Happiness > 7:
                print(Fore.LIGHTGREEN_EX + "|" + str(Happiness) + " - Happiness")
            else:
                print(Fore.LIGHTCYAN_EX + "|" + str(Happiness) + " - Happiness")

            # Energy Colour
            if Energy < 3:
                print(Fore.LIGHTRED_EX + "|" + str(Energy) + " - Energy")
            elif Energy > 7:
                print(Fore.LIGHTGREEN_EX + "|" + str(Energy) + " - Energy")
            else:
                print(Fore.LIGHTCYAN_EX + "|" + str(Energy) + " - Energy")

            # Separator
            print(Fore.WHITE + Spacer)

            # Ipad Colour
            if IPad:
                print(Fore.LIGHTGREEN_EX + "|IPad - True")
            elif not IPad:
                print(Fore.LIGHTRED_EX + "|IPad - False")
            else:
                print(Fore.LIGHTRED_EX + "ERROR - IPAD NOT TRUE OR FALSE")

            if IPad:
                # Battery Colour
                if Battery < 25:
                    print(Fore.LIGHTRED_EX + "|" + str(round(Battery, 1)) + "% - Battery")
                elif Battery > 75:
                    print(Fore.LIGHTGREEN_EX + "|" + str(round(Battery, 1)) + "% - Battery")
                else:
                    print(Fore.LIGHTCYAN_EX + "|" + str(round(Battery, 1)) + "% - Battery")

            # Separator
            print(Fore.WHITE + Spacer)
            print(" ")


        # End Of Setup

    # MenuLoop / Launcher
    while Menuloop:
        # Welcome
        for x in range(1, SCREEN_HEIGHT):
            print(" ")
        print(Style.BRIGHT + Fore.WHITE + Spacer)
        print(" ")
        print("Welcome to the Ruben Simulator")
        if Dev:
            print("RELEASE -", VERSION, " - DEVELOPER MODE / NOT LEGITIMATE RUN")
        else:
            print("RELEASE -", VERSION)
        print("Make sure to report any unusual " + Fore.LIGHTBLUE_EX + "occurrences" + Fore.WHITE + " or " + Fore.LIGHTGREEN_EX + "bugs" + Fore.WHITE + " to help development!")
        print(" ")
        print(Spacer)
        print(Style.BRIGHT + Fore.CYAN + "| 1 | - Play!")
        print(Fore.YELLOW + "| 2 | - Tutorial!")
        print(Fore.MAGENTA + "| 3 | - Setup!")
        print(Fore.WHITE + Spacer)
        Option = int(input(">>>"))
        for x in range(1, SCREEN_HEIGHT):
            print(" ")

        # Tutorial
        if Option == 2:
            print(Spacer)
            print("SETUP:")
            print(Spacer)
            print("| 1 | - Stats and displays")
            print("| 2 | - Scenarios and Stat Changes")
            print("| 3 | - Time and lessons")
            print("| 4 | - Detentions and consequences")
            print("| - | - Close tutorial")
            print(Spacer)
            Option = int(input(">>>"))

            if Option == 1:
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")
                print(Spacer)
                print("Stats are the fundamentals of this game")
                print("If any of your stats reach zero: You lose")
                stall = input(">>>")

                # GENERATE STATS
                Popularity = random.randint(20, 30)
                Popularity = float(Popularity)
                Popularity = Popularity / 10
                Focus = random.randint(30, 50)
                Focus = float(Focus)
                Focus = Focus / 10
                Happiness = random.randint(40, 80)
                Happiness = float(Happiness)
                Happiness = Happiness / 10
                Energy = random.randint(60, 70)
                Energy = float(Energy)
                Energy = Energy / 10
                Battery = random.randint(80, 100)
                # GENERATE STATS

                render()

                print("In this randomly generated starting stat display, it shows you that happiness is", Happiness, " and that Battery is", Battery, "%")
                print("This is how stats will be displayed every scenario")

                # noinspection PyRedeclaration
                stall = input(">>>")

                print(Spacer)

                print("Continue To 2: Scenarios? ")
                Option = int(input("1: yes   2: no"))
                if Option == 1:
                    Option = 2
                else:
                    for x in range(1, SCREEN_HEIGHT):
                        print(" ")

            if Option == 2:
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")
                print(Spacer)
                print("Scenarios are another fundamental part of this game")
                print("One scenario happens every period but some may have multiple options ")

                stall = input(">>>")

                render()
                Scenario = "Bored"
                print("You are bored, what do you do? ")
                print(" ")
                print(Spacer)
                print("| 1 | - Throw paper at teacher")
                print("| 2 | - Play games on IPad")
                print("| 3 | - Chat with friends")
                print("| 4 | - Dont do anything")
                print(Spacer)
                print(">>>")
                print(" ")
                print("This a example of a Scenario")
                print("When prompted by '>>>' type the number of the option you want to pick")
                print("This will Apply the relevant stat changes from that option and may give you a second 'mini' scenario")

                # noinspection PyRedeclaration
                stall = input(">>>")

                print(Spacer)

                print("Continue To 3: Time and lessons? ")
                Option = int(input("1: yes   2: no"))
                if Option == 1:
                    Option = 3
                else:
                    for x in range(1, SCREEN_HEIGHT):
                        print(" ")

            if Option == 3:
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")
                print(Spacer)
                print("Time is handled in this game via periods")
                print("There are 6 work periods(Period 1 - 6) and a break period inbetween P2 and P3 and a lunch period inbetween P4 and P5")

                stall = input(">>>")

                print("Periods have different scenarios that can happen and different lessons")

                # noinspection PyRedeclaration
                stall = input(">>>")

                print("Lessons can happen in period 1 - 6 and not at break or lunch (In that case the lesson IS break or lunch as well as the Period)")
                print("There are many lesson specific scenarios and there is a new lesson generator that can make doubles and stop reoccurrences")

                # noinspection PyRedeclaration
                stall = input(">>>")
                print(Spacer)
                print("Continue To 4: Detention? ")
                Option = int(input("1: yes   2: no"))
                if Option == 1:
                    Option = 4
                else:
                    for x in range(1, SCREEN_HEIGHT):
                        print(" ")

            if Option == 4:
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")
                print(Spacer)
                print("Detentions happen at the end of the day (Period 6) and occur if you get a C2")

                stall = input(">>>")

                print("The 'C's (Short for consequence) are 'Bad Points' aka taking a marble out of the jar (Scary!)")
                print("A C1 Doesnt have much effect but if you get 3, can equate to a C2")
                print("A C2 Gives you a detention but if you get 3, can equate to a C3")
                print("A C3 Gives you an 'Isolation'(Isolated from the rest of the school for 3 days while your stats slowly go down) but if you get 3, can equate to a C4")
                print("A C4 Ends the game and prompts you to try again")

                # noinspection PyRedeclaration
                stall = input(">>>")

                print("A Normal Detention (ANY MODE ACCEPT IMPOSSIBLE) Is relatively harmless: It decreases all your stats from ~1 to ~2.5")
                print("However to add extra challenge if you are playing on impossible: It HALVES all your stats!")

                # noinspection PyRedeclaration
                # stall = input(">>>")
                # print(Spacer)
                # print("Continue To 4: Detention? ")
                # Option = int(input("1: yes   2: no"))
                # if Option == 1:
                #       Option = 4
                # else:
                #       for x in range(1, SCREEN_HEIGHT):
                #           print(" ")

        # Setup
        elif Option == 3:
            print(Spacer)
            print("SETUP:")
            print(Spacer)
            print("| 1 | - SETUP SCREEN WIDTH")
            print("| 2 | - SETUP SCREEN HEIGHT")
            print("| - | - CLOSE SETTINGS")
            print(Spacer)
            Option = int(input(">>>"))

            if Option == 1:
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")
                print(Spacer)
                print("SETUP SCREEN WIDTH")
                print(Spacer)
                print("Type the number of columns your screen/terminal window is: DEFAULT - 80")
                print(Spacer)
                SCREEN_WIDTH = int(input(">>>"))
                Spacer = "=" * SCREEN_WIDTH
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")

            if Option == 2:
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")
                print(Spacer)
                print("SETUP SCREEN HEIGHT")
                print(Spacer)
                print("Type the number of rows your screen/terminal window is: DEFAULT - 24")
                print(Spacer)
                SCREEN_HEIGHT = int(input(">>>"))
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")

        # Dev Menu:
        elif Option == 4:
            print(Spacer)
            print("DEV MENU")
            print(Spacer)
            print("| 1 | - SET 'Detention' VARIABLE TO 'True'")
            print("| 2 | - SET 'Isolation' VARIABLE TO 'True'")
            print("| 3 | - SET 'Time' VARIABLE")
            print("| 4 | - CLOSE DEV MENU")
            print(Spacer)
            Option = int(input(">>>"))

            if Option == 1:
                Dev = True
                Detention = True
                print("Detention set to True")
                stall = input(">>>")

            if Option == 2:
                Dev = True
                Isolation = True
                print("Isolation set to True")
                stall = input(">>>")

            if Option == 3:
                Dev = True
                Time = int(input("NUMBER - >>>"))
                print("Time set to: ", Time)
                stall = input(">>>")

        # LAUNCH
        else:
            print(Spacer)
            print(Fore.CYAN + "Play!")
            print(Fore.WHITE + Spacer)
            print(Fore.LIGHTGREEN_EX + "| 1 | - Easy - x0.75")
            print(Fore.GREEN + "| 2 | - Normal - x1.0")
            print(Fore.BLUE + "| 3 | - Hard - x1.25")
            print(Fore.RED + "| 4 | - Insane - x1.5")
            print(Fore.RED + Style.DIM + "| 5 | - Impossible - x2.0")
            print(Style.RESET_ALL + Style.BRIGHT + Fore.CYAN + "| 6 | - Go Back")
            print(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + Spacer)
            Option = int(input(">>>"))

            # Multipliers
            if Option == 1:
                Multiplier = 0.75
            elif Option == 2:
                Multiplier = 1.0
            elif Option == 3:
                Multiplier = 1.25
            elif Option == 4:
                Multiplier = 1.5
            elif Option == 5:
                Multiplier = 2.0
            print(Multiplier, "DEBUG")

            # INITIALISE GAME
            if Option == 1 or Option == 2 or Option == 3 or Option == 4 or Option == 5:
                Spacer = "=" * SCREEN_WIDTH
                Menuloop = False    # Disable Menu Repeat
                Mainloop = True     # Start Main Game Loop

    # Generate Stats
    if True:
        Popularity = random.randint(20, 30)
        Popularity = float(Popularity)
        Popularity = Popularity / 10
        Focus = random.randint(30, 50)
        Focus = float(Focus)
        Focus = Focus / 10
        Happiness = random.randint(40, 80)
        Happiness = float(Happiness)
        Happiness = Happiness / 10
        Energy = random.randint(60, 70)
        Energy = float(Energy)
        Energy = Energy / 10
        Battery = random.randint(80, 100)

    # GameLoop
    while Mainloop:

        # LESSON ENGINE AND SET PERIOD TIME AND DAY INFO
        if True:

            # SPACE
            for x in range(1, SCREEN_HEIGHT):
                print(" ")

            # LESSONS BREAK AND LUNCH SKIP
            if Period == "BREAK":
                Lesson = "B"
            elif Period == "LUNCH":
                Lesson = "L"

            # LESSON SETTING: CORE
            else:
                # Reset Last Lesson and Counters At Start Of Day
                if Period == "PERIOD 1":
                    LastLesson = "None"
                    CoLessonCounter = 0
                    DtLessonCounter = 0
                    EnLessonCounter = 0
                    SpLessonCounter = 0
                    HiLessonCounter = 0
                    ScLessonCounter = 0
                    OldPopularity = Popularity
                    OldFocus = Focus
                    OldHappiness = Happiness
                    OldEnergy = Energy
                    OldBattery = Battery

                # NORMAL LESSON GENERATION - P1 P3 P5
                if Period == "PERIOD 1" or Period == "PERIOD 3" or Period == "PERIOD 5":

                    # Normal Lesson Changer
                    Lessonloop = True
                    while Lessonloop:

                        # Random
                        LessonNumber = random.randint(1, 8)

                        # Computing
                        if LessonNumber == 1 or LessonNumber == 2:
                            Lesson = "Co"
                            if CoLessonCounter < 2:
                                Lessonloop = False
                                CoLessonCounter = CoLessonCounter + 1
                        # Design Tech
                        elif LessonNumber == 3 or LessonNumber == 4:
                            Lesson = "Dt"
                            if DtLessonCounter < 2:
                                Lessonloop = False
                                DtLessonCounter = DtLessonCounter + 1
                        # English
                        elif LessonNumber == 5:
                            Lesson = "En"
                            if EnLessonCounter < 2:
                                Lessonloop = False
                                EnLessonCounter = EnLessonCounter + 1
                        # Spanish
                        elif LessonNumber == 6:
                            Lesson = "Sp"
                            if SpLessonCounter < 2:
                                Lessonloop = False
                                SpLessonCounter = SpLessonCounter + 1
                        # History
                        elif LessonNumber == 7:
                            Lesson = "Hi"
                            if HiLessonCounter < 2:
                                Lessonloop = False
                                HiLessonCounter = HiLessonCounter + 1
                        # Science
                        elif LessonNumber == 8:
                            Lesson = "Sc"
                            if ScLessonCounter < 2:
                                Lessonloop = False
                                ScLessonCounter = ScLessonCounter + 1
                        # Other - ERROR
                        else:
                            print("ERROR - THAT LESSON NUMBER IS NOT DEFINED")
                            print("NOTE TO SELF - LOOK FOR NORMAL LESSON GENERATION - P1 P3 P5 - NORMAL LESSON CHANGER")
                            stall = input(">>>")
                        # Lesson used if double lesson is chosen
                        LastLesson = Lesson

                # NORMAL LESSON GENERATION - P2 P4 P6
                elif Period == "PERIOD 2" or Period == "PERIOD 4" or Period == "PERIOD 6":
                    # Random
                    GenericRandom = random.randint(1, 10)

                    # Single Lesson
                    if GenericRandom < 8:
                        # Normal Lesson Changer
                        Lessonloop = True
                        while Lessonloop:

                            # Random
                            LessonNumber = random.randint(1, 8)
                            # Computing
                            if LessonNumber == 1 or LessonNumber == 2:
                                Lesson = "Co"
                                if CoLessonCounter < 2:
                                    Lessonloop = False
                                    CoLessonCounter = CoLessonCounter + 1
                            # Design Tech
                            elif LessonNumber == 3 or LessonNumber == 4:
                                Lesson = "Dt"
                                if DtLessonCounter < 2:
                                    Lessonloop = False
                                    DtLessonCounter = DtLessonCounter + 1
                            # English
                            elif LessonNumber == 5:
                                Lesson = "En"
                                if EnLessonCounter < 2:
                                    Lessonloop = False
                                    EnLessonCounter = EnLessonCounter + 1
                            # Spanish
                            elif LessonNumber == 6:
                                Lesson = "Sp"
                                if SpLessonCounter < 2:
                                    Lessonloop = False
                                    SpLessonCounter = SpLessonCounter + 1
                            # History
                            elif LessonNumber == 7:
                                Lesson = "Hi"
                                if HiLessonCounter < 2:
                                    Lessonloop = False
                                    HiLessonCounter = HiLessonCounter + 1
                            # Science
                            elif LessonNumber == 8:
                                Lesson = "Sc"
                                if ScLessonCounter < 2:
                                    Lessonloop = False
                                    ScLessonCounter = ScLessonCounter + 1

                    # Double Lesson
                    elif GenericRandom > 7:
                        Lesson = LastLesson
                        if Lesson == "Co":
                            CoLessonCounter = 2
                        elif Lesson == "Dt":
                            DtLessonCounter = 2
                        elif Lesson == "En":
                            EnLessonCounter = 2
                        elif Lesson == "Sp":
                            SpLessonCounter = 2
                        elif Lesson == "Hi":
                            HiLessonCounter = 2
                        elif Lesson == "Sc":
                            ScLessonCounter = 2

                        # ERROR
                        else:
                            print("ERROR: VARIABLE 'LastLesson' OR VARIABLE 'Lesson' WAS SET WRONG")
                            print("NOTE FOR SELF - LOOK FOR LESSON SETTING - NORMAL LESSON GEN - P1 P3 P5")
                            print("SHUTTING DOWN")
                            Mainloop = False
                            stall = input(">>>")

                    # ERROR
                    else:
                        print("ERROR: CAN'T DECIDE IF SINGLE OR DOUBLE LESSON")
                        print("NOTE FOR SELF - LOOK FOR LESSON SETTING - NORMAL LESSON GEN - P2 P4 P6")
                        print("SHUTTING DOWN")
                        Mainloop = False
                        stall = input(">>>")

                # ERROR
                else:
                    print("ERROR - NO LESSON GEN TOOK PLACE")
                    print("this is probably caused by the time being wrong / not registered?")
                    print("Time = " + Time)
                    stall = input(">>>")

                # PRINT LESSON - WORKING
                if Lesson == "Co":
                    print("COMPUTING")
                elif Lesson == "Dt":
                    print("DESIGN TECH")
                elif Lesson == "En":
                    print("ENGLISH")
                elif Lesson == "Sp":
                    print("SPANISH")
                elif Lesson == "Hi":
                    print("HISTORY")
                elif Lesson == "Sc":
                    print("SCIENCE")
                elif Lesson == "Pe":
                    print("PE")
                elif Lesson == "Ma":
                    print("MATH")
                elif Lesson == "Re":
                    print("RE")
                elif Lesson == "B":
                    print(" ")  # BREAK SKIP
                elif Lesson == "L":
                    print(" ")  # LUNCH SKIP
                else:
                    print("lesson not recognised")

            # SET DAY
            if True:
                # SET DAY
                if Time == 1 or Time == 2 or Time == 3 or Time == 4 or Time == 5 or Time == 6 or Time == 7 or Time == 8:
                    Day = "MONDAY"
                    print(Day)
                elif Time == 9 or Time == 10 or Time == 11 or Time == 12 or Time == 13 or Time == 14 or Time == 15 or Time == 16:
                    Day = "TUESDAY"
                    print(Day)
                elif Time == 17 or Time == 18 or Time == 19 or Time == 20 or Time == 21 or Time == 22 or Time == 23 or Time == 24:
                    Day = "WEDNESDAY"
                    print(Day)
                elif Time == 25 or Time == 26 or Time == 27 or Time == 28 or Time == 29 or Time == 30 or Time == 31 or Time == 32:
                    Day = "THURSDAY"
                    print(Day)
                elif Time == 33 or Time == 34 or Time == 35 or Time == 36 or Time == 37 or Time == 38 or Time == 39 or Time == 40:
                    Day = "FRIDAY"
                    print(Day)
                else:
                    Day = "UNKNOWN"
                    print(Day)

            # Print Period
            print(Period)

            # SET 'DisplayLesson'
            if True:

                if Lesson == "Co":
                    DisplayLesson = "COMPUTING"
                elif Lesson == "Dt":
                    DisplayLesson = "DESIGN TECH"
                elif Lesson == "En":
                    DisplayLesson = "ENGLISH"
                elif Lesson == "Sp":
                    DisplayLesson = "SPANISH"
                elif Lesson == "Hi":
                    DisplayLesson = "HISTORY"
                elif Lesson == "Sc":
                    DisplayLesson = "SCIENCE"
                elif Lesson == "Pe":
                    DisplayLesson = "PE"
                elif Lesson == "Ma":
                    DisplayLesson = "MATH"
                elif Lesson == "Re":
                    DisplayLesson = "RE"
                elif Lesson == "B":
                    DisplayLesson = " "    # BREAK SKIP
                elif Lesson == "L":
                    DisplayLesson = " "     # LUNCH SKIP
                else:
                    print("UNRECOGNISED LESSON")

        # Space
        if True:

            stall = input()
            for x in range(1, SCREEN_HEIGHT):
                print(" ")

        # Isolations
        if Period == "PERIOD 1" and Isolation == True:
            # Disable Isolations
            Isolation = False

            # Skip Scenarios
            WasThereAIsolationToday = True

            for x in range(1, 6):
                for y in range(1, SCREEN_HEIGHT):
                    print(" ")
                if y == 0:
                    print("PERIOD 1")
                if y == 1:
                    print("PERIOD 2")
                if y == 2:
                    print("PERIOD 3")
                if y == 3:
                    print("PERIOD 4")
                if y == 4:
                    print("PERIOD 5")
                if y == 5:
                    print("PERIOD 6")
                print("Your Stats Went Down")
                Time = Time + 1
                time.sleep(1)
                Popularity = Popularity - (random.randint(1, 4) / (10 * Multiplier))
                Focus = Focus - (random.randint(1, 10) / (10 * Focus))
                Happiness = Happiness - (random.randint(1, 20) / (10 * Multiplier))
                Energy = Energy - (random.randint(1, 4) / (10 * Multiplier))

            # REFINE
            if True:
                # REFINE OVER 10/100
                if Popularity > 10:
                    Popularity = 10
                if Focus > 10:
                    Focus = 10
                if Happiness > 10:
                    Happiness = 10
                if Energy > 10:
                    Energy = 10
                if Battery > 100:
                    Battery = 100

                # REFINE UNDER 0
                if Popularity < 0:
                    Popularity = 0
                if Focus < 0:
                    Focus = 0
                if Happiness < 0:
                    Happiness = 0
                if Energy < 0:
                    Energy = 0
                if Battery < 0:
                    Battery = 0

                # ROUND
                Popularity = round(Popularity, 1)
                Focus = round(Focus, 1)
                Happiness = round(Happiness, 1)
                Energy = round(Energy, 1)

                # C1/C2/C3/C4 CONVERSION
                if C1 > 2:
                    C1 = C1 - 3
                    C2 = C2 + 1
                    print("You got 3 C1s You got a C2")
                    Detention = True
                if C2 > 2:
                    C2 = C2 - 3
                    C3 = C3 + 1
                    print("You got 3 C2s You got a C3")
                    Isolation = True
                if C3 > 2:
                    C3 = C3 - 3
                    C4 = C4 + 1
                    print("You got 3 C3s You got a C4")

        # MAIN - SCENARIOS
        if not WasThereAIsolationToday:

            # Setup
            if True:
                # ENABLE SCENARIOS
                Menuloop = True

                # Get Scenario To Load
                ScenarioNumber = random.randint(1, 10)
                if ScenarioNumber > 1:
                    ScenarioNumber = random.randint(4, 4)
                else:
                    ScenarioNumber = random.randint(1, 3)

            # 1: EXTRA - COULD DO WITH MORE DETAIL - MULTIPLIER
            if ScenarioNumber == 1:
                while Menuloop:
                    render()
                    Scenario = "Bored"
                    print("You are bored, what do you do? ")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Throw paper at teacher")
                    print("| 2 | - Play games on IPad")
                    print("| 3 | - Chat with friends")
                    print("| 4 | - Dont do anything")
                    print(Spacer)
                    Option = int(input(">>>"))
                    print(Spacer)
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4:
                        Menuloop = False
                    if Option == 1:
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 4:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You got away with it!")
                            Popularity = Popularity + 1
                            Focus = Focus - 0.2 * Multiplier
                            Happiness = Happiness + 0.5
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You got caught! The teacher gives you a C2")
                            C2 = C2 + 1
                            if not Detention:
                                Detention = True
                                DetentionLesson = Lesson
                            Popularity = Popularity + 1.4
                            Happiness = Happiness - 3 * Multiplier
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 2:
                        if IPad == True and Battery > 0:
                            GenericRandom = random.randint(1, 10)
                            if GenericRandom < 3:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You got caught! The teacher gives you a C1 and takes your IPad!")
                                IPad = False
                                Popularity = Popularity + 0.1
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness - 2.3 * Multiplier
                                Energy = Energy - 0.5 * Multiplier
                                Battery = Battery - random.randint(3, 15) * Multiplier
                            else:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You got away with it and had a great time gaming!")
                                Popularity = Popularity + 0
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness + 1
                                Energy = Energy - 0.5 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                        else:
                            if not IPad:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You don't have an IPad right now, idiot.")
                            elif IPad == True and Battery < 1:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("Your IPad is dead right now, idiot.")
                    elif Option == 3:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You chat with your friends")
                        Popularity = Popularity + 0.1
                        Focus = Focus - 0.5 * Multiplier
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 4:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You dont do anything")
                        Focus = Focus + 0.8
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # 2: EXTRA - COMPLETE - MULTIPLIER
            elif ScenarioNumber == 2:
                while Menuloop:
                    render()
                    Scenario = "Ipad Charge"
                    print("You wonder if you could charge your IPad right now")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Ask the teacher")
                    print("| 2 | - Sneak into a room to charge it")
                    print("| 3 | - Ask for a battery pack")
                    print("| 4 | - Dont charge")
                    print(Spacer)
                    Option = int(input(">>>"))
                    print(Spacer)
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4:
                        Menuloop = False
                    if Option == 1 or Option == 2 or Option == 3 and IPad == False:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You don't have an IPad right now, idiot.")
                    elif Option == 1:
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 6:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The teacher said no")
                            Happiness = Happiness - 1 * Multiplier
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The teacher agreed!")
                            Happiness = Happiness + 1
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery + random.randint(5, 35)
                    elif Option == 2:
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 7:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            if Lesson == "B" or Lesson == "L":
                                print("You got caught")
                                print("Since it was break you didn't get a C1")
                                Battery = Battery - random.randint(1, 5) * Multiplier
                                Happiness = Happiness - 1.3 * Multiplier
                            else:
                                if True:
                                    # REFINE OVER 10/100
                                    if Popularity > 10:
                                        Popularity = 10
                                    if Focus > 10:
                                        Focus = 10
                                    if Happiness > 10:
                                        Happiness = 10
                                    if Energy > 10:
                                        Energy = 10
                                    if Battery > 100:
                                        Battery = 100
                                    # REFINE UNDER 0
                                    if Popularity < 0:
                                        Popularity = 0
                                    if Focus < 0:
                                        Focus = 0
                                    if Happiness < 0:
                                        Happiness = 0
                                    if Energy < 0:
                                        Energy = 0
                                    if Battery < 0:
                                        Battery = 0
                                    # ROUND
                                    Popularity = round(Popularity, 1)
                                    Focus = round(Focus, 1)
                                    Happiness = round(Happiness, 1)
                                    Energy = round(Energy, 1)
                                render()
                                print("A teacher stops you")
                                print(" ")
                                print(Spacer)
                                print("| 1 | - Lie")
                                print("| 2 | - Tell them")
                                print("| 3 | - Run Away")
                                print(Spacer)
                                Option = int(input(">>>"))
                                print(Spacer)
                                if Option == 1:
                                    GenericRandom = random.randint(1, 10)
                                    if GenericRandom != 10 or GenericRandom != 9:
                                        for x in range(1, SCREEN_HEIGHT):
                                            print(" ")
                                        print(Spacer)
                                        print("The teacher believed you and you made it out unpunished")
                                        Popularity = Popularity + 0.6
                                        Happiness = Happiness + 1.2
                                        Energy = Energy - 0.2 * Multiplier
                                        Battery = Battery - random.randint(1, 5) * Multiplier
                                    else:
                                        for x in range(1, SCREEN_HEIGHT):
                                            print(" ")
                                        print(Spacer)
                                        print("You got a C2 for sneaking around the hallways!")
                                        C2 = C2 + 1
                                        if not Detention:
                                            Detention = True
                                            DetentionLesson = Lesson
                                        Popularity = Popularity + 0.1
                                        Happiness = Happiness - 0.7 * Multiplier
                                        Energy = Energy - 0.2 * Multiplier
                                        Battery = Battery - random.randint(1, 5) * Multiplier
                                elif Option == 2:
                                    for x in range(1, SCREEN_HEIGHT):
                                        print(" ")
                                    print(Spacer)
                                    print("You got a C1 instead of a C2 because you owned up")
                                    C1 = C1 + 1
                                    Popularity = Popularity + 0.1
                                    Happiness = Happiness - 0.7 * Multiplier
                                    Energy = Energy - 0.2 * Multiplier
                                    Battery = Battery - random.randint(1, 5) * Multiplier
                                elif Option == 3:
                                    for x in range(1, SCREEN_HEIGHT):
                                        print(" ")
                                    print(Spacer)
                                    print("The teacher calls Mr Brooks who catches up to you easily")
                                    print("You got a C3")
                                    C3 = C3 + 1
                                    Isolation = True
                                    Popularity = Popularity + 2.3
                                    Happiness = Happiness - 4.6 * Multiplier
                                    Energy = Energy - 4.7 * Multiplier
                                    Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print("You didn't get caught")
                            Popularity = Popularity + 1.5
                            Focus = Focus + 4
                            Happiness = Happiness + 1
                            Energy = Energy - 5 * Multiplier
                            Battery = Battery + random.randint(65, 100)
                    elif Option == 3:
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 6:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("No one had one")
                            Popularity = Popularity - 0.4 * Multiplier
                            Energy = Energy - 1.4 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("A friend lends you a battery pack to use")
                            Energy = Energy - 0.7 * Multiplier
                            Battery = Battery + random.randint(23, 54)
                    elif Option == 4:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You decide its not worth the effort")
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # 3: EXTRA - COMPLETE - MULTIPLIER
            elif ScenarioNumber == 3:
                while Menuloop:
                    render()
                    Scenario = "You are hungry"
                    print("You are really hungry")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Get a sandwich")
                    print("| 2 | - Get some fruit")
                    print("| 3 | - Eat nothing")
                    print("| 4 | - Say you feel sick to go home")
                    print("| 5 | - Ask your friends for food")
                    print("| 6 | - Dont do anything")
                    print(Spacer)
                    Option = int(input(">>>"))
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4 or Option == 5 or Option == 6:
                        Menuloop = False
                    if Option == 1:
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 9:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The sandwich was tasty")
                            Focus = Focus - 2 * Multiplier
                            Happiness = Happiness + 1
                            Energy = Energy + 4
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You got caught and given a C1")
                            C1 = C1 + 1
                            Focus = Focus - 2 * Multiplier
                            Happiness = Happiness - 2.3 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 2:
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 9:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The fruit was tasty")
                            Focus = Focus - 2 * Multiplier
                            Happiness = Happiness + 1
                            Energy = Energy + 4
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You got caught and given a C1")
                            C1 = C1 + 1
                            Focus = Focus - 2 * Multiplier
                            Happiness = Happiness - 2.3 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 3:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You dont eat anything")
                        Focus = Focus - 1 * Multiplier
                        Happiness = Happiness - 2 * Multiplier
                        Energy = Energy - 0.5 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 4:
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom == 1:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("They believe you so you get sent home for the day")
                            Time = 8    # SET TO 6TH PERIOD SO WHEN IT GOES TO NEXT PERIOD IT GOES TO THE NEXT DAY
                            Popularity = Popularity + 0.3
                            Focus = Focus - 2 * Multiplier
                            Happiness = Happiness + 3
                            Energy = Energy - 0.2 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You are told off for trying to lie and you get a C2")
                            if not Detention:
                                Detention = True
                                DetentionLesson = Lesson
                            Popularity = Popularity + 2
                            Focus = Focus - 2 * Multiplier
                            Happiness = Happiness - 6 * Multiplier
                            Energy = Energy - 0.2 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 5:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You friends say they don't want to give you any food")
                        Popularity = Popularity - 0.5 * Multiplier
                        Focus = Focus - 1 * Multiplier
                        Happiness = Happiness - 0.5 * Multiplier
                        Energy = Energy - 0.5 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 6:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You dont do anything")
                        Focus = Focus + 0.8
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # 4 - Co: EXTRA - COMPLETE - MULTIPLIER
            elif ScenarioNumber == 4 and Lesson == "Co":
                while Menuloop:
                    render()
                    Scenario = "Mr Henderson is looking away"
                    print("Mr Henderson is looking away, what do you do? ")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Download a random game")
                    print("| 2 | - Play games on IPad")
                    print("| 3 | - Try to break the computer")
                    print("| 4 | - Dont do anything")
                    print(Spacer)
                    Option = int(input(">>>"))
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4:
                        Menuloop = False
                    if Option == 1:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        if True:
                            # REFINE OVER 10/100
                            if Popularity > 10:
                                Popularity = 10
                            if Focus > 10:
                                Focus = 10
                            if Happiness > 10:
                                Happiness = 10
                            if Energy > 10:
                                Energy = 10
                            if Battery > 100:
                                Battery = 100

                            # REFINE UNDER 0
                            if Popularity < 0:
                                Popularity = 0
                            if Focus < 0:
                                Focus = 0
                            if Happiness < 0:
                                Happiness = 0
                            if Energy < 0:
                                Energy = 0
                            if Battery < 0:
                                Battery = 0

                            # ROUND
                            Popularity = round(Popularity, 1)
                            Focus = round(Focus, 1)
                            Happiness = round(Happiness, 1)
                            Energy = round(Energy, 1)
                        render()
                        print("What game will you download?")
                        print("")
                        print(Spacer)
                        print("| 1 | - Download Minecraft")
                        print("| 2 | - Download FNAF")
                        print("| 3 | - Download COD")
                        Option = int(input(">>>"))
                        if Option == 1:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You download Minecraft")
                            GenericRandom = random.randint(1, 10)
                            if GenericRandom > 7:
                                print("You get caught and given a C1")
                                Focus = Focus - 0.5 * Multiplier
                                Happiness = Happiness - 1 * Multiplier
                                Energy = Energy - 0.1 * Multiplier
                                Battery = Battery - random.randint(1, 5) * Multiplier
                                C1 = C1 + 1
                            else:
                                print("You play Minecraft all lesson")
                                Focus = Focus - 0.5 * Multiplier
                                Happiness = Happiness + 0.5
                                Energy = Energy - 0.1 * Multiplier
                                Battery = Battery - random.randint(1, 5) * Multiplier
                        elif Option == 2:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You download FNAF but its obvious you are not doing work")
                            print("You get given a C1")
                            Focus = Focus - 2.3 * Multiplier
                            Happiness = Happiness - 1.7 * Multiplier
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                            C1 = C1 + 1
                        elif Option == 3:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("Download COD? You must be joking")
                            print("It never installs so you end up just daydreaming all lesson")
                            Focus = Focus - 2.4 * Multiplier
                            Happiness = Happiness + 0.3
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 2:
                        if IPad == True and Battery > 0:
                            GenericRandom = random.randint(1, 10)
                            if GenericRandom < 4:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You get caught and given a C1 and have your IPad taken away")
                                IPad = False
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness - 1 * Multiplier
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                                C1 = C1 + 1
                            else:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You dont get caught and play games all lesson")
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness + 1
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                        else:
                            if not IPad:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You don't have an IPad right now, idiot.")
                            elif IPad == True and Battery < 1:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("Your IPad is dead right now, idiot.")
                    elif Option == 3:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        if True:
                            # REFINE OVER 10/100
                            if Popularity > 10:
                                Popularity = 10
                            if Focus > 10:
                                Focus = 10
                            if Happiness > 10:
                                Happiness = 10
                            if Energy > 10:
                                Energy = 10
                            if Battery > 100:
                                Battery = 100

                            # REFINE UNDER 0
                            if Popularity < 0:
                                Popularity = 0
                            if Focus < 0:
                                Focus = 0
                            if Happiness < 0:
                                Happiness = 0
                            if Energy < 0:
                                Energy = 0
                            if Battery < 0:
                                Battery = 0

                            # ROUND
                            Popularity = round(Popularity, 1)
                            Focus = round(Focus, 1)
                            Happiness = round(Happiness, 1)
                            Energy = round(Energy, 1)
                        render()
                        print("How will you break the computer?")
                        print("")
                        print(Spacer)
                        print("| 1 | - Download malware")
                        print("| 2 | - Delete System32")
                        print("| 3 | - Delete drivers")
                        print("| 4 | - Uninstall Apps")
                        print("| 5 | - Install OperaGX")
                        Option = int(input(">>>"))
                        if Option == 1:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You install malware and break the PC")
                            print("The teacher finds out and you get a C2")
                            C2 = C2 + 1
                            if not Detention:
                                Detention = True
                                DetentionLesson = Lesson
                        elif Option == 2:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            GenericRandom = random.randint(1, 100)
                            if GenericRandom < 6:
                                print("You completely nuked windows, WELL DONE!")
                                print("you got 2 C2s though")
                                C2 = C2 + 2
                                if not Detention:
                                    Detention = True
                                    DetentionLesson = Lesson
                                Popularity = Popularity + 2
                                Happiness = Happiness - 2 * Multiplier
                            else:
                                print("You are unable to uninstall System32")
                        elif Option == 3:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You break the PC by uninstalling all the drivers")
                            print("The teacher finds out and you get a C2")
                            C2 = C2 + 1
                        elif Option == 4:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You uninstall all the apps by deleting AppData")
                            print("The teacher finds out and you get a C2")
                            if not Detention:
                                Detention = True
                                DetentionLesson = Lesson
                            C2 = C2 + 1
                        elif Option == 5:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("you install operagx gaming web browser for gamers made by gamers for gamers by gamers.")
                        Popularity = Popularity + 1
                        Focus = Focus - 0.5 * Multiplier
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 4:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You dont do anything")
                        Focus = Focus + 0.8
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # 4 - Dt: EXTRA - COULD DO WITH MORE DETAIL - MULTIPLIER
            elif ScenarioNumber == 4 and Lesson == "Dt":
                while Menuloop:
                    render()
                    Scenario = "Mr Flowers is looking away"
                    print("Mr Flowers is looking away")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Go to the back of the class and mess with your ipad")
                    print("| 2 | - Mess with to saws and other tools")
                    print("| 3 | - Chat with friends")
                    print("| 4 | - Dont do anything")
                    print(Spacer)
                    Option = int(input(">>>"))
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4:
                        Menuloop = False
                    if Option == 1:
                        if IPad == True and Battery > 0:
                            GenericRandom = random.randint(1, 10)
                            if GenericRandom < 4:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You get caught and given a C1 and your IPad gets taken away")
                                IPad = False
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness - 1 * Multiplier
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                                C1 = C1 + 1
                            else:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You dont get caught and play games all lesson")
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness + 1
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                        else:
                            if not IPad:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You don't have an IPad right now, idiot.")
                            elif IPad == True and Battery < 1:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("Your IPad is dead right now, idiot.")
                    elif Option == 2:
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 3:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You don't get caught, you should buy a lottery ticket!")
                            Popularity = Popularity + 0.7
                            Focus = Focus - 1.5 * Multiplier
                            Happiness = Happiness + 1
                            Energy = Energy - 2 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("You got caught, what were you thinking? The teacher gave you a C2")
                            Popularity = Popularity + 2.3
                            Focus = Focus - 3 * Multiplier
                            Happiness = Happiness - 4 * Multiplier
                            Energy = Energy - 2 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                            C1 = C1 + 1
                            if not Detention:
                                Detention = True
                                DetentionLesson = Lesson
                    elif Option == 3:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You chat with friends")
                        Popularity = Popularity + 0.3
                        Focus = Focus - 0.5 * Multiplier
                        Happiness = Happiness + 0.7
                        Energy = Energy - 0.1 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 4:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You dont do anything")
                        Focus = Focus + 0.8
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # 4 - B/L: EXTRA - COMPLETE - MULTIPLIER
            elif ScenarioNumber == 4 and Lesson == "L" or Lesson == "B":
                while Menuloop:
                    render()
                    Scenario = "Lunch Queue"
                    print("Someone pushes past you in the lunch queue, nearly knocking you over")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Argue with them")
                    print("| 2 | - Punch them")
                    print("| 3 | - Tell the teacher")
                    print("| 4 | - Exit the Queue")
                    print("| 5 | - Do nothing")
                    print(Spacer)
                    Option = int(input(">>>"))
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4 or Option == 5:
                        Menuloop = False
                    if Option == 1:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You end up getting punched in the face, that was not worth it")
                        Popularity = Popularity + 0.7
                        Focus = Focus - 1 * Multiplier
                        Happiness = Happiness + 0.1
                        Energy = Energy - 1 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 2:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You get punched in the face, that was not worth it")
                        Popularity = Popularity + 2.5
                        Focus = Focus + 1.2
                        Happiness = Happiness + 1
                        Energy = Energy - 3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 3:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You decide to be 'That Guy' and tell the teacher")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 6:
                            print("The teacher decided to believe you")
                            Popularity = Popularity - 0.3 * Multiplier
                            Focus = Focus + 1
                            Happiness = Happiness + 0.1
                            Energy = Energy - 2 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            print("The teacher doesnt believe you and gives you a C1 for lying")
                            Popularity = Popularity + 0.3
                            Focus = Focus + 0.2
                            Happiness = Happiness - 0.7 * Multiplier
                            Energy = Energy - 1.3 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 4:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You storm out of there in a rage not getting any food")
                        Focus = Focus - 0.2 * Multiplier
                        Happiness = Happiness - 2 * Multiplier
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 5:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You decide to not do anything, smart decision")
                        print("You get some food")
                        Energy = Energy + 4
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # 4 - En: EXTRA - COULD DO WITH MORE DETAIL - MULTIPLIER
            elif ScenarioNumber == 4 and Lesson == "En":
                while Menuloop:
                    render()
                    Scenario = "The English teacher has told you to do the 'Weekly Writing Challenge'"
                    print("The English teacher has told you to do the 'Weekly Writing Challenge'")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Write the weekly wring challenge with the theme - horror")
                    print("| 2 | - Write the weekly wring challenge with the theme - games")
                    print("| 3 | - Write the weekly wring challenge with the theme - school")
                    print("| 4 | - Dont do anything")
                    print(Spacer)
                    Option = int(input(">>>"))
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4:
                        Menuloop = False
                    if Option == 1:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You write a text about horror")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 8:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The teacher liked it!")
                            Focus = Focus + 0.4
                            Happiness = Happiness + 0.5
                            Energy = Energy - 0.7 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The teacher didn't like it")
                            Happiness = Happiness - 0.2 * Multiplier
                            Energy = Energy - 0.6 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 2:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You write a text about games")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 4:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The teacher surprisingly liked it")
                            Focus = Focus + 1
                            Happiness = Happiness + 1.3
                            Energy = Energy - 0.5 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The teacher didn't like it and gave you a C1")
                            C1 = C1 + 1
                            Happiness = Happiness - 0.5 * Multiplier
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 3:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You write a text about school")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 6:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The teacher finds it interesting")
                            Focus = Focus + 0.3
                            Happiness = Happiness + 0.5
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            print(Spacer)
                            print("The teacher didn't like it so they gave you a C1")
                            C1 = C1 + 1
                            Happiness = Happiness - 0.8 * Multiplier
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 4:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You dont write a text")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 4:
                            print("The teacher doesnt realise so you get away with it")
                            Focus = Focus - 0.6 * Multiplier
                            Happiness = Happiness + 0.5
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            print("You got caught! The teacher gives you a C1")
                            C1 = C1 + 1
                            Happiness = Happiness - 0.7 * Multiplier
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # 4 - Sp: EXTRA - COULD DO WITH EXTRA DETAIL - MULTIPLIER
            elif ScenarioNumber == 4 and Lesson == "Sp":
                while Menuloop:
                    render()
                    Scenario = "You are bored in spanish"
                    print("You are really bored in spanish")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Talk to the people next to you")
                    print("| 2 | - Speak in mandarin")
                    print("| 3 | - Mess on your IPad")
                    print("| 4 | - Just do the work")
                    print("| 5 | - Dont do anything")
                    print(Spacer)
                    Option = int(input(">>>"))
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4 or Option == 5:
                        Menuloop = False
                    if Option == 1:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You chat with your friends")
                        Popularity = Popularity + 0.1
                        Focus = Focus - 0.5 * Multiplier
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 2:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You speak mandarin for the rest of the lesson")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 4:
                            print("The teacher surprisingly found it funny")
                            Focus = Focus + 0.3
                            Happiness = Happiness + 1.3
                            Energy = Energy - 0.5 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            print("The teacher didn't like it and gave you a C1")
                            C1 = C1 + 1
                            Happiness = Happiness - 0.5 * Multiplier
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 3:
                        if IPad == True and Battery > 0:
                            GenericRandom = random.randint(1, 10)
                            if GenericRandom < 4:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You get caught and given a C1")
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness - 1 * Multiplier
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                                C1 = C1 + 1
                            else:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You dont get caught and play games all lesson")
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness + 1
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                        else:
                            if not IPad:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You don't have an IPad right now, idiot.")
                            elif IPad == True and Battery < 1:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("Your IPad is dead right now, idiot.")
                    elif Option == 4:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You got on with the work")
                        Focus = Focus + 0.8
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 5:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You don't do anything")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 4:
                            print("The teacher doesnt realise so you get away with it")
                            Focus = Focus - 0.6 * Multiplier
                            Happiness = Happiness + 0.5
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            print("You got caught! The teacher gives you a C1")
                            C1 = C1 + 1
                            Happiness = Happiness - 0.7 * Multiplier
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # 4 - Hi: EXTRA - COULD DO WITH EXTRA DETAIL - MULTIPLIER
            elif ScenarioNumber == 4 and Lesson == "Hi":
                while Menuloop:
                    render()
                    Scenario = "You are bored in history"
                    print("You are really bored in history")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Talk to the people next to you")
                    print("| 2 | - Try to get sent out")
                    print("| 3 | - Mess on your IPad")
                    print("| 4 | - Just do the work")
                    print("| 5 | - Dont do anything")
                    print(Spacer)
                    Option = int(input(">>>"))
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4 or Option == 5:
                        Menuloop = False
                    if Option == 1:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You chat with your friends")
                        Popularity = Popularity + 0.1
                        Focus = Focus - 0.5 * Multiplier
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 2:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You try to get sent out")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 4:
                            print("The teacher knew you wanted tp get sent out so they gave you a C2")
                            if not Detention:
                                Detention = True
                                DetentionLesson = Lesson
                            Focus = Focus + 0.3
                            Happiness = Happiness - 0.8 * Multiplier
                            Energy = Energy - 0.5 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            print("The teacher didn't notice")
                            C1 = C1 + 1
                            Happiness = Happiness - 0.5 * Multiplier
                            Energy = Energy - 0.6 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 3:
                        if IPad == True and Battery > 0:
                            GenericRandom = random.randint(1, 10)
                            if GenericRandom < 4:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You get caught and given a C1")
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness - 1 * Multiplier
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                                C1 = C1 + 1
                            else:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You dont get caught and play games all lesson")
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness + 1
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                        else:
                            if not IPad:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You don't have an IPad right now, idiot.")
                            elif IPad == True and Battery < 1:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("Your IPad is dead right now, idiot.")
                    elif Option == 4:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You got on with the work")
                        Focus = Focus + 0.8
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 5:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You don't do anything")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 4:
                            print("The teacher doesnt realise so you get away with it")
                            Focus = Focus - 0.6 * Multiplier
                            Happiness = Happiness + 0.5
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            print("You got caught! The teacher gives you a C1")
                            C1 = C1 + 1
                            Happiness = Happiness - 0.7 * Multiplier
                            Energy = Energy - 0.1 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # 4 - Sc: EXTRA - COMPLETE - MULTIPLIER
            elif ScenarioNumber == 4 and Lesson == "Sc":
                while Menuloop:
                    render()
                    Scenario = "There is a science practical "
                    print("There is a Mandatory science practical")
                    print(" ")
                    print(Spacer)
                    print("| 1 | - Drink the 'Mystery Liquid'")
                    print("| 2 | - Try to get sent out")
                    print("| 3 | - Mess on your IPad")
                    print("| 4 | - Just do the practical")
                    print(Spacer)
                    Option = int(input(">>>"))
                    if Option == 1 or Option == 2 or Option == 3 or Option == 4:
                        Menuloop = False
                    if Option == 1:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You drink the 'Mystery Liquid'")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 7:
                            print("It was just saltwater. Close one!")
                            Popularity = Popularity + 0.6
                            Focus = Focus - 0.5 * Multiplier
                            Happiness = Happiness + 1
                            Energy = Energy - 0.3 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            for x in range(1, SCREEN_HEIGHT):
                                print(" ")
                            Menuloop = True
                            while Menuloop:
                                render()
                                Scenario = "HYDROCHLORIC ACID "
                                print("It was Hydrochloric Acid. What do you do now?")
                                print(" ")
                                print(Spacer)
                                print("| 1 | - Tell everyone")
                                print("| 2 | - Tell the teacher")
                                print("| 3 | - Tell your parents")
                                print("| 4 | - Tell no none")
                                print(Spacer)
                                Option = int(input(">>>"))
                                if Option == 1 or Option == 2 or Option == 3 or Option == 4:
                                    Menuloop = False
                                if Option == 1:
                                    for x in range(1, SCREEN_HEIGHT):
                                        print(" ")
                                    print("You decide to brag about it")
                                    if GenericRandom < 8:
                                        print("The teachers dont hear")
                                        Popularity = Popularity + 5.3
                                        Happiness = Happiness - 0.6 * Multiplier
                                        Energy = Energy - 4 * Multiplier
                                        Battery = Battery - random.randint(1, 5) * Multiplier
                                        time.sleep(0.5)
                                        print("You feel sick")
                                        print("You get sent to the hospital")
                                        print("Its too late: YOU DIED")
                                        Dead = True
                                    else:
                                        print("The teachers hear and ask you about it")
                                        print("You tell them its true")
                                        print("You get sent to the hospital")
                                        print("You recover")
                                        Popularity = Popularity + 5.6
                                        Happiness = Happiness - 0.6 * Multiplier
                                        Energy = Energy - 4 * Multiplier
                                        Battery = Battery - random.randint(1, 5) * Multiplier
                                elif Option == 2:
                                    for x in range(1, SCREEN_HEIGHT):
                                        print(" ")
                                    print("You tell the teachers")
                                    print("You get sent to the hospital")
                                    print("You recover")
                                    Popularity = Popularity + 5.6
                                    Happiness = Happiness - 0.6 * Multiplier
                                    Energy = Energy - 4 * Multiplier
                                    Battery = Battery - random.randint(1, 5) * Multiplier
                                elif Option == 3:
                                    for x in range(1, SCREEN_HEIGHT):
                                        print(" ")
                                    print("You tell your parents")
                                    print("You get sent to the hospital")
                                    print("You luckily recover")
                                    Popularity = Popularity + 3.5
                                    Happiness = Happiness - 2 * Multiplier
                                    Energy = Energy - 4 * Multiplier
                                    Battery = Battery - random.randint(1, 5) * Multiplier
                                elif Option == 4:
                                    for x in range(1, SCREEN_HEIGHT):
                                        print(" ")
                                    print("You don't tell anyone")
                                    print("You feel sick")
                                    print("You get taken to the doctors")
                                    time.sleep(0.5)
                                    print("You go to the hospital")
                                    time.sleep(2)
                                    print("They cant save you: its too late")
                                    print("YOU DIED")
                                    Dead = True
                                else:
                                    for x in range(1, SCREEN_HEIGHT):
                                        print(" ")
                    elif Option == 2:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You try to get sent out")
                        GenericRandom = random.randint(1, 10)
                        if GenericRandom < 4:
                            print("The teacher knew you wanted tp get sent out so they gave you a C2")
                            if not Detention:
                                Detention = True
                                DetentionLesson = Lesson
                            C2 = C2 + 1
                            Focus = Focus + 0.3
                            Happiness = Happiness - 0.8 * Multiplier
                            Energy = Energy - 0.5 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                        else:
                            print("The teacher didn't notice")
                            C1 = C1 + 1
                            Happiness = Happiness - 0.5 * Multiplier
                            Energy = Energy - 0.6 * Multiplier
                            Battery = Battery - random.randint(1, 5) * Multiplier
                    elif Option == 3:
                        if IPad == True and Battery > 0:
                            GenericRandom = random.randint(1, 10)
                            if GenericRandom < 4:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You get caught and given a C1")
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness - 1 * Multiplier
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                                C1 = C1 + 1
                            else:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You dont get caught and play games all lesson")
                                Focus = Focus - 1.5 * Multiplier
                                Happiness = Happiness + 1
                                Energy = Energy - 0.2 * Multiplier
                                Battery = Battery - random.randint(10, 25) * Multiplier
                        else:
                            if not IPad:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("You don't have an IPad right now, idiot.")
                            elif IPad == True and Battery < 1:
                                for x in range(1, SCREEN_HEIGHT):
                                    print(" ")
                                print(Spacer)
                                print("Your IPad is dead right now, idiot.")
                    elif Option == 4:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
                        print(Spacer)
                        print("You got on with the work")
                        Focus = Focus + 0.8
                        Happiness = Happiness + 1
                        Energy = Energy - 0.3 * Multiplier
                        Battery = Battery - random.randint(1, 5) * Multiplier
                    else:
                        for x in range(1, SCREEN_HEIGHT):
                            print(" ")
            # ERROR
            else:
                print("ERROR: NO SCENARIO")
                print("AFFECTED VARIABLES: 'ScenarioNumber' and 'Lesson'")
                print("SCENARIONUMBER:", ScenarioNumber)
                print("LESSON:", Lesson)
                print("TERMINATING: MainLoop = False")
                MainLoop = False
                stall = input(">>>")

        else:
            # Set to False
            WasThereAIsolationToday = False

        # Stall and Refine
        if True:

            # STALL
            print("PRESS ENTER TO CONTINUE")
            stall = input(">>>")

            # REFINE
            if True:
                # REFINE OVER 10/100
                if Popularity > 10:
                    Popularity = 10
                if Focus > 10:
                    Focus = 10
                if Happiness > 10:
                    Happiness = 10
                if Energy > 10:
                    Energy = 10
                if Battery > 100:
                    Battery = 100

                # REFINE UNDER 0
                if Popularity < 0:
                    Popularity = 0
                if Focus < 0:
                    Focus = 0
                if Happiness < 0:
                    Happiness = 0
                if Energy < 0:
                    Energy = 0
                if Battery < 0:
                    Battery = 0

                # ROUND
                Popularity = round(Popularity, 1)
                Focus = round(Focus, 1)
                Happiness = round(Happiness, 1)
                Energy = round(Energy, 1)

                # C1/C2/C3/C4 CONVERSION
                if C1 > 2:
                    C1 = C1 - 3
                    C2 = C2 + 1
                    print("You got 3 C1s You got a C2")
                    Detention = True
                if C2 > 2:
                    C2 = C2 - 3
                    C3 = C3 + 1
                    print("You got 3 C2s You got a C3")
                    Isolation = True
                if C3 > 2:
                    C3 = C3 - 3
                    C4 = C4 + 1
                    print("You got 3 C3s You got a C4")

        # DETENTION - NEEDS UPGRADE
        if Detention == True and Period == "PERIOD 6":
            for x in range(1, SCREEN_HEIGHT):
                print(" ")
            # TIME INFO ETC.
            if True:
                # PRINT DAY - WORKING
                print(Day)
                print("DETENTION")
                print(DisplayLesson)

            stall = input(">>>")
            for x in range(1, SCREEN_HEIGHT):
                print(" ")
            print("You spend what seems like ages in detention")
            if Multiplier == 2.0:
                time.sleep(5)
                print("YOUR STATS GOT HALVED!")
                Popularity = Popularity // 2
                Focus = Focus // 2
                Energy = Energy // 2
                Happiness = Happiness // 2
            else:
                print("YOUR STATS DECREASED!")
                Popularity = Popularity - (random.randint(1, 10) / 10)
                Focus = Focus - (random.randint(1, 10) / 10)
                Energy = Energy - (random.randint(1, 19) / 10)
                Happiness = Happiness - (random.randint(1, 45) / 10)
            time.sleep(5)
            print("You feel really tired")
            print("Press enter to continue")
            # noinspection PyRedeclaration
            stall = input(">>>")

        # End, Time, Charging
        if True:
            # END
            if Time >= 40 or C4 == 1 or Happiness == 0 or Energy == 0 or Popularity == 0 or Focus == 0 or Dead == True:
                # GAME OVER

                for x in range(1, SCREEN_HEIGHT):
                    print(" ")
                render()
                print(Spacer)
                Mainloop = False

                if Time >= 40:
                    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "GAME DONE!:")
                    print(Fore.LIGHTCYAN_EX + "You made it to the end of the week!")
                elif Dead:
                    print(Fore.LIGHTRED_EX + "YOU DIED")
                    print("Dont die next time? Just a tip")
                else:
                    print(Fore.LIGHTRED_EX + "GAME OVER:")
                if C4 == 1:
                    print(Fore.LIGHTCYAN_EX + "You got expelled - Try again")
                elif Popularity == 0:
                    print(Fore.LIGHTCYAN_EX + "Your popularity reached zero - Try again")
                elif Happiness == 0:
                    print(Fore.LIGHTCYAN_EX + "Your happiness reached zero - Try again")
                elif Focus == 0:
                    print(Fore.LIGHTCYAN_EX + "Your focus reached zero - Try again")
                elif Energy == 0:
                    print(Fore.LIGHTCYAN_EX + "Your energy reached zero - Try again")

                print(Fore.WHITE + Spacer)

                if Multiplier == 0.75:
                    print(Fore.LIGHTGREEN_EX + "| MODE | - EASY")
                elif Multiplier == 1.0:
                    print(Fore.GREEN + "| MODE | - NORMAL")
                elif Multiplier == 1.25:
                    print(Fore.BLUE + "| MODE | - HARD")
                elif Multiplier == 1.5:
                    print(Fore.RED + "| MODE | - INSANE")
                elif Multiplier == 2.0:
                    print(Fore.RED + Style.DIM + "| MODE | - IMPOSSIBLE")

                print(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + Spacer)

                print(Day)
                print(Period)

                print(Spacer)
                print(C1, " C1s")
                print(C2, " C2s")
                print(C3, " C3s")
                print(C4, " C4s")
                print(Spacer)
                if Dev:
                    print("RELEASE -", VERSION, " - DEVELOPER MODE / NOT LEGITIMATE RUN")
                else:
                    print("RELEASE -", VERSION)
                print(Spacer)

                # STALL
                stall = input(">>>")

                for x in range(1, SCREEN_HEIGHT):
                    print(" ")

                print(Spacer)
                print(" ")
                print("Do you want to play again?")
                print(" ")
                print(Spacer)
                print("| 1 | - Yes")
                print("| 2 | - No")
                print(Spacer)
                Option = input(">>>")
                if Option == 1:
                    print("RESTARTING: PLEASE WAIT")
                    for x in range(1, 100):
                        print(" ")
                else:
                    Loop = False
                    print("EXITING: PLEASE WAIT")
                    for x in range(1, 100):
                        print(" ")

            # END OF DAY SCREEN
            if Period == "PERIOD 6":
                PopularityTempDisplay = (OldPopularity - Popularity) * -1
                FocusTempDisplay = (OldFocus - Focus) * -1
                HappinessTempDisplay = (OldHappiness - Happiness) * -1
                EnergyTempDisplay = (OldEnergy - Energy) * -1
                BatteryTempDisplay = (OldBattery - Battery) * -1
                PopularityTempDisplay = round(PopularityTempDisplay, 1)
                FocusTempDisplay = round(FocusTempDisplay, 1)
                HappinessTempDisplay = round(HappinessTempDisplay, 1)
                EnergyTempDisplay = round(EnergyTempDisplay, 1)
                Popularity = round(Popularity, 1)
                Focus = round(Focus, 1)
                Happiness = round(Happiness, 1)
                Energy = round(Energy, 1)
                Battery = round(Battery, 1)

                # Print
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")  # if you see this, have a good day
                print(Spacer)
                print(" ")
                print(Fore.LIGHTCYAN_EX + "DAY SUMMARY")
                print(" ")

                print(Fore.WHITE + Spacer)
                if PopularityTempDisplay < 0:
                    print(Fore.WHITE + "|" + str(OldPopularity))
                else:
                    print(Fore.WHITE + "|" + str(OldPopularity))

                if FocusTempDisplay < 0:
                    print(Fore.WHITE + "|" + str(OldFocus))
                else:
                    print(Fore.WHITE + "|" + str(OldFocus))

                if HappinessTempDisplay < 0:
                    print(Fore.WHITE + "|" + str(OldHappiness))
                else:
                    print(Fore.WHITE + "|" + str(OldHappiness))

                if EnergyTempDisplay < 0:
                    print(Fore.WHITE + "|" + str(OldEnergy))
                else:
                    print(Fore.WHITE + "|" + str(OldEnergy))

                if BatteryTempDisplay < 0:
                    print(Fore.WHITE + "|" + str(OldBattery))
                else:
                    print(Fore.WHITE + "|" + str(OldBattery))
                print(Fore.WHITE + Spacer)

                time.sleep(1)
                stall = input(">>>")

                for x in range(1, SCREEN_HEIGHT):
                    print(" ")

                print(Spacer)
                print(" ")
                print(Fore.LIGHTCYAN_EX + "DAY SUMMARY")
                print(" ")
                print(Fore.WHITE + Spacer)
                if PopularityTempDisplay < 0:
                    print(Fore.LIGHTRED_EX + "|" + Fore.WHITE + str(OldPopularity) + Fore.LIGHTRED_EX + "   -", PopularityTempDisplay * -1)
                elif PopularityTempDisplay == 0.0:
                    print(Fore.WHITE + "|" + Fore.WHITE + str(OldPopularity) + Fore.WHITE + "    ", "0.0")
                else:
                    print(Fore.LIGHTGREEN_EX + "|" + Fore.WHITE + str(OldPopularity) + Fore.LIGHTGREEN_EX + "   +", PopularityTempDisplay)

                if FocusTempDisplay < 0:
                    print(Fore.LIGHTRED_EX + "|" + Fore.WHITE + str(OldFocus) + Fore.LIGHTRED_EX + "   -", FocusTempDisplay * -1)
                elif FocusTempDisplay == 0:
                    print(Fore.WHITE + "|" + Fore.WHITE + str(OldFocus) + Fore.WHITE + "    ", "0.0")
                else:
                    print(Fore.LIGHTGREEN_EX + "|" + Fore.WHITE + str(OldFocus) + Fore.LIGHTGREEN_EX + "   +", FocusTempDisplay)

                if HappinessTempDisplay < 0:
                    print(Fore.LIGHTRED_EX + "|" + Fore.WHITE + str(OldHappiness) + Fore.LIGHTRED_EX + "   -", HappinessTempDisplay * -1)
                elif HappinessTempDisplay < 0:
                    print(Fore.WHITE + "|" + Fore.WHITE + str(OldHappiness) + Fore.WHITE + "    ", "0.0")
                else:
                    print(Fore.LIGHTGREEN_EX + "|" + Fore.WHITE + str(OldHappiness) + Fore.LIGHTGREEN_EX + "   +", HappinessTempDisplay)

                if EnergyTempDisplay < 0:
                    print(Fore.LIGHTRED_EX + "|" + Fore.WHITE + str(OldEnergy) + Fore.LIGHTRED_EX + "   -", EnergyTempDisplay * -1)
                elif EnergyTempDisplay < 0:
                    print(Fore.WHITE + "|" + Fore.WHITE + str(OldEnergy) + Fore.WHITE + "    ", "0.0")
                else:
                    print(Fore.LIGHTGREEN_EX + "|" + Fore.WHITE + str(OldEnergy) + Fore.LIGHTGREEN_EX + "   +", EnergyTempDisplay)

                if BatteryTempDisplay < 0:
                    print(Fore.LIGHTRED_EX + "|" + Fore.WHITE + str(OldBattery) + Fore.LIGHTRED_EX + "   -", BatteryTempDisplay * -1)
                elif BatteryTempDisplay < 0:
                    print(Fore.WHITE + "|" + Fore.WHITE + str(OldBattery) + Fore.WHITE + "    ", "0.0")
                else:
                    print(Fore.LIGHTGREEN_EX + "|" + Fore.WHITE + str(OldBattery) + Fore.LIGHTGREEN_EX + "   +", BatteryTempDisplay)
                print(Fore.WHITE + Spacer)

                time.sleep(1)
                stall = input(">>>")

                for x in range(1, SCREEN_HEIGHT):
                    print(" ")

                print(Spacer)
                print(" ")
                print(Fore.LIGHTCYAN_EX + "DAY SUMMARY")
                print(" ")
                print(Fore.WHITE + Spacer)
                if PopularityTempDisplay < 0:
                    print(Fore.RED + "|" + str(Popularity))
                else:
                    print(Fore.GREEN + "|" + str(Popularity))

                if FocusTempDisplay < 0:
                    print(Fore.RED + "|" + str(Focus))
                else:
                    print(Fore.GREEN + "|" + str(Focus))

                if HappinessTempDisplay < 0:
                    print(Fore.RED + "|" + str(Happiness))
                else:
                    print(Fore.GREEN + "|" + str(Happiness))

                if EnergyTempDisplay < 0:
                    print(Fore.RED + "|" + str(Energy))
                else:
                    print(Fore.GREEN + "|" + str(Energy))

                if BatteryTempDisplay < 0:
                    print(Fore.RED + "|" + str(Battery))
                else:
                    print(Fore.GREEN + "|" + str(Battery))
                print(Fore.WHITE + Spacer)

                time.sleep(1)
                stall = input(">>>")

                for x in range(1, SCREEN_HEIGHT):
                    print(" ")

                print(Spacer)
                print(" ")
                print(Fore.LIGHTCYAN_EX + "DAY SUMMARY")
                print(" ")
                print(Fore.WHITE + Spacer)
                if PopularityTempDisplay < 0:
                    print(Fore.RED + "|" + str(Popularity))
                else:
                    print(Fore.GREEN + "|" + str(Popularity))

                if FocusTempDisplay < 0:
                    print(Fore.RED + "|" + str(Focus))
                else:
                    print(Fore.GREEN + "|" + str(Focus))

                if HappinessTempDisplay < 0:
                    print(Fore.RED + "|" + str(Happiness))
                else:
                    print(Fore.GREEN + "|" + str(Happiness))

                if EnergyTempDisplay < 0:
                    print(Fore.RED + "|" + str(Energy))
                else:
                    print(Fore.GREEN + "|" + str(Energy))

                BatteryTempDisplay1 = random.randint(4, 46)
                if BatteryTempDisplay < 0:
                    BatteryTempDisplay = random.randint(4, 46)
                    print(Fore.RED + "|" + str(Battery) + Fore.GREEN + "    +", BatteryTempDisplay1)
                else:
                    BatteryTempDisplay = random.randint(4, 46)
                    print(Fore.GREEN + "|" + str(Battery) + Fore.GREEN + "    +", BatteryTempDisplay1)

                time.sleep(1)
                stall = input(">>>")

                for x in range(1, SCREEN_HEIGHT):
                    print(" ")

                print(Spacer)
                print(" ")
                print(Fore.LIGHTCYAN_EX + "DAY SUMMARY")
                print(" ")
                print(Fore.WHITE + Spacer)
                if PopularityTempDisplay < 0:
                    print(Fore.RED + "|" + str(Popularity))
                else:
                    print(Fore.GREEN + "|" + str(Popularity))

                if FocusTempDisplay < 0:
                    print(Fore.RED + "|" + str(Focus))
                else:
                    print(Fore.GREEN + "|" + str(Focus))

                if HappinessTempDisplay < 0:
                    print(Fore.RED + "|" + str(Happiness))
                else:
                    print(Fore.GREEN + "|" + str(Happiness))

                Battery = Battery + BatteryTempDisplay

                if Battery > 100:
                    Battery = 100

                Battery = round(Battery)

                if Battery < OldBattery:
                    print(Fore.RED + "|" + str(Battery) + Fore.GREEN + "    +", BatteryTempDisplay1)
                else:
                    print(Fore.GREEN + "|" + str(Battery) + Fore.GREEN + "    +", BatteryTempDisplay1)

                print(Fore.WHITE + Spacer)

                stall = input(">>>")
                for x in range(1, SCREEN_HEIGHT):
                    print(" ")

            # Set Time
            Time = Time + 1
            if Period == "PERIOD 1":
                Period = "PERIOD 2"
            elif Period == "PERIOD 2":
                Period = "BREAK"
            elif Period == "BREAK":
                Period = "PERIOD 3"
            elif Period == "PERIOD 3":
                Period = "PERIOD 4"
            elif Period == "PERIOD 4":
                Period = "LUNCH"
            elif Period == "LUNCH":
                Period = "PERIOD 5"
            elif Period == "PERIOD 5":
                Period = "PERIOD 6"
            elif Period == "PERIOD 6":
                Period = "PERIOD 1"

if True:
    print("See you next time!")
    stall = input(">>>")
