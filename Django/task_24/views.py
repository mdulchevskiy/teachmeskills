# pip install django
# pip install requests


# 24.1. Создать модель NatureImage. Атрибуты: ссылка, ширина картинки(int), высота картинки(int), комментарий.
# 24.2. Создать форму с двумя полями: ширина картинки, высота картинки.
# 24.3. Реализовать следующее поведение:
#     a. Пользователь на домашней странице видит форму с шириной и высотой.
#     b. Пользователь получает случайное изображения с https://picsum.photos/ (той ширины и высоты, что были
#        введены на форме) с полем для комментария, кнопками сохранить и перейти на домашнюю страницу.
#     c. При сохранении, запись заносится в базу и пользователь видит форму
#        для отправки изображения по почте с кнопкой send.


import requests
from django.core.mail import send_mail
from django.template import loader
from task_24.models import NatureImage
from django.conf import settings
from django.shortcuts import (render,
                              redirect, )
from task_24.forms import (ImageResolutionForm,
                           ContactForm, )


def get_image(width, height):
    return requests.get(f'https://picsum.photos/{width}/{height}').url


def home_page(request):
    form = ImageResolutionForm()
    if request.method == 'POST':
        form = ImageResolutionForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            width = form_data['width']
            height = form_data['height']
            image_link = get_image(width, height)
            image_data = dict(
                link=image_link,
                width=width,
                height=height,
            )
            request.session['image_data'] = image_data
            return render(request, 'image_page.html', {'image_link': image_link})
    return render(request, 'home_page.html', {'form': form})


def save_image(request):
    if request.method == 'POST' and 'image_data' in request.session:
        image_data = request.session['image_data']
        image_data['comment'] = request.POST['comment']
        NatureImage.objects.create(**image_data)
        message_dict = {
            'receiver': ' ',
            'subject': 'Message from Task 24!',
            'image': f'{image_data["link"]}',
        }
        context = {'form': ContactForm(message_dict)}
        return render(request, 'message_page.html', context)
    return redirect('home_page')


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            html_message = loader.render_to_string(
                'email.html',
                {'image': data.get('image')},
            )
            send_mail(
                from_email=settings.EMAIL_HOST_USER,
                subject=data.get('subject'),
                message='HI.',
                html_message=html_message,
                recipient_list=[data.get('receiver')],
                fail_silently=False,
            )
    return redirect('home_page')
