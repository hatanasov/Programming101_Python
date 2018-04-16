from songs import Song


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def add_songs(self, songs):
        self.songs += songs

    def total_length(self):
        from datetime import timedelta
        total_in_seconds = 0
        for song in self.songs:
            total_in_seconds += song.get_length(seconds=True)

        return str(timedelta(seconds=total_in_seconds))

    def artists(self):
        pass

    def next_song(self):
        pass

    def pprint_playlist(self):
        pass

    def save(self):
        pass

    @staticmethod
    def load():
        pass
