from django.urls import path
from . import views


urlpatterns = [
    path('services' , views.ServiceList.as_view() , name='services'),
    path('service/<slug:slug>/', views.ServiceView.as_view(), name='service_detail'),

]
