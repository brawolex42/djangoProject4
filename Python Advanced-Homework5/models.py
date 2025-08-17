# Python Advanced: Домашнее задание 5
#
# Цели задания:
# Расширить функциональность существующего API для поддержки категорий вопросов.
#
# Задачи:
# Создание модели Category:
#
# Создайте новую модель Category с использованием SQLAlchemy в модуле models.
#
# Модель должна содержать следующие поля:
#
# id: первичный ключ, целое число, авто-инкремент.
#
# name: строка, название категории, не должно быть пустым.
#
# Модель Question должна быть обновлена, чтобы включить ссылку на Category через внешний ключ.
# Миграция базы данных:
# Создайте новую миграцию для добавления таблицы категорий и обновления таблицы вопросов с использованием Flask-Migrate.


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    questions = db.relationship("Question", back_populates="category", passive_deletes=True)

class Question(db.Model):
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id", ondelete="SET NULL"), nullable=True, index=True)
    category = db.relationship("Category", back_populates="questions")
