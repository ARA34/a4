# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# 69754988

# @lastfm

from WebAPI import *
url = "https://ws.audioscrobbler.com/2.0"

API_KEY_2 = "0356663ee33a0a5d27428b1f63011652"

class LastFMAPIError(Exception):
    pass


lastFMTuple = namedtuple("LastFMTuple",["topsong", "playcount"])


class LastFM(WebAPI):
    def __init__(self, artist):
        super().__init__()
        self.artist = artist
        self.top_song = None
        self.playcount = None
        self.keyword = "@lastfm" # displays the number of plays for a particular artist's top song


    def load_data(self) -> None:
        """
        Gets data from API and stores it in data attribute as namedtuple
        """
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={self.artist}&api_key={self.api_key}&format=json"
        try:
            data = self._download_url(url)
            self.data = data
            lastFM_tup = self.sort_FM_data()
            self.top_song = lastFM_tup.topsong
            self.playcount = lastFM_tup.playcount
        except Exception as ex:
            raise LastFMAPIError(f"LastFM data not loaded: {ex}")


    def sort_FM_data(self) -> lastFMTuple:
        """
        Takes the data and sorts it into a tuple to be parsed in load_data
        """
        top_tuple = self.get_top_track()
        fm_tuple = lastFMTuple(top_tuple[0], top_tuple[1])
        return fm_tuple


    def get_top_track(self) -> tuple:
        """
        Returns a tuple of the highest played track by a certain artist
        """
        data = self.data["toptracks"]["track"]
        top_song = None
        try:
            song_entries = list(filter(lambda d: ("name" and "playcount") in d.keys(), data))
            song_names = list(map(lambda d: d["name"], song_entries))
            playcounts = list(map(lambda d: int(d["playcount"]), song_entries))
            songs_counts = list(map(lambda x,y: (x,y), song_names, playcounts))
            top_count = max(playcounts)
            top_song = list(filter(lambda d: d[1] == top_count, songs_counts))[0]
        except Exception as ex:
            raise LastFMAPIError(f"get_top_track unsuccesful: {ex}")
        return top_song


    def transclude(self, message: str) -> str:
        try:
            if self.keyword in message:
                message_list = message.split()
                for m in range(len(message_list)):
                    if message_list[m] == self.keyword:
                        message_list[m] = str(self.playcount)
                output = " ".join(message_list)
            else:
                output = message
            return output
        except Exception as ex:
            if self.artist is None:
                raise LastFMAPIError("There is no artist, please pass an " +
                                     "artist as a parameter in the object", ex)
            raise LastFMAPIError(ex)

