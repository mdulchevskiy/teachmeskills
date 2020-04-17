# 22. Создать три модели MusicBand, Album и Track.
# Каждая музыкальная группа может иметь несколько альбомов.
# Каждая группа имеет название, год основания, стиль музыки.
# В каждом альбоме может содержаться несколько треков.  Каждый Альбом содержит название, год выпуска.
# Каждый трек имеет длительность и название.


from django.db import models


class MusicBand(models.Model):
    name = models.CharField(max_length=255, default=None)
    f_year = models.IntegerField()
    style = models.CharField(max_length=255, default=None)

    def __str__(self):
        return f'Band: {self.name}'


class Album(models.Model):
    name = models.CharField(max_length=255, default=None)
    r_year = models.IntegerField()
    band = models.ForeignKey('MusicBand', null=False, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return f'Album: {self.name}-{self.r_year}'


class Track(models.Model):
    name = models.CharField(max_length=255, default=None)
    duration = models.FloatField(default=None)
    album = models.ForeignKey('Album', null=False, on_delete=models.CASCADE, related_name='tracks')

    def __str__(self):
        return f'Track: {self.name}, {self.duration}'
