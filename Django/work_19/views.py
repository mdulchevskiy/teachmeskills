# pip install django


from django.http import HttpResponse
from django.template import loader


def hello_world(request):
    return HttpResponse('Hello World!')


# 19.01. Форма из одного поля - имя. Вернуть длину имени.
# Запуск через шаблон (открыть в браузере).
def work_19_01(request):
    name = request.POST.get('name')
    length = len(name)
    return HttpResponse(f'Length "{name}" is {length}.')


# 19.02. Дана форма содержащая следующие поля: имя, фамилию, возраст.
# Если указанный возраст меньше 18 вывести сообщение “В доступе отказано”.
# В ином случае вывести “Добро пожаловать”.
# Запуск через шаблон (открыть в браузере).
def work_19_02(request):
    age = int(request.POST.get('age'))
    message = 'В доступе отказано.' if age < 18 else 'Добро пожаловать.'
    return HttpResponse(message)


# 19.03. Дана форма содержащая следующие поля: имя, фамилию, комментарий.
# Вывести пользователю длину комментария, количество гласных и согласных в комментарии.
# Запуск через шаблон (открыть в браузере).
def work_19_03(request):
    comment = request.POST.get('comment')
    length = len(comment)
    vowels = 'уеыаоэяиюё'
    consonant = 'йцкнгшщзхждлрпвфчсмтбъь'
    vowel_counter = 0
    consonant_counter = 0
    for letter in comment:
        if letter in vowels:
            vowel_counter += 1
        elif letter in consonant:
            consonant_counter += 1
    return HttpResponse(
        f'Comment: {comment}<br>'
        f'Comment length: {length}<br>'
        f'Vowels amount: {vowel_counter}<br>'
        f'Consonant amount: {consonant_counter}'
    )


# 19.04. Дана форма содержащая следующие поля: имя, возраст, комментарий.
# Вывести комментарий пользователя разделенный на строки. Каждую строку дополнить
# в конце следующей надписью “(с) {имя автора}”.
# Запуск через шаблон (открыть в браузере).
def work_19_04(request):
    name = request.POST.get('name')
    comment = request.POST.get('comment')
    comment = f'{comment}'.split('\r\n')
    result = ''
    for line in comment:
        result += f'{line} (c) {name}<br>'
    return HttpResponse(result)


# 19.06. Создать два шаблона. Первый шаблон содержит форму с одним полем - имя.
# Второй django шаблон отображающий имя.
def work_19_06(request):
    name = request.POST.get('name')
    template = loader.get_template('work_19_06_2.html')
    context = {'name': name}
    return HttpResponse(template.render(context, request))
