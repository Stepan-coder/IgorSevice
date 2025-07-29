from pets.pet import Pet
from enums import Male, PetType
from pets.animals import Cat, Dog, Horse

from typing import Any, Dict, List



class User:
    def __init__(self, name: str, age: int, male: Male):
        self._pets = []
        self.name = name
        self.age = age
        self.male = male

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, data: str):
        if not isinstance(data, str):
            raise Exception("Не имя")
        self._name = data

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age) -> None:
        if age < 0:
            print('Некорректный возраст')
        elif age > 100:
            print('Некорректный возраст')
        self._age = age

    @property
    def male(self) -> Male:
        return self._male

    @male.setter
    def male(self, male: Any):
        if not isinstance(male, Male):
            raise TypeError(f"Expected type <Male>,  but got {type(male)}")
        self._male = male

    def add_pet(self, pet: Pet) -> None:
        if pet.pet_type == PetType.DOMESTIC:
            self._pets.append(pet)

    def to_dict(self) -> Dict[str, Any]:
        return {"name": self.name,
                "age": self.age,
                "male": self.male.value,
                "pets": [pet.to_dict() for pet in self._pets]}

