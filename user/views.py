from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from .permissions import IsSelf
from datetime import datetime, timedelta
import jwt
from django.conf import settings


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAdminUser]
        elif (
            self.action == "create"
            or self.action == "retrieve"
            or self.action == "favs"
        ):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsSelf]

        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["POST"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(
                data="사용자명,패스워드를 입력해주세요.", status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode(
                {"pk": user.pk, "exp": datetime.utcnow() + timedelta(hours=9000)},
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            return Response(
                data={"token": encoded_jwt, "id": user.pk}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                data="해당 정보와 일치하는 유저가 없습니다.", status=status.HTTP_401_UNAUTHORIZED
            )

    # @action(detail=True)
    # def favs(self, request, pk):
    #     user = self.get_object()
    #     serializer = RoomSerializer(user.favs.all(), many=True)
    #     return Response(serializer.data)

    # @favs.mapping.put
    # def toggle_favs(self, request, pk):
    #     print(request.data)
    #     pk = request.data.get("pk", None)
    #     user = self.get_object()
    #     if pk is not None:
    #         try:
    #             room = Room.objects.get(pk=pk)
    #             if room in user.favs.all():
    #                 user.favs.remove(room)
    #             else:
    #                 user.favs.add(room)
    #             serializer = RoomSerializer(user.favs.all(), many=True)
    #             return Response(serializer.data)
    #         except Room.DoesNotExist:
    #             pass
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
