from rest_framework import serializers
from authentication.models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class RegisterSerializer(serializers.ModelSerializer):
    """Registration for users"""
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']

    def validate(self, attrs):
        password = attrs.get('password', '')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({
                'password': "Password и Confirm Password don't match!",
                'confirm_password': "Password и Confirm Password don't match!"
            }
            )
        try:
            validators.validate_password(password=password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        attrs.pop('confirm_password', None)
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    """Login for users"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
