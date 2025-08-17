#Задача 1: Наполнение данными
#Добавьте в базу данных следующие категории и продукты
#Добавление категорий: Добавьте в таблицу categories следующие категории:
#Название: "Электроника", Описание: "Гаджеты и устройства."
#Название: "Книги", Описание: "Печатные книги и электронные книги."
#Название: "Одежда", Описание: "Одежда для мужчин и женщин."
#Добавление продуктов: Добавьте в таблицу products следующие продукты, убедившись, что каждый продукт связан с соответствующей категорией:
#Название: "Смартфон", Цена: 299.99, Наличие на складе: True, Категория: Электроника
#Название: "Ноутбук", Цена: 499.99, Наличие наHomewor складе: True, Категория: Электроника
#Название: "Научно-фантастический роман", Цена: 15.99, Наличие на складе: True, Категория: Книги
#Название: "Джинсы", Цена: 40.50, Наличие на складе: True, Категория: Одежда
#Название: "Футболка", Цена: 20.00, Наличие на складе: True, Категория: Одежда
#Задача 2: Чтение данных
#Извлеките все записи из таблицы categories. Для каждой категории извлеките и выведите все связанные с ней продукты, включая их названия и цены.
#Задача 3: Обновление данных
#Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 349.99.
#Задача 4: Агрегация и группировка
#Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой категории.
#Задача 5: Группировка с фильтрацией
#Отфильтруйте и выведите только те категории, в которых более одного продукта.

-- БД и выбор схемы
CREATE DATABASE IF NOT EXISTS shopdb
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE shopdb;

-- Таблицы
CREATE TABLE IF NOT EXISTS categories (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL UNIQUE,
  description VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(150) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  in_stock TINYINT(1) NOT NULL DEFAULT 1,
  category_id INT NOT NULL,
  UNIQUE KEY uq_products_name_category (name, category_id),
  CONSTRAINT fk_products_category
    FOREIGN KEY (category_id) REFERENCES categories(id)
      ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Задача 1: категории
INSERT INTO categories (name, description) VALUES
  ('Электроника', 'Гаджеты и устройства.'),
  ('Книги', 'Печатные книги и электронные книги.'),
  ('Одежда', 'Одежда для мужчин и женщин.')
ON DUPLICATE KEY UPDATE description = VALUES(description);

-- Задача 1: продукты
INSERT INTO products (name, price, in_stock, category_id)
SELECT 'Смартфон', 299.99, 1, c.id FROM categories c WHERE c.name='Электроника'
ON DUPLICATE KEY UPDATE price=VALUES(price), in_stock=VALUES(in_stock), category_id=VALUES(category_id);

INSERT INTO products (name, price, in_stock, category_id)
SELECT 'Ноутбук', 499.99, 1, c.id FROM categories c WHERE c.name='Электроника'
ON DUPLICATE KEY UPDATE price=VALUES(price), in_stock=VALUES(in_stock), category_id=VALUES(category_id);

INSERT INTO products (name, price, in_stock, category_id)
SELECT 'Научно-фантастический роман', 15.99, 1, c.id FROM categories c WHERE c.name='Книги'
ON DUPLICATE KEY UPDATE price=VALUES(price), in_stock=VALUES(in_stock), category_id=VALUES(category_id);

INSERT INTO products (name, price, in_stock, category_id)
SELECT 'Джинсы', 40.50, 1, c.id FROM categories c WHERE c.name='Одежда'
ON DUPLICATE KEY UPDATE price=VALUES(price), in_stock=VALUES(in_stock), category_id=VALUES(category_id);

INSERT INTO products (name, price, in_stock, category_id)
SELECT 'Футболка', 20.00, 1, c.id FROM categories c WHERE c.name='Одежда'
ON DUPLICATE KEY UPDATE price=VALUES(price), in_stock=VALUES(in_stock), category_id=VALUES(category_id);

-- Задача 2: чтение (категории + их продукты)
SELECT
  c.id   AS category_id,
  c.name AS category_name,
  c.description,
  p.id   AS product_id,
  p.name AS product_name,
  p.price
FROM categories c
LEFT JOIN products p ON p.category_id = c.id
ORDER BY c.name, p.name;

-- Задача 3: обновить цену ПЕРВОГО "Смартфона"
UPDATE products
SET price = 349.99
WHERE name = 'Смартфон'
ORDER BY id
LIMIT 1;

-- Проверка
SELECT id, name, price FROM products WHERE name='Смартфон' ORDER BY id;

-- Задача 4: агрегирование (кол-во продуктов по категориям)
SELECT
  c.id   AS category_id,
  c.name AS category_name,
  COUNT(p.id) AS product_count
FROM categories c
LEFT JOIN products p ON p.category_id = c.id
GROUP BY c.id, c.name
ORDER BY c.name;

-- Задача 5: категории, где более одного продукта
SELECT
  c.id   AS category_id,
  c.name AS category_name,
  COUNT(p.id) AS product_count
FROM categories c
JOIN products p ON p.category_id = c.id
GROUP BY c.id, c.name
HAVING COUNT(p.id) > 1
ORDER BY product_count DESC, c.name;
