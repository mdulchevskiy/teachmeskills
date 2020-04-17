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
from work_23.views import (api_products_1,
                           api_products_2,
                           api_products_fin_ver,
                           api_product,
                           api_product_fin_ver,
                           APIProducts1,
                           APIProducts2,
                           APIProductsDetail1,
                           APIProductsDetail2,
                           APIProductViewSet, )


router = DefaultRouter()
router.register('products', APIProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('products_1/', api_products_1),
    path('products_2/', api_products_2),
    path('products_ver_1/', api_products_fin_ver),
    path('products_class_1/', APIProducts1.as_view()),
    path('products_class_2/', APIProducts2.as_view()),

    path('product/<int:product_id>', api_product),
    path('product_ver_1/<int:product_id>', api_product_fin_ver),
    path('product_class_1/<int:product_id>', APIProductsDetail1.as_view()),
    path('product_class_2/<int:pk>', APIProductsDetail2.as_view()),

    path('api/', include(router.urls))
]
