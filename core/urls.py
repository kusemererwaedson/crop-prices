from django.urls import path,include
from rest_framework import routers
from . import views
from .views import(
    CommodityViewSet
)
router = routers.DefaultRouter()
router.register(r'commodities',CommodityViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/',include(router.urls)),
]