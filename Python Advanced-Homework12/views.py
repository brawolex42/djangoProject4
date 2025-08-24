# from django.utils import timezone
# from django.db.models import Count
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Task, Status
# from .serializers import TaskSerializer
#
# class TaskListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Task.objects.all().order_by("-created_at")
#     serializer_class = TaskSerializer
#
# class TaskRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     lookup_field = "pk"
#
# class TaskStatsAPIView(APIView):
#     def get(self, request):
#         total = Task.objects.count()
#         by_status_raw = Task.objects.values("status").annotate(c=Count("id"))
#         by_status = {s.value: 0 for s in Status}
#         for row in by_status_raw:
#             by_status[row["status"]] = row["c"]
#         today = timezone.now().date()
#         overdue = Task.objects.filter(deadline__isnull=False, deadline__lt=today).exclude(status=Status.DONE).count()
#         return Response({"total": total, "by_status": by_status, "overdue": overdue})
