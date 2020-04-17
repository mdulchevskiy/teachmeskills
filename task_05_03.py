# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.
# [02-3.2-HL02]


denom_dict = {}
for number in range(200, 301):
    denom_sum = 0
    for denom in range(1, number):
        if not number % denom:
            denom_sum += denom
    denom_dict[number] = denom_sum

denom_values = list(denom_dict.values())
denom_keys = list(denom_dict.keys())

for key in denom_keys:
    for value in denom_values:
        try:
            if denom_dict[key] == value and denom_dict[value] == key:
                print(f'Friendly numbers is {denom_dict[key]}-{denom_dict[value]}')
        except KeyError:
            pass
