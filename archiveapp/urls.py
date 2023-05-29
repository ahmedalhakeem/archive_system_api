from django.urls import path
from . import views

urlpatterns = [
    path('department_list/', views.departmenList, name='department_list')
]