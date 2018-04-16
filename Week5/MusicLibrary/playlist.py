from songs import Song
import json



class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
<<<<<<< HEAD
        self.songs_list = []


    def add_song(self, song):
        
        pass

    def add_songs(self, songs):
        pass
=======
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
>>>>>>> bcf41f49f68c7b521138d3b669ab37126c1e7f88

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

    @classmethod
    def save(cls):
        pass

    @staticmethod
    def load():
        pass
