# pip install django
# pip install requests


import requests
from work_25.forms import SearchForm
from work_25.models import AnimalImage
from django.shortcuts import (render,
                              redirect, )
from work_25.forms import (TYPES_CHOICES,
                           SPECIES_CHOICES, )


# 25.01. Добавить форму поиска на домашнюю страницу.
# Форма состоит из двух dropdown`ов - выбор животного(собака, кошка), тип изображения.
def home_page(request):
    return render(request, 'home_page.html', {'form': SearchForm()})


# 25.02. Добавить view для фильтрации животных по виду животного.
# В результате отображается список животных с ссылками и кнопкой возвращения на домашнюю страницу.
def filter_images(request):
    if request.method == 'POST':
        data = SearchForm(request.POST)
        if data.is_valid():
            cleaned_data = data.cleaned_data
            species_search = cleaned_data.get('species')
            type_search = cleaned_data.get('type')
            species = dict(SPECIES_CHOICES).get(species_search)
            image_type = dict(TYPES_CHOICES).get(type_search)
            animals = AnimalImage.objects.filter(species=species, type=image_type.lower())
            return render(request, 'search_page.html', {'animals': animals})
    return redirect(home_page)


def get_image(request):
    if request.method == 'POST':
        button = request.POST['button']
        if button == 'I love cats!':
            link = get_cat_url()
            species = 'Cat'
        elif button == 'I love dogs!':
            link = get_dog_url()
            species = 'Dog'
        extension = link.split('.')[-1]
        animal_image_data = dict(
            url=link,
            type=extension,
            species=species,
        )
        request.session['animal_image_data'] = animal_image_data
        return render(request, 'image_page.html', {'image': link})
    return redirect(home_page)


def get_cat_url():
    data = requests.get('https://aws.random.cat/meow').json()
    return data['file']


def get_dog_url():
    data = requests.get('https://dog.ceo/api/breeds/image/random').json()
    return data['message']


def save_image(request):
    if request.method == 'POST' and 'animal_image_data' in request.session:
        animal_image_data = request.session['animal_image_data']
        AnimalImage.objects.create(**animal_image_data)
    return redirect(home_page)
