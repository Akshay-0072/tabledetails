from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.empDetails, name='emp'),
    path('teacher', views.teachDetails, name='tech'),
    path('table', views.table, name='table')
]