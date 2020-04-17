-- создание таблицы
CREATE TABLE person (
    id integer,
    firstname varchar,
    lastname varchar
);

-- удаление таблицы
DROP TABLE person;

-- изменение таблицы
ALTER TABLE person
ADD COLUMN email varchar(255);
/* ALTER TABLE person
DROP COLUMN email; - не работает для sqlite */

-- добавление данных
INSERT INTO person (id,firstname,lastname)
VALUES (0,'Alex','Varkalov'),
       (1,'Alex','Mihalev'),
       (2,'Nick','Perlov'),
       (3,'Nick','Varkalov'),
       (4,'Maxim','Dulchevskiy'),
       (5,'Maxim','Person');

-- выборка данных
SELECT * FROM person;
SELECT id FROM person;
SELECT firstname, lastname FROM person;

-- выборка данных с условием
SELECT * FROM person WHERE firstname = 'Alex';

-- обновление данных
UPDATE person
SET firstname = 'Alexander'
WHERE firstname = 'Alex';
SELECT * FROM person WHERE firstname = 'Alexander';

-- удаление данных
DELETE FROM person
WHERE id = 0;

-- and, or
SELECT * FROM person
WHERE firstname = 'Maxim' and lastname = 'Dulchevskiy';
SELECT * FROM person
WHERE firstname = 'Maxim' or id < 2;
