# encoding:utf-8
"""
-元组取值
-注意变量的数据类型，数字也有可能是字符串
-插入和更新
-整体运行的逻辑， while True 是个死循环， 链接数据库只链接一次
"""
from account import Account
import random
import pymysql
from config import *


class self(object):
    #current_user = None  # cls :  classmethod  or self # 类变量

    def __init__(self):  # self 实例变量
        self.account_lst = []
        self.db = None
        self.current_user = None  #  不要用全局变量，， 将变量定义到init方法里，使用self打点调用

    @staticmethod  # 静态函数
    def b(abc):
        pass
        print(abc)

    @classmethod  # 类函数
    def a(cls):
        cls.current_user
        pass

    def create_conn(self):  # 实例函数
        self.db = pymysql.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database=DB,
        )

    def run(self):
        self.create_conn()
        while True:
            self.get_menu()
            num = int(input("请输入功能序号:"))
            if num == 1:
                self.register()
            elif num == 2:
                self.login()
            elif num == 3:
                self.change_password()
            elif num == 4:
                self.check_balance()
            elif num == 5:
                self.top_up()
            elif num == 6:
                self.draw()
            elif num == 7:
                self.log_out()
                break
            else:
                print("输入的序号有误")

    @staticmethod
    def get_menu():
        print("-" * 10)
        print("请选择您需要的功能:")
        print("1.注册账号")
        print("2.登录")
        print("3.修改密码")
        print("4.查询余额")
        print("5.存钱")
        print("6.取钱")
        print("7.退出")
        print("-" * 10)

    def register(self):
        account = ""
        for i in range(10):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            account += ch
        print(f"您的账号是:{account}")
        password = input("请输入密码：")
        if len(password) > 5:
            print("注册成功")
            sql = """INSERT INTO user (account, password, create_time) VALUES (%s, %s, NOW())"""
            with self.db.cursor() as cur:  # 向user表里写 账户和密码
                cur.execute(sql, (account, password))
                self.db.commit()
            sql2 = """SELECT id FROM user where account = %s"""
            with self.db.cursor() as cur:  # 依据密码在user表里查id ，只知道账户和密码，妥协一下假设随机生成的十位账号具有唯一性
                cur.execute(sql2, (account,))
                userid = cur.fetchone()
            sql3 = """INSERT INTO money(user_id,balance) VALUES (%s, %s)"""
            with self.db.cursor() as cur:  # 这写了三个with，是否过于繁琐，如何优化
                cur.execute(sql3, (userid, 0))
                self.db.commit()
            print(f"您的账户是：{account},密码是：{password}，余额为0")
            print(self.account_lst)
        else:
            print("您输入的密码长度小于6位，请从新输入")

    def login(self):
        account = input("请输入账号：")
        password_input = input("请输入密码：")
        if self.current_user is not None:
            print("用户已存在")
            return None
        sql = f"""SELECT id,password FROM user WHERE account='{account}'"""
        with self.db.cursor() as cur:  # 创建游标
            cur.execute(sql)  # if records is null fetchone return None fetchall return []
            row = cur.fetchone()
        if row is None:
            print("用户不存在")
            return None
        user_id, password = row
        if password != password_input:
            print("密码错误")
            return None
        # login success
        self.current_user = user_id
        print("登录成功")

    def change_password(self):
        if self.current_user:
            new_password = input("请输入新密码：")
            if len(new_password) > 5:
                sql = """UPDATE user SET password = %s WHERE id = %s"""
                with self.db.cursor() as cur:
                    cur.execute(sql, (new_password, self.current_user))
                    self.db.commit()
                print("修改成功")
            else:
                print("您输入的密码长度小于6位，请从新输入")
        else:
            print("请先登录")

    def check_balance(self):
        if self.current_user is None:
            print("请先登录")
            return None
        sql = """SELECT balance FROM money WHERE user_id = %s"""
        with self.db.cursor() as cur:
            cur.execute(sql, (self.current_user))
            balance = cur.fetchone()
            print(f"您的余额为{balance[0]}")
    def top_up(self):
        if self.current_user:
            money = input("请输入存入金额：")
            if money[-2:] == '00' and len(money) > 2:
                sql1 = """SELECT balance FROM money WHERE user_id = %s"""
                with self.db.cursor() as cur:
                    cur.execute(sql1, (self.current_user,))
                    balance =  cur.fetchone()
                sql2 = """UPDATE money SET balance = %s WHERE user_id = %s"""
                with self.db.cursor() as cur:
                    cur.execute(sql2, (int(money)+balance[0], self.current_user))
                    self.db.commit()
                print(f"存款成功！")
            else:
                print("无法存入小于零的金额")
        else:
            print("请先登录")

    def draw(self):
        if self.current_user:
            money = input("请输入取出金额：")
            if money[-2:] == '00' and len(money) > 2:
                sql1 = """SELECT balance FROM money WHERE user_id = %s"""
                with self.db.cursor() as cur:
                    cur.execute(sql1, (self.current_user,))
                    balance = cur.fetchone()
                if balance[0] > int(money):
                    sql2 = """UPDATE money SET balance = %s WHERE user_id = %s"""
                    with self.db.cursor() as cur:
                        cur.execute(sql2, (balance[0]-int(money), self.current_user))
                        self.db.commit()
                    print(f"取款成功！")
                else:
                    print("您的余额不足")
            else:
                print("输入金额有误")
        else:
            print("您尚未登录！")

    def log_out(self):
        # global current_user
        if self.current_user:
            self.db.close()
            self.current_user = None
            print("退出成功")
        else:
            print("您尚未登录！")

    def load_account(self):
        # print("从数据库里加载账户信息")
        # try:
        #     f = open('data.txt', 'r')
        # except:
        #     f = open('data.txt', 'w')
        # else:
        #     data = f.read()
        #     new_lst = eval(data)
        #     self.account_lst = [Account(i['account'], i['password'], i['balance']) for i in new_lst]
        # finally:
        #     f.close()
        global cursor
        global db

        db = pymysql.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database=DB,
        )
        cursor = db.cursor()
        sql = "select * from user, money where user.id = money.user_id"
        try:
            cursor.execute(sql)
            self.account_lst = cursor.fetchall()
            print(self.account_lst)
        except Exception:
            db.rollback()


# print(self.current_user)
