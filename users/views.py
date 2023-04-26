from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import PermissionAdmin

from .models import User
from .serializers import UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer
