from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import (
    LoginView, SignupView, InputView, AudioUploadViewSet,
    Input1View, ApplicationViewSet, CalendarEventViewSet
)

router = routers.DefaultRouter()
router.register(r'login', LoginView, basename='login')
router.register(r'signup', SignupView, basename='signup')
router.register(r'input', InputView, basename='input')
router.register(r'upload', AudioUploadViewSet, basename='upload')
router.register(r'input1', Input1View, basename='input1')
router.register(r'applications', ApplicationViewSet, basename='applications')
router.register(r'calendar', CalendarEventViewSet, basename='calendar')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
