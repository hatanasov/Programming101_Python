import unittest
from playlist import Playlist
from songs import Song


class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.track_1 = Song(title="Why", artist="BTR", album="Why", length="04:44")
        self.track_2 = Song(title="Forgotten gentleness", artist="BTR", album="Why", length="03:44")
        self.my_playlist = Playlist(name="bg rock")


    def test_add_song(self):
        expected = self.my_playlist.songs_list

        self.assertEqual(self.my_playlist.add_song(self.track_1), [self.track_1])


if __name__ == "__main__":
    unittest.main()

