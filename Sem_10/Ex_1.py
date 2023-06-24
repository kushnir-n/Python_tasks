# Задание №5
# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

# Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него. Убедитесь, что в созданные ранее классы внесены правки.

# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

#задание 6

class Animal:
    def __init__(self, name: str, animal_type: str):
        self.name = name
        self.animal_type = animal_type
    
    def make_voice():
        print(f"I`m animal. Just animal")

    def get_animal_type(self):
        print(f"Animal type: {self.animal_type}")


#задание 5
class Cow(Animal):
    def __init__(self, milky_level, *args):
        self._milky_level = milky_level
        super().__init__(*args)
    
    def make_voice(self):
        print(f"Mooooooo! I`m cow {self.name}, my milky level is {self._milky_level}")
    
        
class Bird(Animal):
    def __init__(self, tweet_level, *args):
        self._tweet_level = tweet_level
        super().__init__(*args)

    def make_voice(self):
        print(f"Chirik!!! I`m {self.name}")


class Fish(Animal):
    def __init__(self, sea_level, *args):
        self._sea_level = sea_level
        super().__init__(*args)
        
    def make_voice(self):
        print(f"Buuulk... I`m fish {self.name}")

# Доработаем задачи 5-6. Создайте класс-фабрику.
class AnimalFabric:
    def make_animal(self, animal_type: str, *args):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args)

    def _get_maker(self, animal_type: str):
        types = {"cow": Cow, "bird": Bird, "fish": Fish}
        return types[animal_type.lower()]

if __name__ == '__main__':
    
    Cow1 = Cow(10, "Burenka", "cow")
    Cow1.make_voice()
    print(f'{Cow1.name} milky_level = {Cow1._milky_level}')
    Cow1.get_animal_type()
    
    Bird1 = Bird(55, "Maik", "bird")
    Bird1.make_voice()
    print(f'Bird1 tweet_level = {Bird1._tweet_level}')
    Bird1.get_animal_type()

    Fish1 = Fish(100, "Dolly", "fish")
    Fish1.make_voice()
    print(f'Fish1 sea_level = {Fish1._sea_level}')
    Fish1.get_animal_type()

    print(f"\n\nTest Animal fabric:\n")

    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("cow", 55, "Mura", "Dark")
    animal_from_fabric.make_voice()
    animal_from_fabric.get_animal_type()