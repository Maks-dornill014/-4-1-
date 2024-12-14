class Animal:
    def __init__(self, name, species, sound):
        
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        
        return f"{self.name} каже: {self.sound}"

    def __str__(self):
        
        return f"Ім'я: {self.name}, Вид: {self.species}"


class Dog(Animal):
    def __init__(self, name, breed):
       
        super().__init__(name, "Собака", "Гав-гав")
        self.breed = breed

    def fetch(self):
        
        return f"{self.name} приносить палку!"

    def __str__(self):
        
        return f"{super().__str__()}, Порода: {self.breed}"


class Cat(Animal):
    def __init__(self, name, color):
        
        super().__init__(name, "Кіт", "Мяу")
        self.color = color

    def climb(self):
       
        return f"{self.name} заліз на дерево!"

    def __str__(self):
        
        return f"{super().__str__()}, Колір шерсті: {self.color}"



if __name__ == "__main__":
    # Створення об'єктів
    dog = Dog("Рекс", "Лабрадор")
    cat = Cat("Мурка", "Руда")

    
    print(dog)
    print(cat)

   
    print(dog.make_sound())
    print(dog.fetch())
    print(cat.make_sound())
    print(cat.climb())
