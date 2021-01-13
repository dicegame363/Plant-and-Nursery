from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,CreateAPIView,ListAPIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from .models import Plant,Order
from .serializers import PlantSerializer,OrderSerializer
from .permissions import IsUserCreate_IsNurseryList,IsUser,IsNurseryCreate_IsUserList
from rest_framework.permissions import IsAuthenticated

class PlantListCreateAPIView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsNurseryCreate_IsUserList]
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()

class PlantRetrieveAPIView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUser]
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()

class OrderListCreateAPIView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsUserCreate_IsNurseryList]
    serializer_class = OrderSerializer

    def get_queryset(self):
        uniques = set()
        for obj in Order.objects.filter(plants__plant__nursery__owner=self.request.user):
            uniques.add(obj)
        return uniques