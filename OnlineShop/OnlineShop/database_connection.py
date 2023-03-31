import pymysql


# 使用单例设计模式，创建一个数据库链接类
class DatabaseConnection(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DatabaseConnection, cls).__new__(cls)

        return cls.__instance

    @staticmethod
    def get_connection(dsn):
        mydb = pymysql.connect(**dsn)
        return mydb
