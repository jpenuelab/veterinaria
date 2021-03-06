from django.urls import path, include
from .views import RazaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('raza', RazaViewSet, basename='raza')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
