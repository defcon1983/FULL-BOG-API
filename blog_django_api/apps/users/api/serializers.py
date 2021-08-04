


from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import authenticate, password_validation
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from apps.users.models import User


class UsersLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('invalid credencials')
        self.context['user'] = user
        return data

    def create(self, validated_data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], Token.key




class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )


class UserSignupSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(min_length=8,max_length=75)
    password_confirmation = serializers.CharField(min_length=8,max_length=75)

    def validate(self, data):
        password = data['password']
        password_conf = data['password_confirmation']

        if password != password_conf:
            raise serializers.ValidationError('los passwords no son identicos')
        password_validation.validate_password(password)

        return data

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user
                        