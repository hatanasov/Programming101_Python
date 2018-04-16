class Song:
    def __init__ (self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        result = f"{self.artist} - {self.title} from {self.album} - {self.length}"
        return result

    def __eq__(self, other):
        if self.__hash__() == other.__hash__():
            return True
        return False

    def __hash__(self):
        return f"{self.artist}{self.title}{self.album}{self.length}"


    def get_length(self, seconds=None, minutes=None, hours=None):
        time_list = [int(digit) for digit in self.length.split(':')]
        if len(time_list) == 2:
            time_list.insert(0, 0)
        elif len(time_list) == 1:
            time_list.insert(0, 0), time_list.insert(1, 0)

        if not seconds and not minutes and not hours:
            return self.length
        elif  seconds == True and not minutes and not hours:
            return sum(x * 60 ** i for i, x in enumerate(reversed(time_list)))
        elif minutes == True and not seconds and not hours:
            return sum(x * 60 ** i for i, x in enumerate(reversed(time_list[:2])))
        elif hours == True and not seconds and not minutes:
            return sum(x * 60 ** i for i, x in enumerate(reversed(time_list[:1])))
        else:
            raise TypeError("Only one argument can be True")


