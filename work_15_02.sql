/* Создать таблицу
Добавить 5 записей
Получить всех пользователей с вашим именем
Получить всех пользователей младше 25
Получить всех пользователей в возрасте от 15 до 18 */

CREATE TABLE user (
    id integer primary key autoincrement,
    firstname varchar(255),
    lastname varchar(255),
    age integer
);

INSERT INTO user (firstname,lastname,age)
VALUES ('Alex','Varkalov',14),
       ('Alex','Mihalev',16),
       ('Nick','Perlov',17),
       ('Nick','Varkalov',20),
       ('Maxim','Dulchevskiy',25),
       ('Maxim','Person',28);

SELECT * FROM user
WHERE firstname = 'Maxim';

select * FROM user
WHERE age < 25;

SELECT * FROM user
WHERE age > 14 AND age < 18;
