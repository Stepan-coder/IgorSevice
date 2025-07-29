from enums import PetType

class Pet:
    def __init__(self, name: str, age: int, pet_type: PetType):
        self.age = age
        self.name = name
        self.pet_type = pet_type

    def __str__(self):
        return f"Питомца зовут - {self._name}"

    def __repr__(self): # TODO дописать по нормальному
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

    # def to_dict(self): #TODO доработать, как сделано в User
    #     pass