"""Blood_Bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Donor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home' ),
    path('showDonor/',views.showDonor,name = 'showDonor' ),
    path('reg/',views.reg,name = 'reg' ),
    path('profile/<email>/<password>/',views.profile,name = 'profile' ),
    path('edit/<d_id>/',views.edit,name = 'edit' ),
    path('update/<d_id>/',views.update,name = 'update' ),
    path('login/',views.login,name = 'login' ),
]
