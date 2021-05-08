from django.urls import path, include
from rest_framework import routers
from .api.viewsets import CarModelViewSet, PioneerViewSet, SonyViewSet

router = routers.DefaultRouter()
router.register(r'CarModel', CarModelViewSet, basename='CarModel')
router.register(r'Pioneer', PioneerViewSet, basename='Pioneer')
router.register(r'Sony', SonyViewSet, basename='Sony')

app_name = 'polimorfismapp'

urlpatterns = [
    path('api/', include(router.urls)),
]
