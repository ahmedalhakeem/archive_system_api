from rest_framework import serializers
from archiveapp.models import User, Department, Section, Documents

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','department_name']