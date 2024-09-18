from django.urls import path,include
from rest_framework import routers
from .views import(
    CommodityViewSet
)
router = routers.DefaultRouter()
router.register(r'commodities',CommodityViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
]