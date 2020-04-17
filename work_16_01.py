# pip instal sqlalchemy


from sqlalchemy import create_engine, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker


engine = create_engine('sqlite:///work_16_01_db', echo=True)
Base = declarative_base()

association_table = Table('track_album_association', Base.metadata,
                          Column('album_id', Integer, ForeignKey('album.id')),
                          Column('track_id', Integer, ForeignKey('track.id')),
                          )


class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'Artist: {self.name}'


class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)

    artist = relationship('Artist', foreign_keys='Album.artist_id', backref='albums')


class Booklet(Base):
    __tablename__ = 'booklet'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    album_id = Column(Integer, ForeignKey('album.id'), nullable=False)

    album = relationship('Album', foreign_keys='Booklet.album_id', backref=backref('booklet', uselist=False))


class Track(Base):
    __tablename__ = 'track'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    duration = Column(Float)

    albums = relationship('Album', secondary=association_table, backref='tracks')


def main():
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    artist1 = Artist(name='Imagine Dragons')
    artist2 = Artist(name='Kygo')
    album11 = Album(name='Evolve', artist=artist1)
    album12 = Album(name='Origin', artist=artist1)
    album21 = Album(name='Cloud Nine', artist=artist2)
    album22 = Album(name='Kids In Love', artist=artist2)
    track111 = Track(name='Whatever It Takes', duration=3.2, albums=[album11])
    track121 = Track(name='Bad Liar', duration=2.5, albums=[album12])
    track122 = Track(name='Birds', duration=3.1, albums=[album12])
    track211 = Track(name='Cruise', duration=3.0, albums=[album21, album22])
    track212 = Track(name="It Ain't Me", duration=3.0, albums=[album21, album22])
    track221 = Track(name='Stranger Things', duration=2.4, albums=[album22])
    booklet11 = Booklet(description='Second album', album=album11)
    booklet12 = Booklet(description='Third album', album=album12)
    booklet21 = Booklet(description='First album', album=album21)
    booklet22 = Booklet(description='Second album', album=album22)

    session.add_all([
        artist1, artist2,
        album11, album12, album21, album22,
        track111, track121, track122, track211, track212, track221,
        booklet11, booklet12, booklet21, booklet22,
    ])
    session.commit()


if __name__ == '__main__':
    main()
