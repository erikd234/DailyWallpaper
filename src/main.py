#
# Daily Wallpaper application
# By Erik Dahl - 2021-09-19
#  1. App set up to run as a chron job on windows PC to set a random daily wallpaper
#  2. For now the wallpaper will be a pre downloaded in a folder in the project directory and randomly selected.
#  3. In the future it may be downloaded from a website that has many wallpapers
#  4. I would like to have eventually have the ability to skip wallpapers easily accessible
#  5. I would like to create a simple GUI to configure the time and frequency for wallpaper switching

# Lets do an OOP project structure
# Objects in this program
# 1. Util
#    - Contains functions for helping out with random tasks like list/string manipulation
# 2. Computer
#   - Contains functions for interacting with the windowsdll/ computer. These are going to be the main functions
#     for changing the wallpaper, getting file paths.
# 3. Some separate part for a python GUI that changes some setting files for when to run the script?
#
#

from NameSpaces.computer import Computer


def main():
    file_path = Computer.get_random_file_path()
    Computer.set_desktop_background(file_path)
    return


main()
