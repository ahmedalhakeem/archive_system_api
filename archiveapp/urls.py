from django.urls import path
from . import views

urlpatterns = [
    path('department_list/<int:id>/', views.DepartmentList.as_view(), name="department_list")
]