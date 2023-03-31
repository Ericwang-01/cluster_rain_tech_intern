# # encoding:utf-8
# __all__ = ['USER', 'PASSWORD', 'HOST', 'DATABASE']
#
# USER = "root"
# PASSWORD = "123456"
# HOST = "localhost"
# DATABASE = "wang"
# 单例


config_info = {
    "user": "root",
    "password": "123456",
    "host": "localhost",
    "database": "wang"
}


    # with DatabaseConnection.get_connection(config_info).cursor() as cursor:
    #     cursor.execute("SELECT * FROM item")
    #     data = cursor.fetchall()
    # print(data)

