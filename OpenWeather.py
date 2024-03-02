# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID

from WebAPI import *
from collections import namedtuple

# api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}

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


    def set_apikey(self, apikey: str) -> None:
        """
        Sets the apikey requrired to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        """
        super().set_apikey(apikey)


    # @abstract so is overriden from WebAPI
    def load_data(self) -> None:
        """
        Calls the web api using the required values and stores the response in class data attributes.
        """
        # TODO: use the apikey data attribute and the urllib module to request data from the wbe api. See sample code at the beg of part 1 for a hint
        # TODO: addign the necessary resp data to the requred class data attributes
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
            weather_tuple = WeatherTuple(data["coord"],
                                            data["weather"],
                                            data["base"],
                                            data["main"],
                                            data["visibility"],
                                            data["wind"],
                                            data["rain"],
                                            data["clouds"],
                                            data["dt"],
                                            data["sys"],
                                            data["timezone"],
                                            data["id"],
                                            data["name"],
                                            data["cod"])
            return weather_tuple
        except Exception as ex:
            raise WeatherAPIError(f"Weather data not sorted: {ex}")
        
    def transclude(self):
        pass