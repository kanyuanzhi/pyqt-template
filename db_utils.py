import sqlite3


def connect_database():
    conn = sqlite3.connect('project.sqlite')
    return conn


def authenticate(conn, username, password):
    sql_str = "SELECT password FROM user WHERE username='{}'".format(username)
    cursor = conn.execute(sql_str)
    for row in cursor:
        if row[0] == password:
            cursor.close()
            return True, "验证成功！"
        else:
            cursor.close()
            return False, "密码错误！"
    cursor.close()
    return False, "用户不存在！"


def update(conn, column, column_value, key, key_value):
    sql_str = "UPDATE user SET {}='{}' WHERE {}='{}'".format(column, column_value, key, key_value)
    conn.execute(sql_str)
    conn.commit()
