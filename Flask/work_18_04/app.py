# pip install flask
# pip install flask-sqlalchemy


from datetime import datetime
from flask import (Flask, 
                   request, 
                   redirect, 
                   url_for, 
                   render_template, )


app = Flask(__name__)


# 18.04. При запросе на домашнюю страницу отображается текущая дата.
@app.route('/')
def work_18_04():
    return f'{datetime.now()}'


# 18.05. При запросе по урлу /two_in/[number] возвращает 2 в степени number.
@app.route('/two_in/<int:number>')
def work_18_05(number):
    return f'2 ** {number} = {2 ** number}'


# 18.06. При запросе по урлу /my_word/[word], в случае если длина слова четна - выводит строку
# содержащую все нечетные элементы строки (abcde -> ace). В ином случае просто выводит слово.
@app.route('/my_word/<word>')
def work_18_06(word):
    if not len(word) % 2:
        return f'{word[::2]}'
    else:
        return f'{word}'


@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        # http://127.0.0.1:5000/login?=maxim
        user = request.args.get('name')
        if not user:
            return render_template('login.html')
        else:
            return redirect(url_for('success', name=user))


# 18.07. Создать шаблон с формой (имя, фамилия, возраст).
# Передать данные на вью.
@app.route('/reg', methods=['POST', 'GET'])
def work_18_07():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        # name, surname, age = request.form
        return render_template(
            'work_18_07_2.html',
            name=name,
            surname=surname,
            age=age,
        )
    else:
        return render_template('work_18_07_1.html')


if __name__ == '__main__':
    app.run()
