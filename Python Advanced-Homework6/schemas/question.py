# Python Advanced: Домашнее задание 6
#
# Цели задания:
# Расширить функциональность существующего API для поддержки категорий вопросов.
#
# Задачи:
# Обновление схем Pydantic:
#
# Добавьте новую схему CategoryBase в schemas/question.py для сериализации и валидации данных категории.
#
# Обновите схему QuestionCreate и QuestionResponse для интеграции данных о категории.
#
# Разработка API эндпоинтов:
#
# Создайте новые эндпоинты для создания, чтения, обновления и удаления категорий.
#
# POST /categories: создание новой категории.
#
# GET /categories: получение списка всех категорий.
#
# PUT /categories/{id}: обновление категории по ID.
#
# DELETE /categories/{id}: удаление категории по ID.
#
# Обновите существующие эндпоинты вопросов, чтобы они поддерживали работу с категориями.
#
# GET /questions: должен возвращать вопросы с информацией о категориях.
#
# POST /questions: должен позволять указывать категорию при создании вопроса.



from typing import Optional
from pydantic import BaseModel, ConfigDict

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    category_id: Optional[int] = None

class QuestionUpdate(BaseModel):
    text: Optional[str] = None
    category_id: Optional[int] = None

class QuestionResponse(QuestionBase):
    id: int
    category: Optional[CategoryResponse] = None
    model_config = ConfigDict(from_attributes=True)
