import sqlite3
import utils.db_utils as db_utils


class DBDriver:
    """
    sqlite数据库驱动类
    utils.db_utils封装了各种sql语句，此类通过调用utils.db_utils实现数据库操作的再封装，
    同时在初始化时即创建一个数据库连接，避免之后的数据库操作再次创建新连接，实现连接的复用，
    这种设计方式要注意避免在其他使用多线程或进程池实现的功能中并发操作数据库（本项目此需求）
    """

    def __init__(self, dbname):
        """
        初始化函数
        Args:
            dbname: 连接的数据库名称
        """
        self.dbname = dbname
        self.conn = sqlite3.connect("{}.sqlite".format(dbname))  # 创建数据库连接

    def authenticate(self, username, password) -> (bool, str):
        """
        登录验证函数
        Args:
            username: 用户名
            password: 密码

        Returns:

        """
        return db_utils.authenticate(self.conn, username, password)

    def is_username_exist(self, username) -> bool:
        """
        查询用户名是否存在函数
        Args:
            username: 用户名

        Returns:
            success: 验证成功与否
            message: 验证结果提示信息
        """
        return db_utils.is_username_exist(self.conn, username)

    def update(self, column, column_value, key, key_value):
        """
        数据库更新函数
        更新数据库中的一条记录中的某一列值
        Args:
            column: 待更新列
            column_value: 待更新列值
            key: 键名，依据该键找到待更新记录
            key_value: 键值

        Returns:

        """
        db_utils.update(self.conn, column, column_value, key, key_value)

    def insert_user(self, username, password):
        """
        插入用户函数
        新增一条用户信息
        Args:
            username: 用户名
            password: 密码

        Returns:

        """
        db_utils.insert_user(self.conn, username, password)
