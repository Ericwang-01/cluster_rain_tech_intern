# encoding:utf-8
def get_all_users_age():
    all_users = 10000000
    for id in all_users:
        user_obj = access_db_to_get_users_by_id(id)
        yield user.name, user.age

for user_name, user_age in gat_all_users_age():
    print(user_age, user_name)
