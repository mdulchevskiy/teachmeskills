from django.urls import path
from work_21.views import (home_page,
                           add_customer, )


urlpatterns = [
    path('', home_page, name='home_page'),
    path('add', add_customer, name='add_customer'),
]
