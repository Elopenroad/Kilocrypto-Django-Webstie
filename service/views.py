from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Service
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
# Create your views here.


@method_decorator(ratelimit(key='user', rate='5/m', block=True), name='dispatch')
class ServiceList(ListView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'services'

@method_decorator(ratelimit(key='user', rate='5/m', block=True), name='dispatch')
class ServiceView(DetailView):
    model = Service
    template_name = 'service_detail.html'
    context_object_name = 'service'