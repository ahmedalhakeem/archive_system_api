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
from archiveapp.serializers import UserSerializer, DepartmentSerializer, SectionSerializer, DocumentSerializer, DocumentProcedureSerializer, LoginSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

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
    # authentication_classes = [SessionAuthentication , BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    def get(self, request, format=None):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                
                user = authenticate(username=username, password=password)
                if user is None:
                    return Response({
                        'status': 400,
                        'message': 'Invalid users',
                        'data': serializer.errors
                    })
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access' : str(refresh.access_token),
                })
        except Exception as e:
            print(e)
            # return Response({'message': e})
            
        # content = {
        #     'user': str(request.user),
        #     'auth': str(request.auth)
        # }
        # return Response(content)
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

