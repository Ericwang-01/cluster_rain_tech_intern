# encoding:utf-8
import pymysql
from config.config import config_info
from database_connection import DatabaseConnection


class Item:
    def __init__(self, item_id, name, description, size, stock, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.size = size
        self.stock = stock
        self.price = price

    def add_item(self):
        db = DatabaseConnection.get_connection(config_info)

        try:
            with db.cursor() as cursor:
                sql = "INSERT INTO item (name, description, size, stock, price) VALUES (%s, %s, %s, %s, %s)"
                values = (self.name, self.description, self.size, self.stock, self.price)
                cursor.execute(sql, values)
                db.commit()
                print("Product added successfully.")
        finally:
            db.close()

    @staticmethod
    def find_item(item_id):
        bd = DatabaseConnection.get_connection(config_info)

        try:
            with bd.cursor() as cursor:
                sql = "SELECT * FROM item WHERE id = %s"
                value = (item_id,)
                cursor.execute(sql, value)
                result = cursor.fetchone()

            if result:
                return Item(*result)  # 用查询结果创建一个商品实例
            else:
                print(f"Item with ID {item_id} not found in inventory.")
                return None
        finally:

            bd.close()

    @staticmethod
    def display_all_items():
        db = DatabaseConnection.get_connection(config_info)

        try:
            with db.cursor() as cursor:
                sql = "SELECT * FROM item"
                cursor.execute(sql)
                result = cursor.fetchall()

                for row in result:
                    item = Item(*row)
                    print(
                        f"'Id':{item.item_id} {item.name}: {item.description} ({item.size}) - {item.price:.2f} yuan (stock: {item.stock})")
        finally:
            db.close()


if __name__ == '__main__':
    # 创建商品实例
    product4 = Item(16, 'Product4', 'There is a description for Product4.', 'L', 1, 99.9, )

    # # 添加商品到数据库
    # product4.add_item()
    #
    # #  根据商品id，查找该商品的所有信息
    # print(Item.find_item(16))
    # #  展示所有商品在购物车模块会用到
    # Item.display_all_items()
