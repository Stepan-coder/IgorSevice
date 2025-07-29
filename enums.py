import enum # <-- Импортируем библиотеку. Библиотека - написанный сообществом Python. Точно такой же, какой пишем сами


class Male(enum.Enum): # <-- Тут пишем в скобочках enum.Enum, на следующем занятии разберем
    MAN = 'man' # <-- создаем "переменные" и присваиваем им значения
    WOMEN = 'women'
    ATHER = 'ather'


class PetType(enum.Enum):
    WILD = "wild"
    DOMESTIC = "domestic"