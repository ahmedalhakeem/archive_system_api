from django.urls import path
from archiveapp import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('department_list/', views.department_list),
    path('department_create/', views.department_create)
]
urlpatterns = format_suffix_patterns(urlpatterns)