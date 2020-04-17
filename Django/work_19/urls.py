from django.urls import path
from work_19.views import (work_19_01,
                           work_19_02,
                           work_19_03,
                           work_19_04,
                           work_19_06, )

urlpatterns = [
    path('w1', work_19_01, name='w1'),
    path('w2', work_19_02, name='w2'),
    path('w3', work_19_03, name='w3'),
    path('w4', work_19_04, name='w4'),
    path('w6', work_19_06, name='w6'),
]
