from rest_framework import serializers

from accounts.models import Student


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    # field-level validation
    def validate_email(self, value):
        if 'admin' in value:
            raise serializers.ValidationError('email cant contain "admin"')
        return value

    # object-level validation
    def validate(self, data: dict):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('password dont match')
        # return validated_data
        return data

    def create(self, validated_data):
        user = Student(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
