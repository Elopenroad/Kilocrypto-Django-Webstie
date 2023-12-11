from django.shortcuts import render
from django.views.generic.list import ListView
from .import models
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit

# Create your views here.


@method_decorator(ratelimit(key='user', rate='5/m', block=True), name='dispatch')
class BlogList(ListView):
    model = models.Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

@method_decorator(ratelimit(key='user', rate='5/m', block=True), name='dispatch')
class BlogDetailView(DetailView):
    model = models.Blog
    template_name = 'blog_details.html'
    context_object_name = 'blog'