#
# File responsible to database communication to the liked songs table
#   liked songs table has only one column called path
#   all files in this
# @TODO TEST THIS CODE
import sqlite3 as sq


class LikedSongs:

    def __init__(self):
        # If I ever add more tables I need to extract these to a higher scope.
        self.con = sq.connect('DailyWallpaper.db')
        self.cur = self.con.cursor()
        return

    # get all the liked songs from the liked songs table.
    def get_all_liked_songs(self):
        query = "SELECT * FROM LikedSongs"
        self.cur.execute(query)
        paths = self.cur.fetchall()
        return paths

    # insert a liked song based on its path.
    def insert_liked_song(self, path):
        insert = f"INSERT INTO LikedSongs VALUES ('{path}')"
        self.cur.execute(insert)
        self.con.commit()
        return

    # removes the liked songs from the database by it's path.
    def remove_liked_song(self, path):
        delete = f"DELETE FROM LikedSongs WHERE path='{path}'"
        self.cur.execute(delete)
        self.con.commit()
        return
