# URL Shortener
Final Project 1 for [TeachMeSkills](https://teachmeskills.by/).

## Description

### Task:
Создать сокращалку ссылок наподобие https://bitly.com/<br>
Примеры сокращенных ссылок:<br>
127.0.0.1:8000/ab17k<br>
127.0.0.1:8000/55781

Что должно быть:
1) форма для сокращения ссылки;
2) список сокращенных ссылок.

Список должен включать следующие поля:
- оригинальную ссылку;
- сокращенную ссылку;
- дату добавления ссылки;
- количество кликов по сокращенной ссылке.

Нажатие на сокращенную ссылку должно приводить к перенаправлению на оригинальную ссылку.
Форма сокращения ссылки должна находиться сразу на главной странице (http://127.0.0.1:8000/) и отображаться при отсутствии GET параметров.

***Дополнительное задание 1**<br>
Реализовать возможность самостоятельного ввода сокращенной ссылки. Добавить валидацию при попытке повторного использования уже используемой сокращенной ссылки.

****Дополнительное задание 2**<br>
Покрыть тестами все view.

## Getting Started
### Installing virtualenv
```
pip install virtualenv
```
### Start a new virtualenv container
```
virtualenv -p python3 directory/name
```
activate
```
source bin/activate
```
deactivate
```
deactivate
```
### Installing packages
```
pip install -r requirements.txt
```
### Preparing the database
```
python manage.py makemigrations shortener
python manage.py migrate shortener
```
### Run Server
```
python manage.py runserver
```
## Running the tests
```
python manage.py test shortener
```
