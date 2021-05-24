import sqlite3
import utils.db_utils as db_utils


class DBDriver:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect("{}.sqlite".format(dbname))

    def authenticate(self, username, password):
        return db_utils.authenticate(self.conn, username, password)

    def is_username_exist(self, username):
        return db_utils.is_username_exist(self.conn, username)

    def update(self, column, column_value, key, key_value):
        db_utils.update(self.conn, column, column_value, key, key_value)

    def insert_user(self, username, password):
        db_utils.insert_user(self.conn, username, password)
