from rest_framework import serializers

from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'age' )

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 255, write_only = True
    )        
    password2 = serializers.CharField(
        max_length = 255, write_only = True
    )  
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'age', 'password', 'password2')

    def validate(self, attrs):
        if ['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "пароли отличается"})
        if '+996' not in attrs ['phone_number']:
            raise serializers.ValidationError({'phone_number':"Напишите номер с +996"})
        return attrs

    def create(self, values):
        user = User.objects.create(
            username = values['username'], email = values['email'],
            phone_number = values['phone_number'], age = values['age']
        )
        user.set_password(values['password'])
        user.save()
        return user    