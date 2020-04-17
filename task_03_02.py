# В семье N свадьба. Они решили выбрать заведение, где будут праздновать
# в зависимости от количества людей, которое прибудет к утру.
# Если их будет больше 50 - закажут ресторан, если от 20 до 50 -то кафе,
# а если меньше 20 то отпраздную дома. Вывести "ресторан", "кафе", "дом"
# в зависимости от количества гостей (прочитать переменную с консоли).


while True:
    guests = input('How many guests come to wedding = ')
    if guests.isdigit():
        break
    print('Incorrect input. Try again.')
guests = int(guests)
if guests > 50:
    place = 'restaurant'
elif guests > 20:
    place = 'cafe'
else:
    place = 'home'
print(place)
