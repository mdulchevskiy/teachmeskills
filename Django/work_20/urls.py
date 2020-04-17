from django.urls import path
from work_20.views import (work_20_01,
                           work_20_02,
                           work_20_03,
                           work_20_04, )


urlpatterns = [
    path('w1', work_20_01, name='w1'),
    path('w2', work_20_02, name='w2'),
    path('w3', work_20_03, name='w3'),
    path('w4', work_20_04, name='w4'),
]
