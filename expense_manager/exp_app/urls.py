from django.urls import path,include
from django.contrib.auth import views as auth_views

from . import views as app_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('signup', app_views.signup, name='signup'),
    path('index',app_views.home,name='home'),               # dashboard view
    path('logout',app_views.logout_view,name='logout'),
    path('accounts/',include('django.contrib.auth.urls'))
]
