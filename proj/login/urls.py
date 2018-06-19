
from django.urls import path
from .views import *

urlpatterns = [

    #path('', 'django.contrib.auth.views.login'),
    path('home/', home),
    path('register/', register),
    path('register/success/', register_success),
    #path('accounts/login/', 'django.contrib.auth.views.login'),
    path('logout/', logout_page),

]