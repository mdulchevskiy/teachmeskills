from django.urls import path
from task_19.views import (task_19_01,
                           task_19_02, )


urlpatterns = [
    path('t1', task_19_01, name='t1'),
    path('t2', task_19_02, name='t2'),
]
