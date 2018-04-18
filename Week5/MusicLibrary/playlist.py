from songs import Song
import json


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs_list = []

    def add_song(self, song):
        self.songs_list.append(song)

    def add_songs(self, songs):
        self.songs_list += songs

    def remove_song(self, song):
        self.songs_list.remove(song)

    def total_length(self):
        from datetime import timedelta
        total_in_seconds = 0
        for song in self.songs_list:
            total_in_seconds += song.get_length(seconds=True)

        return str(timedelta(seconds=total_in_seconds))

    def artists(self):
        artists = {}
        for song in self.songs_list:
            if song.artist not in artists:
                artists[song.artist] = 1
            else:
                artists[song.artist] += 1
        return artists

    def next_song(self):
        pass

    # def pprint_playlist(self):
    #     pass

    # @classmethod
    # def save(cls):
    #     pass

    # @staticmethod
    # def load():
    #     pass
