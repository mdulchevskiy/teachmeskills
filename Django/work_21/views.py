# pip install django


from work_21.models import Customer
from work_21.forms import UserDataForm
from django.shortcuts import (render,
                              redirect, )


# 21. Создать домашнюю страницу. Страница доступна по урлу /home/.
# Страница состоит из одной надписи Home Page.
# Добавить возможность добавления нового Customer(добавить форму, шаблон, view, url).
# Форма доступна по урлу /add/. После создания пользователя перенаправлять на домашнюю страницу.
# Отображать всех Customer на домашней страницу.


def home_page(request):
    customers = Customer.objects.filter().all()
    return render(request, 'home.html', {'customers': customers})


def add_customer(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Customer.objects.create(**data)
            return redirect('home_page')
        else:
            data_dict = form.errors
            return render(request, 'add.html', {'errors': data_dict, 'form': UserDataForm()})
    return render(request, 'add.html', {'form': UserDataForm()})
