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
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import (path, 
                         include, )
from task_23.views import (api_fio, 
                           APIFioAll, 
                           APIFio, 
                           APIFioDetail, 
                           APIFioViewSet, )


router = DefaultRouter()
router.register('fio', APIFioViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('fio_a/', api_fio),
    path('fio_b/', APIFioAll.as_view()),
    path('fio_c/', APIFio.as_view()),

    path('fio_a/<int:pk>', api_fio),
    path('fio_b/<int:pk>', APIFioAll.as_view()),
    path('fio_c/<int:pk>', APIFioDetail.as_view()),

    path('fio_d/', include(router.urls)),
]
