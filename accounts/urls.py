from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('login/', views.login_view, name='login')
    
]