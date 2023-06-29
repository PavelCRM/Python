class Animal:
    def __init__(self, name):
        self.name = name

    def specific_info(self):
        pass  # Метод будет переопределен в каждом подклассе


class Fish(Animal):
    def specific_info(self):
        print(f"{self.name} - это рыба. Они обычно живут в воде и имеют жаберные дыхательные органы.")


class Bird(Animal):
    def specific_info(self):
        print(f"{self.name} - это птица. Они обычно имеют оперение, крылья и клюв.")


class Lizard(Animal):
    def specific_info(self):
        print(f"{self.name} - это ящерица. Они обычно имеют чешую, хвост и четыре ноги.")


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "Fish":
            return Fish(name)
        elif animal_type == "Bird":
            return Bird(name)
        elif animal_type == "Lizard":
            return Lizard(name)
        else:
            raise ValueError("Invalid animal type.")


#Использования класса-фабрики:
animal1 = AnimalFactory.create_animal("Fish", "Золотая рыбка")
animal1.specific_info()  # Выведет: Золотая рыбка - это рыба. Они обычно живут в воде и имеют жаберные дыхательные органы.

animal2 = AnimalFactory.create_animal("Bird", "Синица")
animal2.specific_info()  # Выведет: Синица - это птица. Они обычно имеют оперение, крылья и клюв.

animal3 = AnimalFactory.create_animal("Lizard", "Игуана")
animal3.specific_info()  # Выведет: Игуана - это ящерица. Они обычно имеют чешую, хвост и четыре ноги.
