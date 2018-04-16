import unittest
from songs import Song


class TestMusicPlayer(unittest.TestCase):
    def setUp(self):
        self.song = Song(title="Why", artist="BTR", album="Why", length="1:04:44")
        self.same_as_song = Song(title="Why", artist="BTR", album="Why", length="1:04:44")
        self.other_song = Song(title="Kukavica", artist="Ceca", album="Best From Ceca", length="3:54")


    def test_str_representation(self):
        self.assertEqual(str(self.song), f"{self.song.artist} - {self.song.title} from {self.song.album} - {self.song.length}")


    def test_songs_are_equal(self):
        self.assertEqual(self.song, self.same_as_song)


    def test_songs_are_diferent(self):
        self.assertNotEqual(self.song, self.other_song)


    def test_songs_lenght(self):
        song_lenght_in_seconds = 3884
        song_lenght_in_minutes = 64
        song_lenght_in_hours = 1
        song_exact_lenght = "1:04:44"

        with self.subTest("Test lenght of song instance in seconds"):
            self.assertEqual(self.song.get_length(seconds=True), song_lenght_in_seconds)

        with self.subTest("Test lenght of song instance in minutes"):
            self.assertEqual(self.song.get_length(minutes=True), song_lenght_in_minutes)

        with self.subTest("Test lenght of song instance in hours"):
            self.assertEqual(self.song.get_length(hours=True), song_lenght_in_hours)

        with self.subTest("Test lenght of song instance as it is given (string)"):
            self.assertEqual(self.song.get_length(), song_exact_lenght)

        with self.subTest("Test for raise TypeError"):
            with self.assertRaises(TypeError):
                self.song.get_length(seconds=True, hours=True)


    def test_other_song_lenght(self):
        song_lenght_in_seconds = 234
        song_lenght_in_minutes = 3
        song_lenght_in_hours = 0
        song_exact_lenght = "3:54"

        with self.subTest("Test lenght of song instance in seconds"):
            self.assertEqual(self.other_song.get_length(seconds=True), song_lenght_in_seconds)

        with self.subTest("Test lenght of song instance in minutes"):
            self.assertEqual(self.other_song.get_length(minutes=True), song_lenght_in_minutes)

        with self.subTest("Test lenght of song instance in hours"):
            self.assertEqual(self.other_song.get_length(hours=True), song_lenght_in_hours)

        with self.subTest("Test lenght of song instance as it is given (string)"):
            self.assertEqual(self.other_song.get_length(), song_exact_lenght)


if __name__ == "__main__":
    unittest.main()