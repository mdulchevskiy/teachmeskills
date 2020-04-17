"""src URL Configuration

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
from django.urls import path
from shortener.views import (shorten_url,
                             delete_short_url,
                             redirect_short_url, )


urlpatterns = [
    path('', shorten_url, name='home_page'),
    path('<str:short_url>', redirect_short_url, name='redirect_url'),
    path('delete/<str:url_id>', delete_short_url, name='delete_url'),
]
