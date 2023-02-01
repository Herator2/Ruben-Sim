
# Import
import os

# DEVELOPER
Dev = True

# Code
if Dev:
    Branch = "Saving"
else:
    Branch = "main"

# Check for git
print("INSTALLATION REQUIRES GIT")
print("Press any key to start")
input(">>>")

# Install
try:

    # Reinstall
    print("SAY Y TWICE!")
    os.system("rm -r Ruben-Sim")

    # Github Clone
    print("Cloning From Github")
    os.system("git clone https://github.com/Herator2/Ruben-Sim.git --branch " + Branch)
    print("Cloned.")

    # Make config
    print("Making Config...")
    with open("Ruben-Sim/config.ini", "w+") as Config:
        Config.write("[Main]\n")
        Config.write("Linux = True\n")
        Config.write("Directory = Ruben-Sim/\n")
        print("Config created in home directory as config.ini:")
        print("[Main]\nLinux = True\nDirectory = Ruben-Sim\n")
    
    # Print
    print("Successful Install!")
    print("Use python3 Ruben-Sim/Main.py to start!")

# Installation error
except Exception as ErrorMSG:
    print("Exeption:", ErrorMSG, "occured")
    print("Please contact Herator2 or make a issue on the github repo")
    
