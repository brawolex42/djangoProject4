
# Домашнее задание: Проект "Менеджер задач" — продолжение
# Цель:
# Добавить строковое представление (str) и метаданные (Meta) к моделям менеджера задач, а также настроить административную панель для удобного управления этими моделями.
# 1. Реализуйте изменения в моделях:
# Модель Task:
# Добавить метод str, который возвращает название задачи.
# Добавить класс Meta с настройками:
# Имя таблицы в базе данных: 'task_manager_task'.
# Сортировка по убыванию даты создания.
# Человекочитаемое имя модели: 'Task'.
# Уникальность по полю 'title'.
# Модель SubTask:
# Добавить метод str, который возвращает название подзадачи.
# Добавить класс Meta с настройками:
# Имя таблицы в базе данных: 'task_manager_subtask'.
# Сортировка по убыванию даты создания.
# Человекочитаемое имя модели: 'SubTask'.
# Уникальность по полю 'title'.
# Модель Category:
# Добавить метод str, который возвращает название категории.
# Добавить класс Meta с настройками:
# Имя таблицы в базе данных: 'task_manager_category'.
# Человекочитаемое имя модели: 'Category'.
# Уникальность по полю 'name'.
#
# 2. Настройте отображение моделей в админке:
# В файле admin.py вашего приложения добавьте классы администратора для настройки отображения моделей Task, SubTask и Category.
# 3. Зафиксируйте изменения в гит:
# Создайте новый коммит и запушьте его в ваш гит.
# 4. Создайте записи через админку:
# 1. Создайте суперпользователя.
# 2. Перейдите в административную панель Django.
# 3. Добавьте несколько объектов для каждой модели.
# 5. Оформите ответ:
# Прикрепите ссылку на гит и скриншоты, где видны созданные объекты к ответу на домашнее задание.



from django.db import models

class Status(models.TextChoices):
    NEW = "new", "New"
    IN_PROGRESS = "in_progress", "In progress"
    PENDING = "pending", "Pending"
    BLOCKED = "blocked", "Blocked"
    DONE = "done", "Done"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "task_manager_category"
        verbose_name = "Category"

class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, related_name="tasks", blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_task"
        ordering = ["-created_at"]
        verbose_name = "Task"

class SubTask(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    task = models.ForeignKey(Task, related_name="subtasks", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_subtask"
        ordering = ["-created_at"]
        verbose_name = "SubTask"

# python manage.py makemigrations tasks
# python manage.py migrate
# python manage.py createsuperuser
# python manage.py runserver
