# import math
# import enum # <-- Импортируем библиотеку. Библиотека - написанный сообществом Python. Точно такой же, какой пишем сами
#
#
# class Male(enum.Enum): # <-- Тут пишем в скобочках enum.Enum, на следующем занятии разберем
#     MAN = 'man' # <-- создаем "переменные" и присваиваем им значения
#     WOMEN = 'women'
#     ATHER = 'ather'
#
#
# #
# class User:
#     def __init__(self, male: Male):
#         self._male = male
#
#     @property
#     def male(self) -> Male:
#         return self._male
#
#     @male.setter
#     def male(self, male: Male):
#         if not isinstance(male, Male):
#             raise Exception("Не число")
#         self._male = male
#
#     def action1(self):
#         pass
#
#
# class User1:
#     def __init__(self, male: Male):
#         self.male = male
#
#     @property
#     def male(self) -> Male:
#         return self._male
#
#     @male.setter
#     def male(self, male: Male):
#         if not isinstance(male, Male):
#             raise Exception("Не число")
#         self._male = male
#
#     def action2(self):
#         return 45 + 55
#
#
# class User2:
#     def __init__(self, male: Male):
#         self._male = male
#
#     @property
#     def male(self) -> Male:
#         return self._male
#
#     @male.setter
#     def male(self, male: Male):
#         if not isinstance(male, Male):
#             raise Exception("Не число")
#         self._male = male
#
#     def action3(self):
#         return 45 * 55
#
#
# user = User(male=Male.MAN)
# user.action1()
#
# user1 = User1(male=Male.WOMEN)
# user2 = User2(male=Male.ATHER)
# # user.male = Male.MAN
#
# print(user.male)
# print(user1.male)
# print(user2.male)
#
#
#
#
#
#
#
