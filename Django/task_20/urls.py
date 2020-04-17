from django.urls import path
from task_20.views import task_20


urlpatterns = [
    path('aviasales', task_20, name='aviasales'),
]
