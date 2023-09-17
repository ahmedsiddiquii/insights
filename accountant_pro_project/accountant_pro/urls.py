from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', login, name='login'),
path('logout/', logoutt, name='logout'),
path('signup/', signup, name='signup'),
path('company_create/', company_create, name='company_create'),

]