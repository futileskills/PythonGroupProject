# Test file for using figlet within a python script.
# found a package called pyfiglet. This is just for me to mess around and see if I want to use in the project

# Import figlet from the python package for it
from pyfiglet import Figlet

# Defining figlet and a text object to call/use it later
figlet = Figlet()

# Using it within a print statment
print(figlet.renderText("This is a test:"))
print(figlet.renderText("PyFiglet package to allow testing. I have no idea what the hell I'm doing."))
