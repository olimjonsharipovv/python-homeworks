
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}!")
    
    def eat(self, food):
        print(f"{self.name} is eating {food}.")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "cow", "moo")
        self.milk_production = 0
    
    def produce_milk(self):
        self.milk_production += 5
        print(f"{self.name} produced 5 liters of milk!")

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "chicken", "cluck")
        self.eggs_laid = 0
    
    def lay_egg(self):
        self.eggs_laid += 1
        print(f"{self.name} laid an egg!")

class Pig(Animal):
    def __init__(self, name):
        super().__init__(name, "pig", "oink")
        self.mud_bath_count = 0
    
    def take_mud_bath(self):
        self.mud_bath_count += 1
        print(f"{self.name} is happily rolling in the mud!")

class Farm:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def morning_routine(self):
        print("\nFarm Morning Routine:")
        for animal in self.animals:
            animal.make_sound()
            if isinstance(animal, Cow):
                animal.produce_milk()
            elif isinstance(animal, Chicken):
                animal.lay_egg()
            elif isinstance(animal, Pig):
                animal.take_mud_bath()
            animal.eat("feed")

my_farm = Farm()
my_farm.add_animal(Cow("Moshvoy"))
my_farm.add_animal(Chicken("Klocky"))
my_farm.add_animal(Pig("Benom"))

my_farm.morning_routine()






























