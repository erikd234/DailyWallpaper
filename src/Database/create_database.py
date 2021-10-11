#
# File to create the database
# We want to have a tables for likes wallpapers
#  Likes wallpapers will look like this
# Headers: Picture path, screen saver name
# we want to hae a table for disliked wallpapers
#
import sqlite3 as sq


con = sq.connect('DailyWallpaper.db')

# create the sqlite cursor
cur = con.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS LikedSongs
                (path text) ''')

