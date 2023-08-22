from django.shortcuts import render, redirect # для того чтобы отдавать html
from django.urls import reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvForm
# Create your views here.

def index(request):
    advertisements: list[Advertisement] = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, 'index.html', context)

def adv_post(request):
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
            print("ошибка")
    else:# get
        form = AdvForm()
        context = {'form' : form}
        return render(request, 'advertisement-post.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def advertisement(request):
    return render(request, 'advertisement.html')