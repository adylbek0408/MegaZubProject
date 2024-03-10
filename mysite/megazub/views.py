from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
# from .permissions import IsOwnerOrReadOnly


class CarouselItemViewSets(viewsets.ModelViewSet):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer
    permission_classes = [permissions.AllowAny]


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ServiceViewSets(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


class ServicePhotosViewSets(viewsets.ModelViewSet):
    queryset = ServicePhotos.objects.all()
    serializer_class = ServicePhotosSerializer
    permission_classes = [permissions.AllowAny]
