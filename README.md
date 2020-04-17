# ToDo List
Final Project 2 for [TeachMeSkills](https://teachmeskills.by/).

## Description

### Task:
Реализовать ToDo список, который позволяет следующее:
 - просматривать текущие записи в списке;
 - добавлять запись в список;
 - править запись;
 - удалять запись;
 - перемещать запись на уровень выше, ниже;
 - отмечать задачу как сделанную.
 
В рамках выполнения задания обязательно наличие минимум 3 тестов (добавление, удаление, обновление).

***Дополнительное задание 1**<br>
Добавить возможность выбора приоритета с соответствующим отображением в виде цвета в списке (пример: задачи с высоким приоритетом - красные, средним - желтым, низким - зеленым).

****Дополнительное задание 2**<br>
Добавить возможность фильтрации заданий по приоритетам.

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
# Running the tests
```
python manage.py test shortener
```