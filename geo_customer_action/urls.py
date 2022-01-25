from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'geo-customer-action'

router = routers.DefaultRouter()
router.register(r'actions', views.ActionView)

urlpatterns = [
    path(str(), include(router.urls)),
]
