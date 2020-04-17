# 18. Написать сайт. Сайт предоставляет полный CRUD для работы с продуктами.
# Модель продукта состоит из id, name, price, amount, comment.
# На главной странице отображена краткая информация (id, name, price, amount) по всем продуктам.
# При нажатии на продукт происходит перенаправление на детализированную информацию по продукту.
# На детализированной странице продукта есть кнопки позволяющие отредактировать и удалить продукт.


from models import Product
from flask import (render_template, 
                   request, 
                   flash, 
                   redirect, 
                   url_for, )
from settings import (app, 
                      db, )


def is_product_valid(form):
    flag = form['name'] and form['name'].isalpha() and\
           form['price'] and form['price'].replace('.', '').isdigit() and\
           form['amount'] and form['amount'].isdigit() and\
           form['comment'] and not form['comment'].isspace()
    return flag


@app.route('/')
def show_all_products():
    products = Product.query.all()
    return render_template('home_page.html', products=products)


@app.route('/add_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        if not is_product_valid(request.form):
            flash('You entered incorrect information.', 'error')
        else:
            product = Product(**request.form)
            db.session.add(product)
            db.session.commit()
            flash('Product has been successfully added.')
            return redirect(url_for('show_all_products'))
    return render_template('create_product.html')


@app.route('/product/<int:product_id>', methods=['GET'])
def detail_product(product_id):
    if request.method == 'GET':
        product = Product.query.filter_by(id=product_id).first()
        if product:
            return render_template('detail_product.html', product=product)
        flash(f'Product with ID:{product_id} does not exist.')
        return redirect(url_for('show_all_products'))
    flash(f'This view supports only GET method.')
    return redirect(url_for('show_all_products'))


@app.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    if request.method == 'GET':
        product = Product.query.filter_by(id=product_id).first()
        if product:
            return render_template('edit_product.html', product=product)
        flash(f'Product with ID:{product_id} does not exist.')
        return redirect(url_for('show_all_products'))
    elif request.method == 'POST':
        if not is_product_valid(request.form):
            flash('You entered incorrect information.', 'error')
        else:
            product = Product.query.filter_by(id=product_id).first()
            if product:
                product.name = request.form['name']
                product.price = request.form['price']
                product.amount = request.form['amount']
                product.comment = request.form['comment']
                db.session.add(product)
                db.session.commit()
                flash('Record was successfully edited.')
                return redirect(url_for('show_all_products'))
            flash(f'Product with ID:{product_id} does not exist.')
            return redirect(url_for('show_all_products'))
    flash(f'This view supports only GET and PUT methods.')
    return redirect(url_for('show_all_products'))


@app.route('/del/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    if request.method == 'POST':
        product = Product.query.filter_by(id=product_id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            flash(f'Product with ID:{product_id} was successfully deleted.')
            return redirect(url_for('show_all_products'))
        flash(f'Product with ID:{product_id} does not exist.')
        return redirect(url_for('show_all_products'))
    flash(f'This view supports only GET method.')
    return redirect(url_for('show_all_products'))
