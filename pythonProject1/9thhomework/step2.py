class Animal:
    # 类属性初始化为 None
    name = None
    age = None
    species = None
    color = None
    is_domestic = None
    weight = None
    height = None
    diet = None
    habitat = None
    lifespan = None
    def say_hi(self):
        print(self.name)
    # @classmethod
    # def describe(cls):
    #     return (f"Name: {cls.name}, Age: {cls.age}, Species: {cls.species}, Color: {cls.color}, "
    #             f"Domestic: {cls.is_domestic}, Weight: {cls.weight}, Height: {cls.height}, "
    #             f"Diet: {cls.diet}, Habitat: {cls.habitat}, Lifespan: {cls.lifespan}")
    # def get_description(self):
    #     return (f"{self.name} is a {self.age}-year-old {self.species} with {self.color} fur. "
    #             f"Weight: {self.weight}kg, Height: {self.height}m, Diet: {self.diet}, "
    #             f"Habitat: {self.habitat}, Domestic: {self.is_domestic}, Lifespan: {self.lifespan} years.")
animal = Animal()
animal.name = "Tiger"
animal.age = 4
animal.species = "Panthera tigris"
animal.color = "Orange with black stripes"
animal.is_domestic = False
animal.weight = 220
animal.height = 1.1
animal.diet = "Carnivore"
animal.habitat = "Forests and grasslands"
animal.lifespan = 15
print(animal.name, animal.age, animal.species, animal.color, animal.is_domestic,)

