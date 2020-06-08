from django.urls import path
from django.contrib.auth import views as auth_views
from . views import SignupView, LoginView
app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'accounts/login.html'), name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('signup/',SignupView.as_view(), name="signup")
]