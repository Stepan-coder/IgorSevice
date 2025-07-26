import time

from psutil import users

from test_class import MyUser, User, CustomUser


# user = MyUser(name="Igor")
# custom_user = CustomUser(name="Stepan")

users = {}
print(users)

for index in range(5_000_000):
    name = f"Имя{index}"
    user = MyUser(id=index, name=name)
    users.append(user)

print(users)
t1 = time.time()
userid = int(input("Введите id"))
user_new_name = input("Введите id")
for my_user in users:
    # print(f"Проверяю пользователя: {my_user.id}")
    if my_user.id == userid:
        my_user.name = user_new_name
print("Время в миллисекундах", time.time() - t1)
print(users)

users[33].name = "Igor"

# users = {0: MyUser(id=0, name="Stepan0"),
#          1: MyUser(id=1, name="Stepan1"),
#          2: MyUser(id=2, name="Stepan2")}
#
# print(users)
#
# users[0].id += 5
# users[2].id += 7
#
# print(users)





