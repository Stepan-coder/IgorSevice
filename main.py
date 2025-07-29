from user import User
from enums import Male
from pets.animals import *


user = User(name="Igor", age=24, male=Male.MAN)

user.add_pet(pet=Cat(name="Me", age=5, pet_type=PetType.DOMESTIC))
user.add_pet(pet=Dog(name="Me1", age=5, pet_type=PetType.DOMESTIC))
user.add_pet(pet=Horse(name="Me2", age=5, pet_type=PetType.WILD))

print(user.to_dict())