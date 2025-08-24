# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from .models import Subtask
# from .serializers import SubTaskSerializer, SubTaskCreateSerializer
#
#
# class SubTaskListCreateView(APIView):
#     def get(self, request):
#         qs = Subtask.objects.select_related("task").order_by("-created_at")
#         data = SubTaskSerializer(qs, many=True).data
#         return Response(data)
#
#     def post(self, request):
#         serializer = SubTaskCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             obj = serializer.save()
#             return Response(SubTaskSerializer(obj).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SubTaskDetailUpdateDeleteView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Subtask, pk=pk)
#
#     def get(self, request, pk):
#         obj = self.get_object(pk)
#         return Response(SubTaskSerializer(obj).data)
#
#     def put(self, request, pk):
#         obj = self.get_object(pk)
#         serializer = SubTaskCreateSerializer(obj, data=request.data)
#         if serializer.is_valid():
#             obj = serializer.save()
#             return Response(SubTaskSerializer(obj).data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk):
#         obj = self.get_object(pk)
#         serializer = SubTaskCreateSerializer(obj, data=request.data, partial=True)
#         if serializer.is_valid():
#             obj = serializer.save()
#             return Response(SubTaskSerializer(obj).data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         obj = self.get_object(pk)
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
