from rest_framework import serializers
from .models import *



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = '__all__'