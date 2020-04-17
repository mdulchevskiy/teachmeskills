from work_20.models import Customer


# 20.06. Создать 3 пользователей.
# Получить пользователей с именем Vlad. Получить пользователя с id 1.
# Все задания выполняются в шеле.
# python manage.py shell -> from work_20.models import Customer -> exit()
def work_20_06_1():
    customer = Customer(
        firstname='Maxim',
        lastname='Dulchevskiy',
        age=23,
        profession='Developer',
    )
    customer.save()


def work_20_06_2():
    customer = Customer()
    customer.firstname = 'Nick'
    customer.lastname = 'Mihalevich'
    customer.age = 23
    customer.profession = 'Banking'
    customer.save()


def work_20_06_3():
    Customer.objects.create(
        firstname='Vlad',
        lastname='Sudilovskiy',
        age=22,
        profession='Banking',
    )


def work_20_06_4():
    Customer.objects.filter(firstname='Vlad')


def work_20_06_5():
    Customer.objects.filter(id=1)
