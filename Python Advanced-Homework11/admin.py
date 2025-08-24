from django.contrib import admin
from django import forms
from .models import Task, Subtask, Status


class SubtaskInline(admin.TabularInline):
    model = Subtask
    extra = 1
    fields = ("title", "status")
    show_change_link = True
    verbose_name = "Подзадача"
    verbose_name_plural = "Подзадачи"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubtaskInline]
    list_display = ("id", "short_title", "subtasks_total", "created_at")
    list_display_links = ("short_title",)
    search_fields = ("title",)
    ordering = ("-created_at",)

    @admin.display(description="Название", ordering="title")
    def short_title(self, obj: Task):
        name = obj.title or ""
        return name if len(name) <= 10 else f"{name[:10]}..."

    @admin.display(description="Подзадач")
    def subtasks_total(self, obj: Task):
        return obj.subtasks.count()


class SubtaskAdminForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["task"].label_from_instance = lambda task: task.title


@admin.action(description="Перевести выбранные подзадачи в статус Done")
def make_done(modeladmin, request, queryset):
    queryset.exclude(status=Status.DONE).update(status=Status.DONE)


@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    form = SubtaskAdminForm
    list_display = ("id", "title", "task", "status", "created_at")
    list_filter = ("status", "task")
    search_fields = ("title", "task__title")
    actions = [make_done]
    ordering = ("-created_at",)
