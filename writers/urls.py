from django.urls import path
from writers import views as writers_views
from django.contrib.auth import views as auth_views

app_name = 'writers'

urlpatterns = [
    path('register/', writers_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(extra_context={'title': 'Login'}, template_name='writers/login.html'),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(extra_context={'title': 'Log Out'}, template_name='writers/logout.html'),
         name='logout'),
    path('', writers_views.dashboard, name='dashboard')
    ]
