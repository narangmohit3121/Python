class Song(object):
    """
    This class represents a song
    Attributes:
    name (str) : The name of the song
    artist (str) : The artist who created the song
    duratiion (int) : The duration of the song
    """
    def __init__(self, name, artist, duration=0):
        self._name = name
        self._artist = artist
        self._duration = duration

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def artist(self):
        return self._artist

    @artist.setter
    def artist(self, artist):
        self._artist = artist


class Album(object):
    def __init__(self, name, year, artist=None):
        self._name = name
        self._year = year
        if artist is None:
            pass
        else:
            self._artist = artist
        self._tracks = []

    def add_song_to_artist(self, song, position=None):

        if position is None:
            self._tracks.append(song)
        else:
            self._tracks.append(song, position)

    def __get_name__(self):
        return self._name

    def _set_name__(self, name):
        self._name = name
    name = property(__get_name__, _set_name__)

    def __get_year__(self):
        return self._year

    def __set_year__(self, year):
        self._year = year
    year = property(__get_year__, __set_year__)

    def __get_artist__(self):
        return self._artist

    def __set__artist(self, artist):
        self._artist = artist

    artist = property(__get_artist__, __set__artist)

    def __get_tracks__(self):
        return self._tracks

    tracks = property(__get_tracks__)


class Artist(object):
    def __init__(self, name):
        self._name = name
        self._albums = []

    def add_album(self, album):
        self._albums.append(album)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def albums(self):
        return self._albums


def load_data():
    with open('albums.txt', 'r') as albums:
        artists = []
        new_artist = None
        new_album = None
        for line in albums:
            # print(line.strip("\n"))
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            if new_artist is None:
                new_artist = Artist(artist_field)
            elif artist_field != new_artist.name:
                # print(artist_field, new_artist.name, "\n")
                new_artist.add_album(new_album)
                artists.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif album_field != new_album.name:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            new_song = Song(song_field, artist_field)
            new_album.tracks.append(new_song)

        if new_artist not in artists:
            new_artist.add_album(new_album)
            artists.append(new_artist)
        else:
            if new_album not in new_artist.albums:
                new_artist.add_album(album_field)

        print(len(artists))

        return artists


if __name__ == "__main__":
    artist_list = load_data()
    with open('checkFile.txt', 'w') as check_file:
        for current_artist in artist_list:
            for current_album in current_artist.albums:
                # print(current_album)
                for current_track in current_album.tracks:
                    print("{0.name}\t{1.name}\t{2.year}\t{3.name}".
                          format(current_artist, current_album, current_album, current_track),file=check_file)
