from django.contrib import admin

from task_22.models import (MusicBand,
                            Album,
                            Track, )


admin.site.register(MusicBand)
admin.site.register(Album)
admin.site.register(Track)
