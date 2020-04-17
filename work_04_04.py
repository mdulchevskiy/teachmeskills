# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел
# от 1 до n(включая n) используя цикл while.


n = int(input('Enter n: '))
summ = 0
i = 1
while i <= n:
    summ += i ** 3
    i += 1
print(summ)
