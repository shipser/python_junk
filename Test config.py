#############
# Libs used #
#############

# Working with configuration files
import configparser




####################
# Start of project #
####################

Myconfig = configparser.ConfigParser() # Create Instance of configparser
Myconfig.read("config.ini") # Read The Config File

# Get the sections of the config and print them
sections = Myconfig.sections()
print(str(sections) + "\n\n")

# Get the keys of the config and print them
keys = Myconfig.options("Test_Section")
print(str(keys) + "\n")
keys2 = Myconfig.options("Test2")
print(str(keys2) + "\n\n")

# Get the values of the config and print them
Value = Myconfig.get("Test_Section", "drive")
print(str(Value) + "\n")
Value2 = Myconfig.get("Test_Section", "drive2")
print(str(Value2) + "\n")
Value3 = Myconfig.get("Test2", "Folder")
print(str(Value3) + "\n")
Value4 = Myconfig.get("Test2", "folder2")
print(str(Value4) + "\n\n")