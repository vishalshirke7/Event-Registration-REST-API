from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email and password:
            raise ValidationError("Username and Password is required")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("This email address does not exist")
        if user.password == password:
            data["user_id"] = user.id
            return data
        else:
            raise ValidationError("Invalid credentials")


