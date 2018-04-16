import unittest
from playlist import Playlist
from songs import Song


class TestPlaylist(unittest.TestCase):
    def setUp(self):
<<<<<<< HEAD
        self.track_1 = Song(title="Why", artist="BTR", album="Why", length="04:44")
        self.track_2 = Song(title="Forgotten gentleness", artist="BTR", album="Why", length="03:44")
        self.my_playlist = Playlist(name="bg rock")


    def test_add_song(self):
        expected = self.my_playlist.songs_list

        self.assertEqual(self.my_playlist.add_song(self.track_1), [self.track_1])
=======
        self.track_1 = Song(title="Why", artist="BTR",
                            album="Why", length="4:44")
        self.track_2 = Song(title="Forgotten gentleness", artist="BTR",
                            album="Why", length="3:44")
        self.my_favorite = Playlist(name="bg rock")

    def test_add_and_remove_songs(self):
        self.my_favorite.add_song(self.track_1)
        self.my_favorite.add_song(self.track_2)

        with self.subTest("Test adding songs one by one"):
            self.assertEqual(self.my_favorite.songs, [
                             self.track_1, self.track_2])

        self.my_favorite.remove_song(self.track_1)

        with self.subTest("Test removing song"):
            self.assertEqual(self.my_favorite.songs, [self.track_2])

        self.my_favorite.add_songs([self.track_1])

        with self.subTest("Test adding list of songs"):
            self.assertEqual(self.my_favorite.songs, [
                             self.track_2, self.track_1])

        with self.subTest("Test total duration of playlist for a few minutes"):
            self.assertEqual(self.my_favorite.total_length(), "0:08:28")

        self.track_3 = Song(title="The old collection", artist="BTR",
                            album="Why", length="1:22:50")
        self.my_favorite.add_song(self.track_3)

        with self.subTest("Test total duration of playlist for longet period"):
            self.assertEqual(self.my_favorite.total_length(), "1:31:18")
>>>>>>> bcf41f49f68c7b521138d3b669ab37126c1e7f88


if __name__ == "__main__":
    unittest.main()
