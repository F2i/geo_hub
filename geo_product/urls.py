from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'geo-product'

router = routers.DefaultRouter()
router.register(r'geo-products', views.GeoProductView)

urlpatterns = [
    path(str(), include(router.urls)),
]
