import unittest
from playlist import Playlist
from songs import Song


class TestPlaylist(unittest.TestCase):
    def setUp(self):

        self.track_1 = Song(title="Why", artist="BTR",
                            album="Why", length="04:44")
        self.track_2 = Song(title="Forgotten gentleness",
                            artist="BTR", album="Why", length="03:44")
        self.track_3 = Song(title="Kukavica", artist="Ceca",
                            album="Best From Ceca", length="3:54")
        self.my_playlist = Playlist(name="bg rock")

    def test_add_and_remove_songs(self):
        self.my_playlist.add_song(self.track_1)
        self.my_playlist.add_song(self.track_2)

        with self.subTest("Test adding songs one by one"):
            self.assertEqual(self.my_playlist.songs_list,
                             [self.track_1, self.track_2])

        self.my_playlist.remove_song(self.track_1)

        with self.subTest("Test removing song"):
            self.assertEqual(self.my_playlist.songs_list, [self.track_2])

        self.my_playlist.add_songs([self.track_1])

        with self.subTest("Test adding list of songs"):
            self.assertEqual(self.my_playlist.songs_list, [
                             self.track_2, self.track_1])

        with self.subTest("Test total duration of playlist for a few minutes"):
            self.assertEqual(self.my_playlist.total_length(), "0:08:28")

        self.track_3 = Song(title="The old collection", artist="BTR",
                            album="Why", length="1:22:50")
        self.my_playlist.add_song(self.track_3)

        with self.subTest("Test total duration of playlist for longet period"):
            self.assertEqual(self.my_playlist.total_length(), "1:31:18")

    def test_artists(self):
        self.my_playlist.add_songs([self.track_2, self.track_3, self.track_1])

        self.assertDictEqual(self.my_playlist.artists(), {"Ceca": 1, "BTR": 2})

    def test_next_song(self):
        pass


if __name__ == "__main__":
    unittest.main()
