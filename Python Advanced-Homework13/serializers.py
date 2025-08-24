# Python Advanced: Домашнее задание 13
#
# Домашнее задание: Проект "Менеджер задач" — Создание и настройка сериализаторов и добавление представлений
# Цель:
# Освоить настройку сериализаторов для работы с подзадачами и категориями, включая переопределение полей, использование вложенных сериализаторов, методов create и update, а также классы представлений.
#
# Задание 1: Переопределение полей сериализатора
# Создайте SubTaskCreateSerializer, в котором поле created_at будет доступно только для чтения (read_only).
#
# Шаги для выполнения:
#
# Определите SubTaskCreateSerializer в файле serializers.py.
#
# Переопределите поле created_at как read_only.
#
#
# Задание 2: Переопределение методов create и update
# Создайте сериализатор для категории CategoryCreateSerializer, переопределив методы create и update для проверки уникальности названия категории. Если категория с таким названием уже существует, возвращайте ошибку валидации.
#
# Шаги для выполнения:
#
# Определите CategoryCreateSerializer в файле serializers.py.
#
# Переопределите метод create для проверки уникальности названия категории.
#
# Переопределите метод update для аналогичной проверки при обновлении.
#
#
#
# Задание 3: Использование вложенных сериализаторов
# Создайте сериализатор для TaskDetailSerializer, который включает вложенный сериализатор для полного отображения связанных подзадач (SubTask). Сериализатор должен показывать все подзадачи, связанные с данной задачей.
#
# Шаги для выполнения:
#
# Определите TaskDetailSerializer в файле serializers.py.
#
# Вложите SubTaskSerializer внутрь TaskDetailSerializer.
#
#
#
# Задание 4: Валидация данных в сериализаторах
# Создайте TaskCreateSerializer и добавьте валидацию для поля deadline, чтобы дата не могла быть в прошлом. Если дата в прошлом, возвращайте ошибку валидации.
#
# Шаги для выполнения:
#
# Определите TaskCreateSerializer в файле serializers.py.
#
# Переопределите метод validate_deadline для проверки даты.
#
#
# Задание 5: Создание классов представлений
# Создайте классы представлений для работы с подзадачами (SubTasks), включая создание, получение, обновление и удаление подзадач. Используйте классы представлений (APIView) для реализации этого функционала.
#
# Шаги для выполнения:
#
# Создайте классы представлений для создания и получения списка подзадач (SubTaskListCreateView).
#
# Создайте классы представлений для получения, обновления и удаления подзадач (SubTaskDetailUpdateDeleteView).
#
# Добавьте маршруты в файле urls.py, чтобы использовать эти классы.
#
# from rest_framework import serializers
# from .models import Task, Subtask, Category, Status
# from django.utils import timezone
#
#
# class SubTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subtask
#         fields = ["id", "task", "title", "status", "created_at"]
#
#
# class SubTaskCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subtask
#         fields = ["id", "task", "title", "status", "created_at"]
#         read_only_fields = ["id", "created_at"]
#
# 
# class CategoryCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ["id", "name"]
#
#     def create(self, validated_data):
#         name = validated_data.get("name", "")
#         if Category.objects.filter(name__iexact=name).exists():
#             raise serializers.ValidationError({"name": "Категория с таким названием уже существует."})
#         return super().create(validated_data)
#
#     def update(self, instance, validated_data):
#         name = validated_data.get("name", instance.name)
#         if Category.objects.filter(name__iexact=name).exclude(pk=instance.pk).exists():
#             raise serializers.ValidationError({"name": "Категория с таким названием уже существует."})
#         instance.name = name
#         instance.save()
#         return instance
#
#
# class TaskCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ["id", "title", "description", "status", "deadline", "created_at", "updated_at"]
#         read_only_fields = ["id", "created_at", "updated_at"]
#
#     def validate_deadline(self, value):
#         if value and value < timezone.now().date():
#             raise serializers.ValidationError("Дедлайн не может быть в прошлом.")
#         return value
#
#
# class TaskDetailSerializer(serializers.ModelSerializer):
#     subtasks = SubTaskSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Task
#         fields = ["id", "title", "description", "status", "deadline", "created_at", "updated_at", "subtasks"]
#
#
#
#
#
#
#
#
#
#
