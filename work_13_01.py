from string import ascii_uppercase
from random import (choice, randint)
from abc import ABC, abstractmethod


class FelineInterface(ABC):
    @abstractmethod
    def do_cat_thing(self):
        raise NotImplemented


class CanineInterface(ABC):
    @abstractmethod
    def do_dog_thing(self):
        raise NotImplemented


class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass


class WildAnimal(Animal):
    pass


class Lion(WildAnimal, FelineInterface):
    def voice(self):
        print('Roar!')

    def do_cat_thing(self):
        pass


class Wolf(WildAnimal, CanineInterface):
    def voice(self):
        print('Awwww!')

    def do_dog_thing(self):
        pass


class Pet(Animal):
    __counter = 0

    def __init__(self, name, age, master, weight, address='Minsk'):
        self.name = name
        self.age = age
        self.weight = weight
        self.__master = master
        self.__address = address
        Pet.__counter += 1

    def run(self):
        print('Run!')

    def jump(self, meters):
        print(f'Jump {meters} meters')

    def birthday(self):
        self.age += 1

    def change_weight(self, diff=0.2):
        self.weight += diff

    def change_name(self, name):
        self.name = name

    def get_master(self):
        return self.__master

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @classmethod
    def get_counter(cls):
        return cls.__counter

    @staticmethod
    def get_random_name():
        return f'{choice(ascii_uppercase)}-{randint(0, 99)}'


class Dog(Pet, CanineInterface):
    def voice(self):
        print('Woof Woof!')

    def jump(self, meters):
        if meters > 0.5:
            print('Dogs cannot jump so high.')
        else:
            super().jump(meters)

    def do_dog_thing(self):
        pass


class Cat(Pet, FelineInterface):
    def voice(self):
        print('Meow Meow!')

    def jump(self, meters):
        if meters > 2:
            print('Cats cannot jump so high.')
        else:
            super().jump(meters)

    def do_cat_thing(self):
        pass


class Parrot(Pet):
    def __init__(self, name, age, master, weight, address, species):
        super().__init__(name, age, master, weight, address)
        self.species = species

    def voice(self):
        print('I am parrot!')

    def fly(self):
        if self.weight > 0.1:
            print('This parrot cannot fly.')
        else:
            print('Fly!')

    def change_weight(self, diff=0.05):
        self.weight += diff

    def jump(self, meters):
        if meters > 0.05:
            print('Parrots cannot jump so high.')
        else:
            super().jump(meters)


def animal_voices(animals):
    for animal in animals:
        animal.voice()


def main():
    dog = Dog('Bob', 2, 'Max', 2)
    cat = Cat('Fil', 2, 'Max', 2)
    parrot = Parrot('Chick', 2, 'Max', 0.1, 'Minsk', 'Ara')
    lion = Lion()
    wolf = Wolf()
    animal_voices([dog, cat, parrot, lion, wolf])
    print(f'\nPets counter: {Pet.get_counter()}')
    print(f'Random name: {Pet.get_random_name()}')


if __name__ == '__main__':
    main()
