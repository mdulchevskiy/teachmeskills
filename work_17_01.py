# pip install sqlalchemy


from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///work_17_01_db', echo=False)
Base = declarative_base()


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

    def __repr__(self):
        return f'Album: {self.name}'


def main():
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    artists = session.query(Artist).filter().all()
    if not artists:
        artist1 = Artist(name='Sunflower')
        artist2 = Artist(name='Mushrooms')
        artist3 = Artist(name='Trees')
        album1 = Album(name='Only sun we love', artist=artist1)
        album2 = Album(name='Only moon we love', artist=artist2)
        album3 = Album(name='Only sun we love', artist=artist3)
        session.add_all([
            artist1, artist2, artist3,
            album1, album2, album3,
        ])
        session.commit()
    else:
        artists_albums = session.query(Artist, Album).join(
            Album, Artist.id == Album.artist_id).filter(
            Album.name == 'Only sun we love').all()
        print(artists_albums)


if __name__ == '__main__':
    main()
