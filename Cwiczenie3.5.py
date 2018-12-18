class Animal:
    def __init__(self, homeothermic, adaptive):
        self.homeothermic = homeothermic
        self.adaptive = adaptive

    def __eq__(self, other):
        return self.homeothermic == other.homeothermic and self.adaptive == other.adaptive


animal1 = Animal("Tak", "Nie")
animal2 = Animal("Nie", "Tak")

print(animal1 == animal2)


class Mammal(Animal):
    def __init__(self, home, wild):
        self.home = home
        self.wild = wild

    def __eq__(self, other):
        return self.home == other.home and self.wild == other.wild


mammal1 = Mammal("Tak", "Nie")
mammal2 = Mammal("Tak", "Nie")

print(mammal1 == mammal2)


class Reptile(Animal):
    def __init__(self, water, land):
        self.water = water
        self.land = land

    def __eq__(self, other):
        return self.water == other.water and self.land == other.land


reptile1 = Reptile("Tak", "Nie")
reptile2 = Reptile("Nie", "Tak")

print(reptile1 == reptile2)


class Cat(Mammal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


cat1 = Cat("Miauczek", 3)
cat2 = Cat("Miauczek", 3)
cat3 = Cat("Pyszczek", 5)

print(cat1 == cat2)
print(cat2 == cat3)
print(cat1 == cat3)


class Dog(Mammal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


dog1 = Dog("Bari", 6)
dog2 = Dog("Pluto", 4)
dog3 = Dog("Pruto", 6)

print(dog1 == dog2)
print(dog2 == dog3)
print(dog1 == dog3)


class Lizard(Reptile):
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __eq__(self, other):
        return self.name == other.name and self.length == other.length


lizard1 = Lizard("Jaszczurka", "0,2m")
lizard2 = Lizard("Szczurka", "0,2m")
lizard3 = Lizard("Szczurka", "0,2m")

print(lizard1 == lizard2)
print(lizard2 == lizard3)
print(lizard1 == lizard3)


class Crocodile(Reptile):
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __eq__(self, other):
        return self.name == other.name and self.length == other.length


crocodile1 = Crocodile("Crock", "1.75m")
crocodile2 = Crocodile("Crock", "1.75m")
crocodile3 = Crocodile("Sławomir", "1.75m")

print(crocodile1 == crocodile2)
print(crocodile2 == crocodile3)
print(crocodile1 == crocodile3)
