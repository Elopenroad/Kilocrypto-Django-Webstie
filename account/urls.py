from . import views
from django.urls import path


urlpatterns = [
    path('register/' , views.RegisterUser.as_view() , name='register'),
    path('panel/' , views.panel , name='panel'),
]
