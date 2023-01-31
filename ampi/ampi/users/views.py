from drf_yasg import openapi
from rest_framework import viewsets
from ampi.ampi.users.models import User
from ampi.ampi.users.serializers import UserSerializer

filter_query_params = [
    openapi.Parameter('id', openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description='ID пользователя'),
]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []
