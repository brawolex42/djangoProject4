from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveAPIView, TaskStatsAPIView

urlpatterns = [
    path("api/tasks/", TaskListCreateAPIView.as_view(), name="tasks-list-create"),
    path("api/tasks/<int:pk>/", TaskRetrieveAPIView.as_view(), name="tasks-detail"),
    path("api/tasks/stats/", TaskStatsAPIView.as_view(), name="tasks-stats"),
]
