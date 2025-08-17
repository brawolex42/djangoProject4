# Python Advanced: Домашнее задание 8
# # Домашнее задание: Проект "Менеджер задач"
# Цель:
# Создать структуру менеджера задач и зарегистрировать модели в панели администратора Django.
# # Реализовать модели:
# Модель Task:
## Описание: Задача для выполнения.
## Поля:
## title: Название задачи. Уникально для даты.
## description: Описание задачи.
## categories: Категории задачи. Многие ко многим.
## status: Статус задачи. Выбор из: New, In progress, Pending, Blocked, Done
## deadline: Дата и время дедлайн.
## created_at: Дата и время создания. Автоматическое заполнение.
## Модель SubTask:
## Описание: Отдельная часть основной задачи (Task).
## Поля:
## title: Название подзадачи.
## description: Описание подзадачи.
## task: Основная задача. Один ко многим.
## status: Статус задачи. Выбор из: New, In progress, Pending, Blocked, Done
## deadline: Дата и время дедлайн.
# # created_at: Дата и время создания. Автоматическое заполнение.
# # Модель Category:
# # Описание: Категория выполнения.
# # Поля:
# # name: Название категории.
# # Шаги для выполнения задания:
# Создайте модели:
# # В файле models.py вашего приложения добавьте модели с указанными полями и описаниями.
# # Создайте миграции:
# # Выполните команду для создания миграций:
# # Примените миграции:
# # Выполните команду для применения миграций:
# # Зарегистрируйте модели в админке:
# # В файле admin.py вашего приложения зарегистрируйте все модели.
# # Зафиксируйте изменения в гит:
# # Создайте новый коммит и запушьте его в ваш гит.
# # Создайте записи через админку:
# # Создайте суперпользователя
# # Перейдите в административную панель Django.
# # Добавьте несколько объектов для каждой модели.
# # Оформите ответ:
# # Прикрепите ссылку на гит и скриншоты где видны созданные объекты к ответу на домашнее задание.

from django.db import models

class Status(models.TextChoices):
    NEW = "new", "New"
    IN_PROGRESS = "in_progress", "In progress"
    PENDING = "pending", "Pending"
    BLOCKED = "blocked", "Blocked"
    DONE = "done", "Done"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200, unique_for_date="created_at")
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, related_name="tasks", blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} [{self.get_status_display()}]"

class SubTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    task = models.ForeignKey(Task, related_name="subtasks", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} → {self.task_id}"
