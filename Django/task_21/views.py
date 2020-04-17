# pip install django


from task_21.models import Users
from task_21.forms import UserForm
from django.shortcuts import (render,
                              redirect, )


# 21. Написать сайт. Сайт предоставляет полный CRUD для работы с пользователями.
# Модель продукта состоит из id, firstname, lastname, age, profession.
# На главной странице отображена краткая информация(id, firstname, lastname) о всех пользователях.
# При нажатии на пользователя происходит перенаправление на детализированную информацию по пользователю.
# На детализированной странице пользователя есть кнопки позволяющие отредактировать и удалить пользователя.


def home_page(request):
    users = Users.objects.filter()
    return render(request, 'home_page.html', {'users': users})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Users.objects.create(**data)
            return redirect('home_page')
        else:
            error_list = form.errors
            attr_dict = {
                'firstname': request.POST.get('firstname'),
                'lastname': request.POST.get('lastname'),
                'age': request.POST.get('age'),
                'profession': request.POST.get('profession'),
            }
            field_list = list(attr_dict.keys())
            for field in field_list:
                if field in error_list:
                    del attr_dict[field]
            form = UserForm(initial=attr_dict)
            return render(request, 'add_user.html', {'form': form, 'errors': error_list})
    return render(request, 'add_user.html', {'form': UserForm()})


def detail_user(request, user_id):
    user = Users.objects.get(id=user_id)
    return render(request, 'detail_user.html', {'user': user})


def delete_user(request, user_id):
    Users.objects.filter(id=user_id).delete()
    return redirect('home_page')


def edit_user(request, user_id):
    user = Users.objects.get(id=user_id)
    attr_dict = {
        'firstname': user.firstname,
        'lastname': user.lastname,
        'age': user.age,
        'profession': user.profession,
    }
    form = UserForm(initial=attr_dict)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Users.objects.filter(id=user_id).update(**data)
            return redirect('home_page')
        else:
            error_list = form.errors
            attr_dict = {
                'firstname': request.POST.get('firstname'),
                'lastname': request.POST.get('lastname'),
                'age': request.POST.get('age'),
                'profession': request.POST.get('profession'),
            }
            field_list = list(attr_dict.keys())
            for field in field_list:
                if field in error_list:
                    del attr_dict[field]
            form = UserForm(initial=attr_dict)
            return render(request, 'edit_user.html', {'form': form, 'errors': error_list, 'user_id': user_id})
    return render(request, 'edit_user.html', {'form': form, 'user_id': user_id})
