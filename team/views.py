from django.shortcuts import render , redirect
from django.views.generic.list import ListView
from . import models
from django.contrib import messages
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
# Create your views here.


@method_decorator(ratelimit(key='user', rate='5/m', block=True), name='dispatch')
class TeamList(ListView):
    model = models.Team
    template_name = 'team.html'
    context_object_name = 'team'

