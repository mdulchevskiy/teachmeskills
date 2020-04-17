from django.urls import path
from task_21.views import (home_page,
                           add_user,
                           detail_user,
                           delete_user,
                           edit_user, )


urlpatterns = [
    path('', home_page, name='home_page'),
    path('add', add_user, name='add_user'),
    path('detail/<int:user_id>', detail_user, name='detail_user'),
    path('del/<int:user_id>', delete_user, name='delete_user'),
    path('edit/<int:user_id>', edit_user, name='edit_user'),
]
