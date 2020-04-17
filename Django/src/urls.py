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
from django.urls import path
from todo_list.views import (home_page,
                             add_activity,
                             delete_activity,
                             edit_activity,
                             up_activity,
                             down_activity,
                             edit_status,
                             filter_activity,
                             )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('add', add_activity, name='add_activity'),
    path('delete/<int:activity_id>', delete_activity, name='delete_activity'),
    path('edit/<int:activity_id>', edit_activity, name='edit_activity'),
    path('filter', filter_activity, name='filter_activities'),
    path('edit_status/<int:activity_id>', edit_status, name='edit_status'),
    path('up/<int:activity_id>', up_activity, name='up_activity'),
    path('down/<int:activity_id>', down_activity, name='down_activity'),
]
