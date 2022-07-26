"""hfo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main.views import AddDonationView, ConfirmView, LandingPageView, LoginView, LogoutView, RegisterView, SettingsUserView, UserView, ShowMyDonationsView
from main.views import get_institutions_by_id
urlpatterns = [  
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="donations-for-the-organizations"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="log-out"),
    path('userview/', UserView.as_view(), name="user-view"),
    path('setting/', SettingsUserView.as_view(), name="setting-user"),
    path('adddonation/', AddDonationView.as_view(), name="add-donation"),
    path('donationconfirm/', ConfirmView.as_view(), name="confirm"),
    path('showmydonations/', ShowMyDonationsView.as_view(), name="show-my-donations"),
    #path for REST API:
    path('get_inst_by_id/', get_institutions_by_id, name='get-ins-by-type'),
]

  
