class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, n):
        for i in range(n):
            print('Wow...')


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_pet(self, pet):
        self.pet = pet

    def listen_to_bark(self, n):
        self.pet.bark(n)


tom = Person('Tom', 12)
tom.add_pet(Dog('Golf', 2))
tom.listen_to_bark(3)
