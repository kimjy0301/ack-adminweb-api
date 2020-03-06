from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import psutil
from rest_framework import permissions
from .serializers import (
    ServerStatusSerializer,
    EmrifYearSerializer,
    EmrifWeekSerializer,
    EmrifDeptSerializer,
)
from emrif.models import EmrifAib, EmrifError
import datetime


class ServerStatusView(APIView):
    pagination_class = None
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        memory = psutil.virtual_memory()
        cpu = psutil.cpu_percent()
        disk = psutil.disk_usage("C:/")

        total_memory = round(memory.total / (1024 ** 3), 1)
        free_memory = round(memory.available / (1024 ** 3), 1)
        percent_memory = memory.percent
        used_memory = round(memory.used / (1024 ** 3), 1)

        total_disk = round(disk.total / (1024 ** 3), 1)
        free_disk = round(disk.free / (1024 ** 3), 1)
        used_disk = round(disk.used / (1024 ** 3), 1)
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


class EmrifYearView(APIView):
    pagination_class = None
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        year = request.GET.get("year", None)
        filter_kwargs = {}
        if year is None:
            year = datetime.datetime.now().year
        data = []

        for month in range(1, 13):
            filter_kwargs["created__year"] = year
            filter_kwargs["created__month"] = month
            month_send_count = EmrifAib.objects.filter(**filter_kwargs).count()
            month_error_count = EmrifError.objects.filter(**filter_kwargs).count()
            tempdata = {
                "month": f"{month}월",
                "send_count": month_send_count,
                "error_count": month_error_count,
            }
            data.append(tempdata)
        serializer = EmrifYearSerializer(data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EmrifWeekView(APIView):
    pagination_class = None
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        year = request.GET.get("year", None)
        filter_kwargs = {}
        if year is None:
            year = datetime.datetime.now().year
        data = []

        week = request.GET.get("week", None)
        filter_kwargs = {}
        if week is None:
            week = datetime.datetime.now().isocalendar()[1]

        filter_kwargs["created__year"] = year
        filter_kwargs["created__week"] = week

        month_send_count = EmrifAib.objects.filter(**filter_kwargs).count()
        month_error_count = EmrifError.objects.filter(**filter_kwargs).count()
        data = {
            "send_count": month_send_count,
            "error_count": month_error_count,
        }
        serializer = EmrifWeekSerializer(data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EmrifDeptView(APIView):
    pagination_class = None
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        year = request.GET.get("year", None)
        filter_kwargs = {}
        if year is None:
            year = datetime.datetime.now().year
        month = request.GET.get("month", None)
        filter_kwargs = {}
        if month is None:
            month = datetime.datetime.now().month

        dept = request.GET.get("dept", None)
        deptList = dept.split(",")
        if dept is None:
            pass
        data = []

        filter_kwargs = {}
        for dept in deptList:
            filter_kwargs["created__year"] = year
            filter_kwargs["created__month"] = month
            filter_kwargs["emrifpc__equip__lab__dept__name"] = dept
            month_send_count = EmrifAib.objects.filter(**filter_kwargs).count()
            month_error_count = EmrifError.objects.filter(**filter_kwargs).count()
            tempdata = {
                "dept": dept,
                "send_count": month_send_count,
                "error_count": month_error_count,
            }
            data.append(tempdata)
        serializer = EmrifDeptSerializer(data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
