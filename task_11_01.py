# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.


from random import random


class Wizard:
    def __init__(self, hero_class, level, hp, mana, damage, cast_speed):
        self.__hero_class = hero_class
        self.__level = level
        self.__hp = hp
        self.__mana = mana
        self.damage = damage
        self.cast_speed = cast_speed

    def cast_first_spell(self):
        spell_damage = self.damage * random() + 40
        print(f'Fireball! - {spell_damage} hp')

    def cast_second_spell(self):
        spell_damage = self.damage * random() + 100
        print(f'Flame Pillar! - {spell_damage} hp')

    def get_hero_class(self):
        return self.__hero_class

    def get_level(self):
        return self.__level

    def get_hp(self):
        return self.__hp

    def get_mana(self):
        return self.__mana

    def get_damage(self):
        return self.damage

    def get_cast_speed(self):
        return self.cast_speed

    def set_hero_class(self, hero_class):
        self.__hero_class = hero_class

    def set_level(self, level):
        self.__level = level

    def set_hp(self, hp):
        self.__hp = hp

    def set_mana(self, mana):
        self.__mana = mana

    def set_damage(self, damage):
        self.damage = damage

    def set_cast_speed(self, cast_speed):
        self.cast_speed = cast_speed


class Warrior:
    def __init__(self, hero_class, level, hp, mana, damage, attack_speed):
        self.__hero_class = hero_class
        self.__level = level
        self.__hp = hp
        self.__mana = mana
        self.damage = damage
        self.attack_speed = attack_speed

    def get_hero_class(self):
        return self.__hero_class

    def attack_first_spell(self):
        attack_damage = self.damage * random() + 30
        print(f'Slam! - {attack_damage} hp')

    def attack_second_attack(self):
        attack_damage = self.damage * random() + 150
        print(f'Vengeance! - {attack_damage} hp')

    def get_level(self):
        return self.__level

    def get_hp(self):
        return self.__hp

    def get_mana(self):
        return self.__mana

    def get_damage(self):
        return self.damage

    def get_attack_speed(self):
        return self.attack_speed

    def set_hero_class(self, hero_class):
        self.__hero_class = hero_class

    def set_level(self, level):
        self.__level = level

    def set_hp(self, hp):
        self.__hp = hp

    def set_mana(self, mana):
        self.__mana = mana

    def set_damage(self, damage):
        self.damage = damage

    def set_attack_speed(self, attack_speed):
        self.attack_speed = attack_speed


def main():
    wizard = Wizard('Sorcerer', 84, 3400, 6000, 700, 70)
    print(f'Wizard class and level: {wizard.get_hero_class()} {wizard.get_level()} lvl')
    print(f'Wizard hp and mana: {wizard.get_hp()}, {wizard.get_mana()}')
    print(f'Wizard damage and cast speed: {wizard.damage}, {wizard.cast_speed} hits per minute')
    print(f'\nNew level!!\n')
    wizard.set_level(wizard.get_level() + 1)
    wizard.set_hp(wizard.get_hp() + 100)
    wizard.set_mana(wizard.get_mana() + 200)
    wizard.set_damage(wizard.damage + 50)
    wizard.set_cast_speed(wizard.cast_speed + 5)
    print(f'Wizard class and level: {wizard.get_hero_class()} {wizard.get_level()} lvl')
    print(f'Wizard hp and mana: {wizard.get_hp()}, {wizard.get_mana()}')
    print(f'Wizard damage and cast speed: {wizard.damage}, {wizard.cast_speed} hits per minute')


if __name__ == '__main__':
    main()
