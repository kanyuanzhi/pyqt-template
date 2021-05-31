def authenticate(conn, username, password) -> (bool, str):
    """
    登录验证函数
    确认用户名的真实密码与输入密码是否一致
    Args:
        conn: 数据库连接
        username: 用户名
        password: 密码

    Returns:
        success: 验证成功与否
        message: 验证结果提示信息

    """
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


def is_username_exist(conn, username) -> bool:
    """
    确认用户名是否存在
    Args:
        conn: 数据库连接
        username: 用户名

    Returns:
        is_exist: 用户名是否存在
    """
    sql_str = "SELECT username FROM user WHERE username='{}'".format(username)
    cursor = conn.execute(sql_str)
    row = cursor.fetchone()
    if row is None:
        # 用户名不存在
        cursor.close()
        return False
    else:
        # 用户名存在
        cursor.close()
        return True


def update(conn, column, column_value, key, key_value):
    """
    数据库更新函数
    更新数据库中的一条记录中的某一列值
    Args:
        conn: 数据库连接
        column: 待更新列
        column_value: 待更新列值
        key: 键名，依据该键找到待更新记录
        key_value: 键值

    Returns:

    """
    sql_str = "UPDATE user SET {}='{}' WHERE {}='{}'".format(column, column_value, key, key_value)
    conn.execute(sql_str)
    conn.commit()


def insert_user(conn, username, password):
    """
    插入用户函数
    新增一条用户信息
    Args:
        conn: 数据库连接
        username: 用户名
        password: 密码

    Returns:

    """
    sql_str = "INSERT INTO user (username, password) VALUES ('{}', '{}')".format(username, password)
    conn.execute(sql_str)
    conn.commit()
