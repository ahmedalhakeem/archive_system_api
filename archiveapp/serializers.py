from rest_framework import serializers
from .models import *
# from rest_framework.authtoken.models import Token



class SignUpSerializer(serializers.ModelSerializer):
    pass
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'section_id']

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'

class DocumentProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model= Document_Procedures
        fields = '__all__'