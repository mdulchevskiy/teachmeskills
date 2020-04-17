# pip install sqlalchemy


# Транзакция — это осуществление одного или нескольких изменений базы данных.
# .commit - применение транзакции
# .rollback - отмена транзакции


from sqlalchemy import create_engine


engine = create_engine('sqlite:///work_15_db', echo=True)
connection = engine.connect()

transaction = connection.begin()
connection.execute(
   'INSERT INTO user_py (firstname, lastname) VALUES (:firstname, :lastname)',
   firstname="Pasha", lastname='Ivanov')
transaction.commit()
connection.close()
