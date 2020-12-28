"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from first_app.views import home, add_product, \
     edit_product, show_products, register, login_page, logout_fn, edit_user, change_password

urlpatterns = [
    path('', home, name = 'home'),
    path('product/', add_product, name='add_product'),
    path('product/edit/<int:id>/', edit_product),
    path('category/<int:id>/', show_products),
    path('register/', register),
    path('login/', login_page),
    path('logout/', logout_fn),
    path('edit/user/', edit_user),
    path('password/', change_password),




]
