# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# mdulchevskiy -> 1234567890


from django.contrib import admin
from work_22.models import (Group,
                            Student,
                            Diary,
                            Book, )


admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Diary)
admin.site.register(Book)
