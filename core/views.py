from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import psutil
from rest_framework import permissions
from .serializers import ServerStatusSerializer


class ServerStatusView(APIView):
    pagination_class = None
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        memory = psutil.virtual_memory()
        cpu = psutil.cpu_percent()
        disk = psutil.disk_usage("C:/")

        total_memory = round(memory.total / (1024 ** 3), 2)
        free_memory = round(memory.available / (1024 ** 3), 2)
        percent_memory = memory.percent
        used_memory = round(memory.used / (1024 ** 3), 2)

        total_disk = round(disk.total / (1024 ** 3), 2)
        free_disk = round(disk.free / (1024 ** 3), 2)
        used_disk = round(disk.used / (1024 ** 3), 2)
        percent_disk = disk.percent

        data = {
            "total_disk": total_disk,
            "free_disk": free_disk,
            "percent_disk": percent_disk,
            "used_disk": used_disk,
            "total_memory": total_memory,
            "free_memory": free_memory,
            "percent_memory": percent_memory,
            "used_memory": used_memory,
            "cpu": cpu,
        }

        serializer = ServerStatusSerializer(data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
