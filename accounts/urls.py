from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .import views


app_name = 'accounts'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks')
]
