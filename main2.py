# class UserInf:
#     def __init__(self):
#         self._name = 'Igor'
#         self._age = 23
#         self._male = 'man'
#
#     @property
#     def name(self) -> str:
#         return self._name
#
#     @name.setter
#     def name(self, data: str):
#         if not isinstance(data, str):
#             raise Exception("Не имя")
#         self._name = data
#
#
#     @property
#     def age(self) -> int:
#         return self._age
#
#     @age.setter
#     def age(self, age) -> None:
#         if age < 0:
#             print('Некорректный возраст')
#         elif age > 100:
#             print('Некорректный возраст')
#         self._age = age
#
#     @property
#     def male(self) -> str:
#         return self._male
#
#     @male.setter
#     def male(self, male: str):
#         if not isinstance(male, str):
#             raise Exception("Не пол")
#         if male != "m" and male != "w":
#             raise ValueError("Недопустимое значение")
#         self._male = male
#
#     def smt(self, data):
#         return data
#
# user = UserInf()
# user.male = 'ew'
# print(user.male)
# print(user.smt(12))