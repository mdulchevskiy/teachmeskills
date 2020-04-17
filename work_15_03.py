# pip install sqlalchemy


from sqlalchemy import create_engine

FLAG = 0
e = create_engine("sqlite:///work_15_db")

if FLAG:
    e.execute("""
       CREATE TABLE user_py (
           id integer primary key autoincrement,
           firstname varchar,
           lastname varchar
       );
       """)

if FLAG:
    e.execute("""
       INSERT INTO user_py (firstname, lastname)
       VALUES ('Alex','Varkalov'),
              ('Alex','Mihalev'),
              ('Nick','Perlov'),
              ('Nick','Varkalov'),
              ('Maxim','Dulchevskiy'),
              ('Maxim','Person');
    """)

result = e.execute('SELECT * FROM user_py')
print(type(result))
for user in result:
   print(user)
