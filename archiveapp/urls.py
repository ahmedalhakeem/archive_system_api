from django.urls import path
from . import views


urlpatterns = [
    path('UserAuthentication/', views.UserAuthentication.as_view(), name='UserAuthentication') ,
    path('department_list/', views.DepartmentList.as_view(), name="department_list"),
    path('signup/', views.SignUpForm.as_view(), name="signup"),
    path('userlist/', views.UserList.as_view(), name="userlist"),
    path('user-detail/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('user-update/<int:pk>/', views.UpdateUser.as_view(), name="user-update"),
    path('create-department/', views.CreateDepartment.as_view(), name="create-department"),
    path('retrieve-department/<int:pk>/', views.RetrieveDepartment.as_view(), name="retrieve-department"),
    path('update-department/<int:pk>/', views.UpdateDepartment.as_view(), name="update-department"),
    path('list-create-sections/', views.ListSections.as_view(), name="list-create-sections"),
    path('section-details/<int:pk>/', views.DetailsSection.as_view(), name="section-details"),
    path('section-update/<int:pk>/', views.UpdateSection.as_view(), name="section-update"),
    path('list-document/', views.ListDocuments.as_view(), name="list-documents"),
    path('document-detail/<int:pk>/', views.DocumentDetails.as_view(), name="document-detail"),
    path('document-update/<int:pk>/', views.DocumentUpdate.as_view(), name="document-update"),
    path('list-create-documentprocedure/', views.ListAllDocumentProcedure.as_view(), name="list-create-documentprocedure"),
    path('document-procedure-details/<int:pk>/', views.DocumentProcedureDetails.as_view(), name="document-procedure-details"),
    path('document-procedure-update/<int:pk>/', views.DocumentProcedureUpdate.as_view(), name="document-procedure-update"),







]
