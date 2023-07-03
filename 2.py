# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра
# Добавить строки документации для классов
# Добавьте методы представления экземпляра для программиста и для пользователя.


class Archive:
    '''Класс Archive для хранения пары свойств'''

    numarch = []
    strarch = []

    def __init__(self, number, string):
        '''Инициализирует новый экземпляр класса Archive'''

        self.number = number
        self.string = string
        Archive.numarch.append(number)
        Archive.strarch.append(string)

    def __repr__(self):
        '''Представление экземпляра класса для программиста'''

        return f"Archive(number={self.number}, string='{self.string}')"

    def __str__(self):
        '''Представление экземпляра класса для пользователя'''

        return f"Число: {self.number}\nСтрока: {self.string}"

# Создание экземпляра класса Archive
archive1 = Archive(67, "Hi, welcome!")

# Вывод представления экземпляра для программиста
print(repr(archive1))

# Вывод представления экземпляра для пользователя
print(archive1)