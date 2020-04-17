# pip install django


from django.http import HttpResponse
from django.template import loader
from datetime import datetime


# 19.01. Дана форма с тремя текстовыми полями. Вернуть пользователю максимальное по длине значение поля.
# Пример: введены abc, abcdef, ab - пользователю вернется abcdef.
# Запуск через шаблон (открыть в браузере).
def task_19_01(request):
    first_str = request.POST.get('first')
    second_str = request.POST.get('second')
    third_str = request.POST.get('third')
    strings = [first_str, second_str, third_str]
    max_str = strings[0]
    max_len = len(max_str)
    for string in strings:
        length = len(string)
        if length > max_len:
            max_str = string
            max_len = length
    template = loader.get_template('task_19_01_2.html')
    context = {
        'first': first_str,
        'second': second_str,
        'third': third_str,
        'max_str': max_str,
    }
    return HttpResponse(template.render(context, request))


# 19.02. Дана форма с одним полем - дата. Если дата первое января - вывести сообщение:
# “С новым {номер года} годом”. В ином случае, вывести дату в формате: год-месяц-день.
# Запуск через шаблон (открыть в браузере).
def task_19_02(request):
    date = request.POST.get('date')
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    message = f'С новым {year} годом!' if month == 1 and day == 1 else date
    template = loader.get_template('task_19_02_2.html')
    return HttpResponse(template.render({'message': message}, request))
