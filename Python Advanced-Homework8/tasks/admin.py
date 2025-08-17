from django.contrib import admin
from .models import Category, Task, SubTask

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 0

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "deadline", "created_at")
    list_filter = ("status", "categories")
    search_fields = ("title", "description")
    date_hierarchy = "created_at"
    inlines = [SubTaskInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "task", "status", "deadline", "created_at")
    list_filter = ("status",)
    search_fields = ("title", "description")
#python manage.py makemigrations tasks
#python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver
# http://127.0.0.1:8000/admin — создай несколько Category, Task и SubTask

