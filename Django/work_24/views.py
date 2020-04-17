# pip install django


# 24. Создать приложения по хранению ссылок на изображения животных.
# На главной странице две кнопки: I love cats!, I love dogs.
# При нажатии на кнопку возвращается ссылка на рандомное изображение, которое пользователь может сохранить в бд.
# Бд - модель AnimalImage. Атрибуты: url, вид(species: кошка или собака), дата создания, тип(png, gif, jpg, jpeg).
# Доп. Написать view и темплейт для отправки текстовых сообщений на почту.
# Форма: тема письма, получатель, текст сообщения.


import requests
from django.core.mail import send_mail
from src.settings import EMAIL_HOST_USER
from work_24.models import AnimalImage
from work_24.forms import SendEmailForm
from django.shortcuts import (render, 
                              redirect, )


def home_page(request):
    return render(request, 'home_page.html')


def get_image(request):
    if request.method == 'POST':
        button = request.POST['button']
        if button == 'I love cats!':
            data = requests.get('https://aws.random.cat/meow').json()
            link = data['file']
            species = 'Cat'
        elif button == 'I love dogs!':
            data = requests.get('https://dog.ceo/api/breeds/image/random').json()
            link = data['message']
            species = 'Dog'
        extension = link.split('.')[-1]
        animal_image_data = dict(
            url=link,
            type=extension,
            species=species,
        )
        request.session['animal_image_data'] = animal_image_data
        return render(request, 'get_image.html', {'image': link})
    return redirect(home_page)


def save_image(request):
    if request.method == 'POST' and 'animal_image_data' in request.session:
        animal_image_data = request.session['animal_image_data']
        AnimalImage.objects.create(**animal_image_data)
    return redirect(home_page)


def send_email(request):
    if request.method == 'GET':
        return render(request, 'send_email.html', {'form': SendEmailForm()})
    elif request.method == 'POST':
        data = SendEmailForm(request.POST)
        if data.is_valid():
            cleaned_data = data.cleaned_data
            send_mail(
                subject=cleaned_data.get('topic'),
                message=cleaned_data.get('message'),
                from_email=EMAIL_HOST_USER,
                recipient_list=[cleaned_data.get('receiver')],
                fail_silently=False,
            )
    return redirect(home_page)
