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
from work_24.views import (home_page,
                           get_image,
                           save_image,
                           send_email, )


urlpatterns = [
    path('', home_page, name='home_page'),
    path('get_image/', get_image, name='get_image'),
    path('save/', save_image, name='save_image'),
    path('send_email/', send_email, name='send_email'),
]
