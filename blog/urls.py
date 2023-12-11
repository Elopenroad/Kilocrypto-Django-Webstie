from django.urls import path
from . import views


urlpatterns = [
    path('blogs/' , views.BlogList.as_view() , name='blog'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),

]
