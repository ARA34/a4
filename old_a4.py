# a4.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# STUDENT ID
from OpenWeather import OpenWeather
from LastFM import LastFM


def main():
    zipcode = "92697"
    ccode = "US"
    weather_apikey = "74b398cb32ec1a411463ab90288a8b6a"
    lastfm_api_key = "0356663ee33a0a5d27428b1f63011652"
    artist = "kanye"

    open_weather = OpenWeather(zipcode, ccode)
    open_weather.set_apikey(weather_apikey)
    open_weather.load_data()

    print(open_weather.transclude("wow its so @weather today!"))

    print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
    print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
    print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
    print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
    print(f"The current weather for {zipcode} is {open_weather.description}")
    print(f"The current humidity for {zipcode} is {open_weather.humidity}")
    print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")

    lastfm = LastFM(artist)
    lastfm.set_apikey(lastfm_api_key)
    lastfm.load_data()
    print(lastfm.transclude("my favorite song has @lastfm plays!"))

    print(f"topsong = {lastfm.top_song}, playcount = {lastfm.playcount}")


if __name__ == "__main__":
    main()




