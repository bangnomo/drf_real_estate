from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender") #Lay field gender tu profile, vi quan he cua profile va user la OneToOne
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ImageField(source="profile.phofile_photo")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    top_seller = serializers.BooleanField(source="profile.top_seller")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="get_full_name") #get_full_name la property cua User duoc tao ra trong models.py

    class Meta:
        model = User
        fields = ['id','username','email', 'first_name','last_name','full_name','gender','phone_number','profile_photo','country','city','top_seller']
    
    def get_first_name(self, obj):
        return obj.first_name.title()
    
    def get_last_name(self,obj):
        return obj.last_name.title()

    '''
    https://www.django-rest-framework.org/api-guide/relations/#custom-relational-fields
    This method takes the target of the field as the value argument, 
    and should return the representation that should be used to serialize the target. 
    The value argument will typically be a model instance.
    '''
    
    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)

        if  instance.is_superuser:
            representation["admin"] = True
        return representation

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta(UserCreateSerializer.Meta): #su dung Meta tu class UserCreateSerializer cua Djoser
        model = User
        fields = ["id","username","email","first_name","last_name","password"]
