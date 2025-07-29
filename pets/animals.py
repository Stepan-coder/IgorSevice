from pets.pet import Pet
from enums import PetType
from typing import Any, Dict

class Cat(Pet):
    def __init__(self, name: str, age: int, pet_type: PetType):
        super().__init__(name=name, age=age, pet_type=pet_type)

    def do_action(self):
        pass

    def to_dict(self) -> Dict[str, Any]: #TODO доработать, как сделано в User
        return {"some": 123}


class Horse(Pet):
    def __init__(self, name: str, age: int, pet_type: PetType):
        super().__init__(name=name, age=age, pet_type=pet_type)

    def do_action(self):
        pass

    def to_dict(self) -> Dict[str, Any]:  # TODO доработать, как сделано в User
        return {"some": 123}


class Dog(Pet):
    def __init__(self, name: str, age: int, pet_type: PetType):
        super().__init__(name=name, age=age, pet_type=pet_type)

    def do_action(self):
        pass

    def to_dict(self) -> Dict[str, Any]:  # TODO доработать, как сделано в User
        return {"some": 123}




