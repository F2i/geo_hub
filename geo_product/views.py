from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import GeoProductSerializer
from .filters import GeoProductFilter
from core.decorators import request_coming_decorator
# Create your views here.


@method_decorator(request_coming_decorator, name='list')
@method_decorator(request_coming_decorator, name='retrieve')
class GeoProductView(ModelViewSet):
    serializer_class = GeoProductSerializer
    queryset = GeoProductSerializer.Meta.model.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = GeoProductFilter
    ordering_fields = ['price']
    search_fields = ['title']
