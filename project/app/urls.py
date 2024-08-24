from django.urls import path
from .views import home,login,login_data

urlpatterns = [
    path('home/',home,name='home'),
    path('login/',login,name='login'),
    path('login_data/',login_data,name='login_data')
    
]
