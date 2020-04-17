# pip install django


from django.http import HttpResponse
from django.template import loader
from work_20.forms import UserForm


# 20.01. Форма имя, фамилия, возраст, комментарий. Вью выводит в консоль строку
# вида '{firstname}|{lastname}|{age}|{comment}' и возвращает пустую форму.
# Шаблон, роут должны быть определены в приложении.
def work_20_01(request):
    if request.method == 'POST':
        firstname = request.POST.get('name')
        lastname = request.POST.get('surname')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        result = f'{firstname}|{lastname}|{age}|{comment}'
        print(result)
    template = loader.get_template('work_20_01.html')
    return HttpResponse(template.render({}, request))


# 20.02. В задании 20.01 создать base.html в папке templates.
# Изменить шаблон задания 20.01, чтобы он использовал как основу base.html.
def work_20_02(request):
    if request.method == 'POST':
        firstname = request.POST.get('name')
        lastname = request.POST.get('surname')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        result = f'{firstname}|{lastname}|{age}|{comment}'
        print(result)
    template = loader.get_template('work_20_02.html')
    return HttpResponse(template.render({}, request))


# 20.03. В задании 20.02 поменять урл в шаблоне на обращение по имени урла.
def work_20_03(request):
    if request.method == 'POST':
        firstname = request.POST.get('name')
        lastname = request.POST.get('surname')
        age = request.POST.get('age')
        comment = request.POST.get('comment')
        result = f'{firstname}|{lastname}|{age}|{comment}'
        print(result)
    template = loader.get_template('work_20_03.html')
    return HttpResponse(template.render({}, request))


# 20.04 - 20.05. В задании 20.03 добавить валидацию через форму
# и использовать ее в шаблоне.
def work_20_04(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            age = data.get('age')
            comment = data.get('comment')
            result = f'{firstname}|{lastname}|{age}|{comment}'
            print(result)
        else:
            errors_dict = form.errors
            template = loader.get_template('work_20_05.html')
            return HttpResponse(template.render({'errors': errors_dict}, request))
    form = UserForm()
    context = {'form': form}
    template = loader.get_template('work_20_05.html')
    return HttpResponse(template.render(context, request))
