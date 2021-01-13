from rest_framework.generics import CreateAPIView
from .models import CustomUser
from .serializers import UserSerializer

class UserAndNurseryCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()