# pip install django


from django.http import HttpResponse
from django.template import loader
from task_20.forms import AviaSales


# 20. Создать форму через django forms описывающую заказ авиабилета.
# Форма должна содержать следующие поля - имя, откуда, куда, сколько человек, дата.
# При отправке данных пользователем проверять валидность данных.
# Если они валидны и количество человек равно 1 то вывести результат - "стоимость 100$",
# если количество человек больше 1, то стоимость должна считаться по формуле 100*2*количество человек.
# Если данные не валидны, то вывести ошибку.
def task_20(request):
    form = AviaSales(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            departure = data.get('departure')
            arrival = data.get('arrival')
            amount = data.get('amount')
            date = data.get('date')
            price = 100 if amount == 1 else amount * 2 * 100
            ticket = f'<p>Name: {name}' \
                     f'</p>Persons: {amount}' \
                     f'<p>Route: {date}, {departure}-{arrival}' \
                     f'</p>Price: {price} dollars.'
            return HttpResponse(ticket)
        else:
            err_dict = form.errors
            attr_dict = {
                'name': request.POST.get('name'),
                'departure': request.POST.get('departure'),
                'arrival': request.POST.get('arrival'),
                'amount': request.POST.get('amount'),
                'date': request.POST.get('date'),
            }
            field_list = ['name', 'departure', 'arrival', 'amount', 'date']
            for field in field_list:
                if field in err_dict:
                    del attr_dict[field]
            template = loader.get_template('task_20.html')
            form = AviaSales(initial=attr_dict)
            return HttpResponse(template.render({'errors': err_dict, 'form': form}, request))
    template = loader.get_template('task_20.html')
    context = {'form': AviaSales()}
    return HttpResponse(template.render(context, request))
