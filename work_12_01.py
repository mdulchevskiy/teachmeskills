class Pet:
    __counter = 0

    def __init__(self, name, age, master, weight, address='Minsk'):
        self.name = name
        self.age = age
        self.weight = weight
        self.__master = master
        self.__address = address
        Pet.__counter += 1

    def voice(self):
        pass

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


class Dog(Pet):
    def voice(self):
        print('Woof Woof!')

    def jump(self, meters):
        if meters > 0.5:
            print('Dogs cannot jump so high.')
        else:
            super().jump(meters)


class Cat(Pet):
    def voice(self):
        print('Meow Meow!')

    def jump(self, meters):
        if meters > 2:
            print('Cats cannot jump so high.')
        else:
            super().jump(meters)


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
    animal_voices([dog, cat, parrot])
    # print(Pet._Pet__counter)


if __name__ == '__main__':
    main()
