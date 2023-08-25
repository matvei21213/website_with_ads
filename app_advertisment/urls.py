from django.urls import path
from .views import index, top_sellers, adv_post, advertisement, register

urlpatterns = [
    path('', index, name = 'main-page'),
    path('top-sellers/', top_sellers, name= 'top-sellers'),
    path('adv_post/', adv_post, name= 'adv_post'),
    path('register/', register, name='register'),
    path('advertisement/', advertisement, name='advertisement'),

]
