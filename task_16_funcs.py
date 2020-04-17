# Создать таблицы Brand(name), Car(model, release_year, brand(foreing key на
# таблицу Brand)). Реализовать CRUD(создание, чтение, обновление по id,
# удаление по id) для бренда и машины. Создать пользовательский интерфейс.


from sqlalchemy.orm import sessionmaker
from task_16_db_creation import engine, Base, Brand, Car
from task_16_ui_funcs import brand_choosing_param, car_choosing_param


Session = sessionmaker(bind=engine)
session = Session()


def create_table():
    Base.metadata.create_all(engine)


def get_brands(brand_id=None):
    if brand_id:
        brands = session.query(Brand).filter_by(id=brand_id).first()
    else:
        brands = session.query(Brand).all()
    session.close()
    return brands


def add_brand():
    print_brands(pause=False)
    brand_name = input('Brand name: ')
    if not brand_name or not brand_name.isalpha():
        print("\nIncorrect brand name.")
        input('PRESS ENTER')
    else:
        brand = Brand(brand_name=brand_name)
        session.add(brand)
        session.commit()


def brand_update():
    brands = get_brands()
    if brands:
        print_brands(pause=False)
        brand_id = input('Brand ID: ')
        brand = get_brands(brand_id)
        parameter = brand_choosing_param()
        new_value = input('\nEnter new value: ')
        setattr(brand, parameter, new_value)
        session.add(brand)
        session.commit()
        print(f'Brand ID:{brand_id} successfully updated!')
    else:
        print("\nCannot update a brand without brands in DB.")
        input('PRESS ENTER')


def brand_delete():
    brands = get_brands()
    if brands:
        print_brands(pause=False)
        brand_id = input('Brand ID: ')
        print('\nDeleting brand by ID.')
        brand = get_brands(brand_id)
        session.delete(brand)
        session.commit()
        print(f'Brand ID:{brand_id} successfully deleted!')
    else:
        print("\nCannot delete a brand without brands in DB.")
        input('PRESS ENTER')


def print_brands(pause=True):
    brands = get_brands()
    print('\n*************************')
    print('ID', 'Brand name'.center(20), sep='|')
    print('-------------------------')
    for brand in brands:
        result_str = '{}|{}'.format(
            str(brand.id).ljust(2),
            brand.brand_name.center(20),
        )
        print(result_str)
    print('*************************')
    if pause:
        input('PRESS ENTER')


def get_cars(car_id=None):
    if car_id:
        cars = session.query(Car).filter_by(id=car_id).first()
    else:
        cars = session.query(Car).all()
    session.close()
    return cars


def add_car():
    brands = get_brands()
    if brands:
        print_brands(pause=False)
        name, release_year, brand = enter_car()
        car = Car(model=name, release_year=release_year, brand=brand)
        session.add(car)
        session.commit()
    else:
        print("\nCannot add a car without brands in DB.")
        input('PRESS ENTER')


def enter_car():
    model = input('Model: ')
    release_year = int(input('Release year: '))
    brand_id = int(input('Brand ID: '))
    brand = get_brands(brand_id)
    return model, release_year, brand


def car_update():
    cars = get_cars()
    if cars:
        print_cars(pause=False)
        car_id = input('Car ID: ')
        car = get_cars(car_id)
        parameter = car_choosing_param()
        if parameter == 'brand':
            print_brands(pause=False)
            brand_id = input('Brand ID: ')
            brand = get_brands(brand_id)
            car.brand = brand
        else:
            new_value = input('\nEnter new value: ')
            setattr(car, parameter, new_value)
        session.add(car)
        session.commit()
        print(f'Car ID:{car_id} successfully updated!')
    else:
        print("\nCannot update a car without cars in DB.")
        input('PRESS ENTER')


def car_delete():
    cars = get_cars()
    if cars:
        print_cars(pause=False)
        car_id = input('Car ID: ')
        print('\nDeleting car by ID.')
        car = get_cars(car_id)
        session.delete(car)
        session.commit()
        print(f'Car ID:{car_id} successfully deleted!')
    else:
        print("\nCannot delete a car without cars in DB.")
        input('PRESS ENTER')


def print_cars(pause=True):
    cars = get_cars()
    print('\n****************************************')
    print('ID', 'Model'.center(10), 'Release year'.center(12), 'Brand'.center(10), sep='|')
    print('----------------------------------------')
    for car in cars:
        result_str = '{}|{}|{}|{}'.format(
            str(car.id).ljust(2),
            car.model.center(10),
            str(car.release_year).center(12),
            str(car.brand.brand_name).center(10),
        )
        print(result_str)
    print('****************************************')
    if pause:
        input('PRESS ENTER')

