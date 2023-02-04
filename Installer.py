
# Import
import os

# Default to default directory
os.chdir("")

# Take input
print("| [!] | INSTALLER/UNINSTALLER\n| [1] | - Install\n| [2] | - Update\n| [3] | - Uninstall")
Option = str(input("| [?] | >>>"))

# Install
if Option.lower() == "1":

    # Take input
    print("| [!] | INSTALLING\n| [1] | - Install\n| [2] | - Reinstall")
    Option = str(input("| [?] | >>>"))

    # Reinstall - Clear folder
    if Option.lower() == "1":
        os.system("rm -r Ruben-Sim")

    # Install

    # Take input
    print("| [!] | HOW TO INSTALL\n| [1] | - Git\n| [2] | - Github-cli")
    Option = str(input("| [?] | >>>"))

    # Clone

    # Git
    if Option.lower() == "1":
        print("Cloning From Github Via Git")
        os.system("git clone https://github.com/Herator2/Ruben-Sim.git")

    # Github-cli
    elif Option.lower() == "2":
        print("Cloning From Github Via Github-cli")
        os.system("gh repo clone Herator2/Ruben-Sim")

    # Specific branch git
    else:
        print("Cloning From Github Branch " + Option + " via git")
        os.system("git clone https://github.com/Herator2/Ruben-Sim.git --branch " + Option)

    # Generate config
    print("Making Config...")
    with open("Ruben-Sim/config.ini", "w+") as Config:
        Config.write("[Main]\n")
        Config.write("Linux = True\n")
        Config.write("Directory = Ruben-Sim/\n")
        print("Config created in home directory as config.ini:")
        print("[Main]\nLinux = True\nDirectory = Ruben-Sim\n")

    # Print
    print("Operation Finished")

# Uninstall
elif Option.lower() == "3":

    # Take comfirmation
    print("| [!] | CONFIRM  D E L E T I O N\n| [1] | - DOO IT!\n| [2] | - Go Back...")
    Option = str(input("| [?] | >>>"))

    if Option.lower() == "1":
        # Remove it
        os.system("rm -r Ruben-Sim")
