📌 Создание таблиц
sql
Копировать
Редактировать
-- Простая таблица товаров
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    price REAL DEFAULT 0.0,
    stock INTEGER
);

-- Таблица клиентов
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
);

-- Таблица заказов с внешним ключом
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
📌 Вставка данных
sql
Копировать
Редактировать
-- Один товар
INSERT INTO products (title, price, stock) VALUES ('Монитор', 9999.99, 12);

-- Несколько сразу
INSERT INTO customers (name, email) VALUES
('Иван Петров', 'ivan@example.com'),
('Анна Смирнова', 'anna@example.com');
📌 Получение данных
sql
Копировать
Редактировать
-- Всё из таблицы
SELECT * FROM products;

-- С фильтром
SELECT * FROM products WHERE price > 5000;

-- Только нужные поля
SELECT title, price FROM products;

-- Сортировка
SELECT * FROM products ORDER BY price DESC;

-- Лимит + пропуск
SELECT * FROM products LIMIT 5 OFFSET 10;
📌 Обновление данных
sql
Копировать
Редактировать
-- Изменить цену у товара с id=1
UPDATE products SET price = 7999.99 WHERE id = 1;
📌 Удаление данных
sql
Копировать
Редактировать
-- Удалить один товар
DELETE FROM products WHERE id = 3;

-- Очистить всю таблицу
DELETE FROM products;
📌 Агрегация
sql
Копировать
Редактировать
-- Сколько товаров
SELECT COUNT(*) FROM products;

-- Средняя цена
SELECT AVG(price) FROM products;

-- Минимальная и максимальная
SELECT MIN(price), MAX(price) FROM products;

-- Сумма всех товаров на складе
SELECT SUM(stock) FROM products;
📌 Группировка
sql
Копировать
Редактировать
-- Сколько товаров по каждому складу
SELECT stock, COUNT(*) FROM products GROUP BY stock;

-- Группировка с фильтрацией по группам
SELECT stock, COUNT(*) FROM products
GROUP BY stock
HAVING COUNT(*) > 1;
📌 JOIN (связь таблиц)
sql
Копировать
Редактировать
-- Заказы с именами клиентов
SELECT orders.id, customers.name, orders.order_date
FROM orders
JOIN customers ON orders.customer_id = customers.id;
📌 Создание индекса
sql
Копировать
Редактировать
CREATE INDEX idx_product_title ON products(title);
📌 Временная таблица
sql
Копировать
Редактировать
CREATE TEMP TABLE temp_example (
    id INTEGER,
    name TEXT
);
📌 Проверка существования таблицы
sql
Копировать
Редактировать
SELECT name FROM sqlite_master WHERE type='table' AND name='products';
📌 Добавление столбца в таблицу
sql
Копировать
Редактировать
ALTER TABLE products ADD COLUMN description TEXT;
📌 Уникальное поле и NOT NULL
sql
Копировать
Редактировать
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
📌 Вложенные запросы (подзапросы)
sql
Копировать
Редактировать
-- Все продукты дороже средней цены
SELECT * FROM products WHERE price > (
    SELECT AVG(price) FROM products
);
📌 Псевдонимы (AS)
sql
Копировать
Редактировать
SELECT title AS Название, price AS Цена FROM products;
📌 CASE (условия внутри SELECT)
sql
Копировать
Редактировать
SELECT title,
  CASE
    WHEN price > 10000 THEN 'Дорогой'
    ELSE 'Дешевый'
  END AS категория
FROM products;