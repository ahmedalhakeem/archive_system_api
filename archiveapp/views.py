from .models import Department
from .serializers import DepartmentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import APIView
from rest_framework.authtoken.models import Token
from archiveapp.models import User, Department, Section, Documents, Document_Procedures
from archiveapp.serializers import UserSerializer, DepartmentSerializer, SectionSerializer, DocumentSerializer, DocumentProcedureSerializer
from django.shortcuts import get_object_or_404

# Create a new User
class SignUpForm(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# List all Users
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# update a user
class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Retrieve a specific user
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAuthentication(APIView):
    authentication_classes = [SessionAuthentication , BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth)
        }
        return Response(content)
# /list of all Departments

class DepartmentList(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # lookup_field = 'id'
    # permission_classes = [IsAdminUser]
# Create a new Department

class CreateDepartment(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# Retrieve a department
class RetrieveDepartment(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# Update a department
class UpdateDepartment(generics.RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# List All sections
class ListSections(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

# Section Details
class DetailsSection(generics.RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

# Update Sections
class UpdateSection(generics.RetrieveUpdateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

# /LIST/create Documents
class ListDocuments(generics.ListCreateAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer

# Retrieve a document
class DocumentDetails(generics.RetrieveAPIView):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer

# Update a Document
class DocumentUpdate(generics.RetrieveUpdateAPIView):
    queryset= Documents.objects.all()
    serializer_class = DocumentSerializer

# List all Document Procedures
class ListAllDocumentProcedure(generics.ListCreateAPIView):
    queryset = Document_Procedures.objects.all()
    serializer_class = DocumentProcedureSerializer

# Document Procedures details
class DocumentProcedureDetails(generics.RetrieveAPIView):
    queryset = Document_Procedures.objects.all()
    serializer_class = DocumentProcedureSerializer

# Update Document Procedure
class DocumentProcedureUpdate(generics.RetrieveUpdateAPIView):
    queryset = Document_Procedures.objects.all()
    serializer_class = DocumentProcedureSerializer

