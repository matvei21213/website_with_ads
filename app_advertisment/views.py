from django.shortcuts import render, redirect # для того чтобы отдавать html
from django.urls import reverse
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvForm
# Create your views here.

def index(request):
    advertisements: list[Advertisement] = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'advertisement/index.html', context)

def adv_post(request:WSGIRequest):
    if request.method == 'POST':
        form = AdvForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            return redirect( # перехожу по ссылке
                reverse('index') # получаю полную ссылку
            )
        else:
            print('ошибка')
    else:# get
        form = AdvForm()
        context = {'form' : form}
        return render(request, 'advertisement/advertisement-post.html', context)

def top_sellers(request):
    return render(request, 'advertisement/top-sellers.html')

def advertisement(request):
    return render(request, 'advertisement/advertisement.html')

def register(request):
    return render(request, 'auth/register.html')
