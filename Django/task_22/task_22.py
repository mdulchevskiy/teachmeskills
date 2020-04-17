# pip install django


# Описать в отдельном файле следующие команды:
# ● Получение всех альбомов группы;
# ● Получение всех треков альбома;
# ● Получение всех треков группы;
# ● Получение всех альбомов, группы которых были основаны в 1990 году.


from task_22.models import (MusicBand,
                            Album, )


def get_band_albums(band_name):
    band = MusicBand.objects.filter(name=band_name).first()
    band_albums = band.albums.all()
    # band_albums = Album.objects.filter(band__name=band_name)
    return band_albums


def get_album_tracks(album_name):
    album = Album.objects.filter(name=album_name).first()
    album_tracks = album.tracks.all()
    # album_tracks = Track.objects.filter(album__name=album_name)
    return album_tracks


def get_band_songs(band_name):
    band = MusicBand.objects.filter(name=band_name).first()
    albums = band.albums.all()
    tracks = [album.tracks.all() for album in albums]
    # tracks = Track.objects.filter(album__band__name=band_name)
    return tracks


def get_albums_bands_90s():
    bands = MusicBand.objects.filter(f_year=1990)
    albums = [band.albums.all() for band in bands]
    # albums = Album.objects.filter(band__f_year=1990)
    return albums
