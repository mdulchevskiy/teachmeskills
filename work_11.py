class Pet:
    def __init__(self, name, age, master, weight, address='Minsk'):
        self.name = name
        self.age = age
        self.weight = weight
        self.__master = master
        self.__address = address


    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')

    def birthday(self):
        self.age += 1

    def sleep(self):
        print('Sleep!')

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



class Dog(Pet):
    def bark(self):
        print('Woof Woof!')


class Cat(Pet):
    def meow(self):
        print('Meow Meow!')


class Parrot(Pet):
    def fly(self):
        if self.weight > 0.1:
            print('This parrot cannot fly.')
        else:
            print('Fly!')
