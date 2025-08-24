# Python Advanced: Домашнее задание 11
# Домашнее задание: Проект "Менеджер задач" — Инлайн формы и Admin actions
# Задание 1:
# Добавить настройку инлайн форм для админ класса задач. При создании задачи должна появиться возможность создавать сразу и подзадачу.
# Задание 2:
# Названия задач могут быть длинными и ухудшать читаемость в Админ панели, поэтому требуется выводить в списке задач укороченный вариант – первые 10 символов с добавлением «...», если название длиннее, при этом при выборе задачи для создания подзадачи должно отображаться полное название. Необходимо реализовать такую возможность.
# Задание 3:
# Реализовать свой action для Подзадач, который поможет выводить выбранные в Админ панели объекты в статус Done

from django.db import models


class Status(models.TextChoices):
    TODO = "todo", "To do"
    IN_PROGRESS = "in_progress", "In progress"
    DONE = "done", "Done"


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
