# NameSpace for all interaction with windows
# For example Computer.set_desktop_background()
# or Computer.get_random_file_path():

import ctypes
import glob
import random
from datetime import datetime


class Computer:
    def __init__(self):
        return

    @staticmethod
    def set_desktop_background(picture_file_path):
        ctypes.windll.user32.SystemParametersInfoA(20, 0, picture_file_path.encode("us-ascii"), 2)
        return

    # Grabs a random file path from the wallpapers folder
    # TODO: make this grab a random file path from the internet?
    @staticmethod
    def get_random_file_path():
        file_paths = glob.glob(r"C:\Dev\DailyWallpaper\src\WallPapers\*")  # TODO: make this a relative path.
        file_count = len(file_paths)
        random.seed(datetime.now())
        random_number = random.randrange(file_count)

        if len(file_paths) == 0:
            raise Exception("There are no wallpapers to grab!")

        return file_paths[random_number]
