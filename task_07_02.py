# Написать программу, со следующим интерфейсом: пользователю предоставляется
# на выбор 12 вариантов перевода(описанных в первой задаче). Пользователь
# вводит цифру от одного до двенадцати. После программа запрашивает ввести численное
# значение. Затем программа выдает конвертированный результат. Использовать функции
# из первого задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”.


from task_07_01 import *


while True:
    functions = {1: inches_to_cm,
                 2: cm_to_inches,
                 3: miles_to_km,
                 4: km_to_miles,
                 5: pounds_to_kg,
                 6: kg_to_pounds,
                 7: ounces_to_grams,
                 8: grams_to_ounces,
                 9: gallons_to_liters,
                 10: liters_to_gallons,
                 11: pints_to_liters,
                 12: liters_to_pints}
    number = input('Enter number from 1 to 12: ')
    if not number.isdigit():
        print('Incorrect input. Try again.')
        continue
    number = int(number)

    if number == 0:
        break
    elif number > 12 or number < 1:
        print('Entered number out of range. Try again.')
        continue
    else:
        num = float(input('Enter number for convertation: '))

    func = functions[number]
    result = func(num)
    print(num, func.__name__, result)
