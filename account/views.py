# views.py
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Panel
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator



@ratelimit(key='user', rate='5/m', block=True)
def home(request):
    return render(request,'home.html')

@method_decorator(ratelimit(key='user', rate='5/m', block=True), name='dispatch')
class RegisterUser(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

   
@ratelimit(key='user', rate='5/m', block=True)
def about(request):
    return render(request,'about.html')


# class Panel(ListView):
#     model = Panel
#     template_name = 'registration/panel.html'
#     context_object_name = 'coins'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         price = cg.get_price(ids='bitcoin', vs_currencies='usd', include_24hr_change=True)
#         context['changes'] = price['bitcoin']['usd_24h_change']
#         return context

@ratelimit(key='user', rate='5/m', block=True)
def panel(request):
    model = Panel.objects.all()
    
    bitcoin_price = cg.get_price(ids='bitcoin', vs_currencies='usd', include_24hr_change=True)
    bitcoin = bitcoin_price['bitcoin']['usd_24h_change']

    ethereum_price = cg.get_price(ids='ethereum', vs_currencies='usd', include_24hr_change=True)
    ethereum= ethereum_price['ethereum']['usd_24h_change']


    binancecoin_price = cg.get_price(ids='binancecoin', vs_currencies='usd', include_24hr_change=True)
    binancecoin= binancecoin_price['binancecoin']['usd_24h_change']

    return render(request , 'registration/panel.html' ,{'bitcoin' : bitcoin , 'ethereum': ethereum , 'binancecoin':binancecoin , 'coins': model})
