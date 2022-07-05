from django.urls import path, reverse_lazy
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('sign_up/', views.sign_up , name='users-sign-up'),
    path('profile', views.profile , name='users-profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
    path('password/', auth_view.PasswordChangeView.as_view(
        template_name="users/change-password.html",
        success_url=reverse_lazy('password_change_done'))
        ,name='users-pass-change'),
    path('password_change_done/',auth_view.PasswordChangeDoneView.as_view(
         template_name="users/change-password-done.html",
        ), 
        name='password_change_done')
]

