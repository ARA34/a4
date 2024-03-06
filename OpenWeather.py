# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# 69754988

from WebAPI import *

# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}
# @weather

class WeatherAPIError(Exception):
    pass


WeatherTuple = namedtuple("WeatherTuple", ["coord",
                                           "weather",
                                           "base",
                                           "main",
                                           "visibility",
                                           "wind",
                                           "rain",
                                           "clouds",
                                           "dt",
                                           "sys",
                                           "timezone",
                                           "id",
                                           "name",
                                           "cod"])


class OpenWeather(WebAPI):
    def __init__(self, zipcode, city):
        super().__init__() # handles apikey, url, data

        # location
        self.zipcode = zipcode
        self.city = city
        self.keyword = "@weather" # displays desceription of weather

        # weather
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.humidity = None

        # miscs
        self.sunset = None
        self.latitude = None
        self.longitude = None
        self.description = None


    # @abstract so is overriden from WebAPI
    def load_data(self) -> None:
        """
        Calls the web api using the required values and stores the response in class data attributes.
        """
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.city}&appid={self.api_key}"
        try:
            data = self._download_url(url)
            self.data = data
            weather_tuple = self.sort_weather_data()

            self.temperature = weather_tuple.main["temp"]
            self.high_temperature = weather_tuple.main["temp_max"]
            self.low_temperature = weather_tuple.main["temp_min"]
            self.humidity = weather_tuple.main["humidity"]

            self.sunset = weather_tuple.sys["sunset"]
            self.latitude = weather_tuple.coord["lat"]
            self.longitude = weather_tuple.coord["lon"]
            description = ""
            for dict in weather_tuple.weather:
                description += dict["description"] + " with "
            description = description[:-6]
            self.description = description
        except Exception as ex:
            raise WeatherAPIError(f"Weather data not loaded: {ex}")


    def sort_weather_data(self) -> WeatherTuple:
        """
        Sorts json_object with weather data into WeatherTuple namedtuple
        """
        try:
            data = self.data
            if not "rain" in data.keys():
                rain = None
            else:
                rain = data["rain"]
            if not "clouds" in data.keys():
                clouds = None
            else:
                clouds = data["clouds"]
            weather_tuple = WeatherTuple(data["coord"],
                                            data["weather"],
                                            data["base"],
                                            data["main"],
                                            data["visibility"],
                                            data["wind"],
                                            rain,
                                            clouds,
                                            data["dt"],
                                            data["sys"],
                                            data["timezone"],
                                            data["id"],
                                            data["name"],
                                            data["cod"])
            return weather_tuple
        except Exception as ex:
            raise WeatherAPIError(f"Weather data not sorted: {ex}")


    def transclude(self, message: str) -> str:
        try:
            if self.keyword in message:
                message_list = message.split()
                for m in range(len(message_list)):
                    if message_list[m] == self.keyword:
                        message_list[m] = self.description
                output = " ".join(message_list)
            else:
                output = message
            return output
        except Exception as ex:
            raise WeatherAPIError("There was an error "+
                                  "transcluding: ", ex)

