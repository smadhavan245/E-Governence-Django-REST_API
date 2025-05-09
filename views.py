# views.py
from rest_framework import viewsets
from .models import Login, Signup, Input, Input1, AudioUpload, Application, CalendarEvent
from .serializers import (
    LoginSerializer, SignupSerializer, InputSerializer, Input1Serializer,
    AudioUploadSerializer, ApplicationSerializer, CalendarEventSerializer
)

class LoginView(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class SignupView(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer

class InputView(viewsets.ModelViewSet):
    queryset = Input.objects.all()
    serializer_class = InputSerializer

class Input1View(viewsets.ModelViewSet):
    queryset = Input1.objects.all()
    serializer_class = Input1Serializer

class AudioUploadViewSet(viewsets.ModelViewSet):
    queryset = AudioUpload.objects.all()
    serializer_class = AudioUploadSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class CalendarEventViewSet(viewsets.ModelViewSet):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer
