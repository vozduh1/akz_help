🟢 Назначение: Работа с базой данных SQLite (файловый формат)

📂 Open Database — открыть .sqlite файл
📘 Browse Data — посмотреть таблицу
📄 Execute SQL — ввод SQL-запросов вручную

🟢 Main меню:
    📁 File → New Database — создать базу
    🧱 Database Structure — показывает таблицы и поля

🧰 Execute SQL:
    🟩 Run SQL — выполнить написанный запрос
    🟢 Примеры:
        CREATE TABLE users (id INTEGER, name TEXT);
        INSERT INTO users VALUES (1, 'Alice');
        SELECT * FROM users;

💾 Write Changes — сохранить изменения
🔙 Revert Changes — откатить


🟢 Как создать базу данных в sqlite3 (Windows / Linux / macOS)
sqlite3 — это консольная утилита. Ты можешь использовать либо:

Встроенную консоль (терминал), либо

Программу DB Browser for SQLite (с интерфейсом)

✅ Способ 1: Через терминал (sqlite3)
Открой терминал (в Windows — cmd, в macOS/Linux — Terminal).

Введи команду:

nginx
Копировать
Редактировать
sqlite3 mydatabase.db
Это создаст файл mydatabase.db и откроет сессию работы с базой.

Создай таблицу:

sql
Копировать
Редактировать
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
Добавь данные:

sql
Копировать
Редактировать
INSERT INTO users (name, age) VALUES ('Alice', 25);
Проверь результат:

sql
Копировать
Редактировать
SELECT * FROM users;
Выйди из базы:

Копировать
Редактировать
.quit
✅ Способ 2: Через DB Browser for SQLite (если ты визуал)
Открой программу.

Нажми File → New Database

Дай имя, например: mydata.sqlite

В открывшемся окне нажми "Create Table"

Добавь поля (например: id, name, age) → Сохрани

Во вкладке "Browse Data" добавляй и смотри записи

📝 Быстрый шаблон кода для SQLite
sql
Копировать
Редактировать
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    title TEXT,
    price REAL
);

INSERT INTO products (title, price) VALUES ('Товар 1', 99.99);
SELECT * FROM products;