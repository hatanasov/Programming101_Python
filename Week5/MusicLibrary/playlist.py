from songs import Song

class Playlist:
    def __init(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle


    def add_song(self, song):
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

    def save(self):
        pass

    @staticmethod
    def load():
        pass