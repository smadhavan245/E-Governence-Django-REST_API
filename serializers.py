from rest_framework import serializers
from .models import Login, Signup, Input, AudioUpload, Input1, Application, CalendarEvent

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = '__all__'

class Input1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Input1
        fields = '__all__'

class AudioUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioUpload
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class CalendarEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvent
        fields = '__all__'
