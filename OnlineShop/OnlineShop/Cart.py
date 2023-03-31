import pymysql
from config.config import config_info
from database_connection import DatabaseConnection
from item import Item

"""
写的代码太冗余，如何把多此使用的代码，封装到类中 如sql语句
"""


class Cart:
    connection = DatabaseConnection.get_connection(config_info)

    def __init__(self):
        self.items = {}


        self.total_price = 0

    def add_item(self, item, quantity):
        if quantity < 0:
            print("quantity can't zero value")
            return None
        if item.stock < quantity:
            print(f"Only {item.stock} units of '{item.name}' available in inventory.")
            return None
        print("看一眼字典里有啥", self.items)
        if item.name not in self.items:
            self.items[item.name] = {'item': item, 'quantity': quantity}
            # self.items字典里创建一个键值对：
            # Key为将来传入函数的商品实例的name属性，value是一个字典

            item.stock -= quantity

            sql = """UPDATE item SET stock = %s WHERE id = %s"""
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (item.stock, item.id))
                self.connection.commit()

        else:
            self.items[item.name]['quantity'] += quantity
            item.stock -= quantity

            connection = DatabaseConnection.get_connection(config_info)
            sql = """UPDATE item SET stock = %s WHERE id = %s"""
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (item.stock, item.id))
                self.connection.commit()

        self.total_price += item.price * quantity
        print(f"{quantity} units of '{item.name}' added to cart.")

    def remove_item(self, remove_item_name, remove_quantity):
        # 移出数量小于购物车中的数量
        if remove_item_name in self.items and self.items[remove_item_name]['quantity'] > remove_quantity:
            item = self.items[remove_item_name]['item']
            self.items[remove_item_name]['quantity'] -= remove_quantity
            item.stock += remove_quantity

            sql = """UPDATE item SET stock = %s WHERE id = %s"""
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (item.stock, item.id))
                self.connection.commit()

            self.total_price -= item.price * remove_quantity
            print(f"{remove_quantity} units of '{item.name}' removed from cart.")
        elif remove_item_name in self.items and self.items[remove_item_name]['quantity'] == remove_quantity:
            item = self.items[remove_item_name]['item']

            item.stock += remove_quantity

            sql = """UPDATE item SET stock = %s WHERE id = %s"""
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (item.stock, item.id))
                self.connection.commit()

            del self.items[remove_item_name]
            self.total_price -= item.price * remove_quantity
        elif remove_item_name in self.items and self.items[remove_item_name]['quantity'] < remove_quantity:
            item = self.items[remove_item_name]['item']
            print(f"Only {self.items[remove_item_name]['quantity']} units of '{item.name}' are in the cart.")
        else:
            print(f"No '{remove_item_name}' found in cart.")

    def checkout(self):
        if self.items:
            print("Ordered items:")
            for item_name in self.items:
                item = self.items[item_name]['item']
                quantity = self.items[item_name]['quantity']
                print(f"{item.name}: {quantity}")
            print(f"Total price: {self.total_price:.2f} yuan")
            # 改user指定用户的balance
            sql = """UPDATE user SET balance = %s WHERE id = %s"""
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (self.total_price, 3))
                self.connection.commit()
            # 清空items和total_price
            self.items.clear()
            self.total_price = 0
        else:
            print("There are no items in the cart.")

    def clear_cart(self):
        for item_name in self.items:
            item = self.items[item_name]['item']
            item.stock += self.items[item_name]['quantity']

            sql = """UPDATE item SET stock = %s WHERE id = %s"""
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (item.stock, item.id))
                self.connection.commit()

        self.items.clear()
        self.total_price = 0

    def show_cart(self):
        if self.items:
            print("Current cart items:")
            for item_name in self.items:
                item = self.items[item_name]['item']
                quantity = self.items[item_name]['quantity']
                print(f"{item.name}: {quantity}")
            print(f"Total price: {self.total_price:.2f} yuan")
        else:
            print("There are no items in the cart.")


if __name__ == '__main__':
    # 创建购物车
    my_cart = Cart()

    print("1.展示所有商品")
    print("-" * 20)
    print('ALL items in inventory:')
    Item.display_all_items()
    print("-" * 20)

    print("2.添加商品")
    p1 = Item.find_item(4)
    p2 = Item.find_item(5)

    my_cart.add_item(p1, 1)
    my_cart.add_item(p2, 2)
    my_cart.add_item(p2, 2)

    print("3.展示购物车内容")
    my_cart.show_cart()

    # 4.剔除商品
    print("4.删除商品")
    print("删除前字典", my_cart.items)
    my_cart.remove_item('Product3', 4)
    print(my_cart.items)

    print("5,结账")
    my_cart.checkout()
