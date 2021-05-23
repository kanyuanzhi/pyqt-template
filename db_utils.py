import sqlite3


def connect_database():
    conn = sqlite3.connect('project.sqlite')
    return conn
