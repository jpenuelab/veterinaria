from django.urls import path, include
from .views import TipoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tipo', TipoViewSet, basename='tipo')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
