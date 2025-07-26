from typing import Optional # <--  из библиотеки typing импортируем "тип" Optional Он позволяет указать либо явный тип, либо None



class User: # <-- Класс "пользователь"
    # def __init__(self): <-- инициализация класса без входных аргументов User()
    # def __init__(self, name: Optional[str]):  <-- инициализация класса с обязательным аргументом User(name="Igor")
    def __init__(self, id: int, name: Optional[str] = None): # <-- инициализация класса с не обязательным аргументом User()[тогда по умолчанию name=None], User(name="Igor")[тогда name="Igor"]
        self.id = id
        self.name = name
        self._animals = []

    def __str__(self): # <-- встроенный метод, который позволяет представить класс в виде строки (Произвольное описание)
        return f"Пользователя зовут - {self.name}"

    def __repr__(self): # <-- встроенный метод, который позволяет представить класс в виде строки, зачастую выводят в виде Класс(параметр1=1, параметр2=2, ... параметрN=N)
        return f"User(id={self.id}, name={self.name})"

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    # def add_animal(self, animal: Animal):
        # self._animals.append(X)
        # pass


class MyUser(User):
    def __init__(self, id: int, name: str):
        super().__init__(id=id, name=name)



class CustomUser(User): # <-- Тут в скобочках пишем название "родительского" класса (Того, чьи переменные, сеттеры и геттеры, методы и т.д. будем "забирать")
    def __init__(self, id: int, name: str):
        super().__init__(id=id, name=name)

    def __repr__(self):
        return f"CustomUser(name={self.name})"

    def action(self):
        raise Exception(f"Ошибка в классе: {self.__repr__()}")

