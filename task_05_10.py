# Создать список поездов. Структура словаря: номер поезда, пункт и время прибытия,
# пункт и время отбытия. Вывести все сведения о поездах, время пребывания в пути
# которых превышает 7 часов 20 минут. Примечание: данное задание подразумевает
# самостоятельное изучение принципов работы со временем в Python(библиотека datetime).
# [02-7.3-ML02]


import datetime


schedule = [
    {
        'train number': 456,
        'end route': 'Moscow',
        'arrival': datetime.datetime(2019, 10, 15, 8, 30),
        'start route': 'Minsk',
        'departure': datetime.datetime(2019, 10, 14, 12, 30),
    },
    {
        'train number': 302,
        'end route': 'Vilnius',
        'arrival': datetime.datetime(2019, 10, 14, 16, 30),
        'start route': 'Minsk',
        'departure': datetime.datetime(2019, 10, 14, 12, 30),
    },
    {
        'train number': 403,
        'end route': 'Warsaw',
        'arrival': datetime.datetime(2019, 10, 15, 3, 30),
        'start route': 'Minsk',
        'departure': datetime.datetime(2019, 10, 14, 12, 30),
    },
    {
        'train number': 234,
        'end route': 'Berlin',
        'arrival': datetime.datetime(2019, 10, 16, 10, 30),
        'start route': 'Minsk',
        'departure': datetime.datetime(2019, 10, 14, 12, 30),
    },
]
for ind, train in enumerate(schedule):
    time_travel = train['arrival'] - train['departure']
    if time_travel > datetime.timedelta(hours=7, minutes=20):
        print(f'\nTime travel for {ind + 1} train is {time_travel} hours. More details:')
        for key, value in train.items():
            print(f'{key}: {value}')
