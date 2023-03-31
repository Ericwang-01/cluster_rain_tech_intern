# encoding:utf-8
'''
-用户模块
-完成注册、登录、登出、查询余额、充值、支付订单功能

'''
import pymysql
from config.config import *
from database_connection import DatabaseConnection


class User(object):

    def __init__(self):
        self.db = None
        self.current_user = None

    def create_conn(self):
        self.db = pymysql.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database=DATABASE,
        )

    def reg(self):
        self.create_conn()
        name = input("请输入您的姓名：")
        tel = input("请输入您的电话：")
        password = input("请输入您的密码：")
        sql = """INSERT INTO user(name, tel, password, balance) VALUES (%s, %s, %s, 0);"""
        with self.db.cursor() as cur:
            cur.execute(sql, (name, tel, password))
            self.db.commit()
        print("注册成功！")

    def login(self):
        self.create_conn()
        tel = input("请输入您的电话：")
        password = input("请输入您的密码：")
        sql = """SELECT id FROM user WHERE tel = %s and password = %s"""
        with self.db.cursor() as cur:
            cur.execute(sql, (tel, password))
            id = cur.fetchone()[0]
        self.current_user = id
        print(f"登录成功，当前用户id为{self.current_user}")

    def logout(self):
        if self.current_user:
            self.current_user = None
            print("退出成功")
        else:
            print("请先登录")

    def check_balance(self):
        self.create_conn()
        if self.current_user:
            sql = """SELECT balance FROM user WHERE id= %s"""
            with self.db.cursor() as cur:
                cur.execute(sql, (self.current_user, ))
                balance = cur.fetchone()[0]
                print(f"余额为:{balance}")
        else:
            print("请先登录")

    def top_up(self):
        self.create_conn()
        if self.current_user:
            money = input("请输入充值金额：")
            sql = """UPDATE user SET balance = balance + %s  WHERE id = %s """
            with self.db.cursor() as cur:
                cur.execute(sql, (money, self.current_user))
                self.db.commit()
                cur.execute("SELECT balance FROM user WHERE id = %s", (self.current_user,))
                balance = cur.fetchone()[0]
                print("充值成功，余额为：", balance)
        else:
            print("请先登录")


myuser = User()
myuser.login()
myuser.top_up()