from rest_framework.viewsets import ModelViewSet
from .serializers import (
    EmrifPcSerializer,
    EmrifDeptSerializer,
    EmrifEquipSerializer,
    EmrifErrorSerializer,
    EmrifLabSerializer,
    EmrifAIBSerializer,
)
from .models import EmrifPc, EmrifDept, EmrifEquip, EmrifError, EmrifLab, EmrifAib
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class EmrifPcViewSet(ModelViewSet):
    queryset = EmrifPc.objects.all()
    serializer_class = EmrifPcSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    @action(detail=False, url_path="search")
    def search(self, request):

        dept = request.GET.get("dept", None)
        deptname = request.GET.get("deptname", None)
        lab = request.GET.get("lab", None)
        labname = request.GET.get("labname", None)

        filter_kwargs = {}
        if dept is not None:
            filter_kwargs["equip__lab__dept"] = dept
        if deptname is not None:
            filter_kwargs["equip__lab__dept__name"] = deptname
        if lab is not None:
            filter_kwargs["equip__lab"] = lab
        if labname is not None:
            filter_kwargs["equip__lab__name"] = labname

        paginator = self.paginator
        try:
            emrifpcs = EmrifPc.objects.filter(**filter_kwargs)
        except ValueError:
            emrifpcs = EmrifPc.objects.all()
        results = paginator.paginate_queryset(emrifpcs, request)
        serializer = EmrifPcSerializer(
            instance=results, many=True, context={"request": request}
        )

        return paginator.get_paginated_response(serializer.data)


class EmrifDeptViewSet(ModelViewSet):
    queryset = EmrifDept.objects.all()
    serializer_class = EmrifDeptSerializer
    paginator = None

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]


class EmrifEquipViewSet(ModelViewSet):
    queryset = EmrifEquip.objects.all()
    serializer_class = EmrifEquipSerializer
    paginator = None

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]


class EmrifErrorViewSet(ModelViewSet):
    queryset = EmrifError.objects.all()
    serializer_class = EmrifErrorSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]


class EmrifLabViewSet(ModelViewSet):
    queryset = EmrifLab.objects.all()
    serializer_class = EmrifLabSerializer
    paginator = None

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    @action(detail=False, url_path="search")
    def search(self, request):

        floor = request.GET.get("floor", None)

        filter_kwargs = {}
        if floor is not None:
            filter_kwargs["floor"] = floor
        try:
            emrifLabs = EmrifLab.objects.filter(**filter_kwargs)
        except ValueError:
            emrifLabs = EmrifLab.objects.all()
        serializer = EmrifLabSerializer(instance=emrifLabs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EmrifAibViewSet(ModelViewSet):
    queryset = EmrifAib.objects.all()
    serializer_class = EmrifAIBSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    @action(detail=False, url_path="search")
    def search(self, request):

        floor = request.GET.get("floor", None)

        filter_kwargs = {}
        if floor is not None:
            filter_kwargs["floor"] = floor
        try:
            emrifLabs = EmrifLab.objects.filter(**filter_kwargs)
        except ValueError:
            emrifLabs = EmrifLab.objects.all()
        serializer = EmrifLabSerializer(instance=emrifLabs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
