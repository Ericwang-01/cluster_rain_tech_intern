# encoding:utf-8
from config.config import config_info
from database_connection import DatabaseConnection
"""
提交订单 我的订单

"""
# 在Cart实例中的items属性中，拿到商品实例
# 总价
# 和商品库存
from Cart import Cart
my_cart = Cart()
my_cart.checkout()

