
import configparser
# Setup
config = configparser.ConfigParser()
config.read("Rewrite/Scenarios/Test.ini")

print(config.sections())

# Read
print(config.get("Main", "Question"))