from songs import Song
import json


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs_list = []


    def add_song(self, song):
        
        pass

    def add_songs(self, songs):
        pass

    def remove_song(self, song):
        pass

    def total_length(self):
        pass

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