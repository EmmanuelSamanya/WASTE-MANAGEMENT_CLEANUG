from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['role','phone','company_name']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','profile']

class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Profile._meta.get_field('role').choices, write_only=True)
    phone = serializers.CharField(write_only=True, required=False, allow_blank=True)
    company_name = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name','role','phone','company_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role = validated_data.pop('role')
        phone = validated_data.pop('phone', '')
        company_name = validated_data.pop('company_name', '')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, role=role, phone=phone, company_name=company_name)
        return user
