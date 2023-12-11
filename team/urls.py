from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.TeamList.as_view() , name='team')
]
