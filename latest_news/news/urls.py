from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path("", views.signup, name="signup"),
	path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),

    path("password_reset", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_send.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_confirm"),
    path('password_reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"), 
]
