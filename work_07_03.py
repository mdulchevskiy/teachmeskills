# Написать программу для нахождения факториала. Факториал натурального числа n
# определяется как произведение всех натуральных чисел от 1 до n включительно.


def my_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


print(my_factorial(3))
