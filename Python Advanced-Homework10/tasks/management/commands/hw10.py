# Python Advanced: Домашнее задание 10
#
# Домашнее задание: Проект "Менеджер задач" — ORM запросы
# Цель:
# Освоение основных операций CRUD (Create, Read, Update, Delete) на примере заданных моделей.
#
# Выполните запросы:
#
# Создание записей:
#
# Task:
#
# title: "Prepare presentation".
#
# description: "Prepare materials and slides for the presentation".
#
# status: "New".
#
# deadline: Today's date + 3 days.
#
# SubTasks для "Prepare presentation":
#
# title: "Gather information".
#
# description: "Find necessary information for the presentation".
#
# status: "New".
#
# deadline: Today's date + 2 days.
#
# title: "Create slides".
#
# description: "Create presentation slides".
#
# status: "New".
#
# deadline: Today's date + 1 day.
#
# Чтение записей:
#
# Tasks со статусом "New":
#
# Вывести все задачи, у которых статус "New".
#
# SubTasks с просроченным статусом "Done":
#
# Вывести все подзадачи, у которых статус "Done", но срок выполнения истек.
#
# Изменение записей:
#
# Измените статус "Prepare presentation" на "In progress".
#
# Измените срок выполнения для "Gather information" на два дня назад.
#
# Измените описание для "Create slides" на "Create and format presentation slides".
#
# Удаление записей:
#
# Удалите задачу "Prepare presentation" и все ее подзадачи.
#
#
# Оформите ответ:
# Прикрепите все выполненные запросы (код) и скриншоты с консоли к ответу на домашнее задание




# from datetime import timedelta
# from django.utils import timezone
# from tasks.models import Task, SubTask, Status
#
# now = timezone.now()
#
#
# task, _ = Task.objects.update_or_create(
#     title="Prepare presentation",
#     defaults={
#         "description": "Prepare materials and slides for the presentation",
#         "status": Status.NEW,
#         "deadline": now + timedelta(days=3),
#     },
# )
# st1, _ = SubTask.objects.update_or_create(
#     title="Gather information",
#     defaults={
#         "description": "Find necessary information for the presentation",
#         "status": Status.NEW,
#         "deadline": now + timedelta(days=2),
#         "task": task,
#     },
# )
# st2, _ = SubTask.objects.update_or_create(
#     title="Create slides",
#     defaults={
#         "description": "Create presentation slides",
#         "status": Status.NEW,
#         "deadline": now + timedelta(days=1),
#         "task": task,
#     },
# )
# print("CREATE:", task, st1, st2, sep="\n")
#
# # READ
# print("\nREAD — Tasks with NEW:")
# for t in Task.objects.filter(status=Status.NEW):
#     print(t.id, t.title, t.status, t.deadline)
#
# print("\nREAD — SubTasks DONE & overdue:")
# for s in SubTask.objects.filter(status=Status.DONE, deadline__lt=now):
#     print(s.id, s.title, s.status, s.deadline)
#
#
# task = Task.objects.get(title="Prepare presentation")
# task.status = Status.IN_PROGRESS
# task.save()
# st1 = SubTask.objects.get(title="Gather information")
# st1.deadline = now - timedelta(days=2)
# st1.save()
# st2 = SubTask.objects.get(title="Create slides")
# st2.description = "Create and format presentation slides"
# st2.save()
# print("\nUPDATE:", task, st1.deadline, st2.description)
#
# Task.objects.filter(title="Prepare presentation").delete()
# print("\nDELETE — Task and related SubTasks removed.")
#
from datetime import timedelta
from django.utils import timezone
from tasks.models import Task, SubTask, Status

now = timezone.now()

# CREATE
task, _ = Task.objects.update_or_create(
    title="Prepare presentation",
    defaults={
        "description": "Prepare materials and slides for the presentation",
        "status": Status.NEW,
        "deadline": now + timedelta(days=3),
    },
)
st1, _ = SubTask.objects.update_or_create(
    title="Gather information",
    defaults={
        "description": "Find necessary information for the presentation",
        "status": Status.NEW,
        "deadline": now + timedelta(days=2),
        "task": task,
    },
)
st2, _ = SubTask.objects.update_or_create(
    title="Create slides",
    defaults={
        "description": "Create presentation slides",
        "status": Status.NEW,
        "deadline": now + timedelta(days=1),
        "task": task,
    },
)
print("CREATE:", task, st1, st2, sep="\n")

# READ
print("\nREAD — Tasks with NEW:")
for t in Task.objects.filter(status=Status.NEW):
    print(t.id, t.title, t.status, t.deadline)

print("\nREAD — SubTasks DONE & overdue:")
for s in SubTask.objects.filter(status=Status.DONE, deadline__lt=now):
    print(s.id, s.title, s.status, s.deadline)

# UPDATE
task = Task.objects.get(title="Prepare presentation")
task.status = Status.IN_PROGRESS
task.save()
st1 = SubTask.objects.get(title="Gather information")
st1.deadline = now - timedelta(days=2)
st1.save()
st2 = SubTask.objects.get(title="Create slides")
st2.description = "Create and format presentation slides"
st2.save()
print("\nUPDATE:", task, st1.deadline, st2.description)

# DELETE
Task.objects.filter(title="Prepare presentation").delete()
print("\nDELETE — Task and related SubTasks removed.")
