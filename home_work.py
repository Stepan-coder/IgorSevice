from typing import Optional

class Pet:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name

    def __str__(self):
        return f"Питомца зовут - {self._name}"

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int):
        if not isinstance(age, int):
            raise TypeError("Не число")
        if age < 0:
            raise ValueError('Некорректный возраст')
        elif age > 50:
            raise ValueError('Некорректный возраст')
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Не имя')
        self._name = name


class Cat(Pet):
    def __init__(self, name: str, age: int, work: str):
        super().__init__(name=name, age=age)

    def add_work(self):
        work = 'Спать'
        self.work = work


class Horse(Pet):
    def __init__(self, name: str, age: int, work: str):
        super().__init__(name=name, age=age)

    def add_work(self):
        work = 'Пахать'
        self.work = work


class Dog(Pet): # TODO доделать класс
    def __init__(self, name: str, age: int, work: str):
        super().__init__(name=name, age=age)

    def add_work(self):
        work = 'Гулять'
        self.work = work


