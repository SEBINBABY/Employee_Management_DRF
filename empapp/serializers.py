from rest_framework import serializers
from .models import Employee
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'role', 'date_joined']

    # Ensure validation , name is not empty
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name should not be empty.")
        return value

    # Ensure validation , email is unique and valid
    def validate_email(self, value):
        # Check if email is unique
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        # Validate email format
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Enter a valid email address.")
        return value

