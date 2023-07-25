from django.urls import path
from . import views

urlpatterns = [
    # path('home', views.home),
    # path('authorized', views.authorized)
    path('', views.HomeView.as_view(), name="home"),
    path('authorized', views.AuthorizedView.as_view()),
    path('login', views.LoginInterfaceView.as_view(), name='home.login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='home.logout'),
    path('signup', views.SignUpView.as_view(), name='home.signup'),
    
]