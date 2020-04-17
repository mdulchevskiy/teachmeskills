# Написать функцию, которая получает на вход имя и выводит строку вида: “Hello, {name}”.
# Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.


def my_hello(name):
    print(f'Hello, {name}')


names = ['Alex', 'Kate', 'Pasha', 'Max', 'Daria']
for name in names:
    my_hello(name)
