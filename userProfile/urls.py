from django.urls import path
from .import views

urlpatterns = [
    path("signup/", views.usercreate, name="signup"),
    path("login/", views.userlogin, name="login"),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('logout/', views.handleLogout, name='logout'),
    path('changepass/', views.user_change_pass, name='changepass'),
]