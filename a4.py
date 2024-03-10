# a4.py ADAPTED from a3 and old_a4.py

# Alex Reyes Aranda
# areyesar@uci.edu
# 69754988
import ds_protocol as dsp
import ds_client as dsc
from ui import *  # do not have to import Profile.py because its in ui.py
from pathlib import Path

# API imports
from OpenWeather import OpenWeather
from LastFM import LastFM


USERNAME = "melonmusk"
PASSWORD = "XA123"
BIO = ""
# C /Users/alexra/Documents/UCI_WINTER_2023/ICS_32/test_folder -n myjournal
SERVER = "168.235.86.101"
PORT = 3021
CURRENT_FOLDER = Path(".").resolve()
OFFLINE_ONLINE = ("Hello Welcome to my Journaling program.\n" +
                  "Would you like to continue offline(offline)" +
                  " or online(online)?\n")

OPTIONS1 = ("Hello Welcome to Journaling program.\n" +
            "Create or log into existing account(join).\n'Q' to quit.\n")

OPTIONS2 = ("Now that you've created an account or logged in.\n" +
            "Would you like to post(-post) or change bio(-bio)" +
            " or both?\n'Q' to quit.\n")


def convert_online():
    usr_input = input("Would you like to make this information" +
                      " public online(yes or no).\n" +
                      "Saying yes will make everything you" +
                      " type in public: \n").lower()
    while usr_input != "no" and usr_input != "yes":
        print("Incorrect input")
        usr_input = input("Would you like to make this information " +
                          "public online(yes or no): \n").lower()
    return str(usr_input)


def print_profile(n_profile: Profile):
    print("dsuserver" + n_profile.dsuserver)
    print("username" + n_profile.username)
    print("password" + n_profile.password)
    print("bio" + n_profile.bio)


def main():
    zipcode = "92697"
    ccode = "US"
    weather_apikey = "74b398cb32ec1a411463ab90288a8b6a"
    lastfm_api_key = "0356663ee33a0a5d27428b1f63011652"
    artist = "kanye"

    input_1 = print_user_options()
    p_input_1 = parse_inputs(input_1)
    command_input = p_input_1[0]

    user_profile = Profile(dsuserver=None, username=None, password=None)
    profile_loaded_online = False

    while command_input != "Q":
        if command_input == "C":
            directory_input = p_input_1[1]
            directory_input = Path(directory_input)
            subs, extra = p_input_1[2:]
            command_c = command_C(directory_input, subs, extra)
            user_profile.username = command_c[1]
            user_profile.password = command_c[2]
            user_profile.bio = command_c[3]
            user_profile.dsuserver = command_c[4]
            print("Reminder: Everything you type is currently local")

            online_question = convert_online()
            if online_question == "yes":
                profile_loaded_online = True
                print("Reminder: Your profile, bio, " +
                      "and posts will now be public")

            input_2 = print_user_options_2()
            p_input_2 = parse_inputs(input_2)
            command_input_2 = p_input_2[0]
            tup_list = p_input_2[2]
            # replace messages with their transcribed versions
            for i in range(len(tup_list)):
                if tup_list[i][0] == "-addpost":
                    message = tup_list[i][1]
                    if "@weather" in message:
                        open_weather = OpenWeather()
                        open_weather.set_apikey(weather_apikey)
                        open_weather.load_data()
                    # weather api transclusion
                        message = open_weather.transclude(message)
                    if "@lastfm" in message:
                        user_artist = input("Enter the name of an " +
                                            "artist in the LastFM database: ")
                        lastfm = LastFM()
                        lastfm.set_artist(user_artist)
                        lastfm.set_apikey(lastfm_api_key)
                        lastfm.load_data()
                    # LastFM Transcluison
                        message = lastfm.transclude(message)
                    tup_list[i] = (tup_list[i][0], message)

            if profile_loaded_online:
                allows = ["-addpost", "-bio"]
                valid_tups = list(filter(lambda d: d[0] in allows, tup_list))

            if command_input_2 == "E":
                # E edits username, password, and bio
                directory_input = str(directory_input)
                directory_input += "/" + extra + ".dsu"
                directory_input = Path(directory_input)
                editDSU(tup_list, directory_input, user_profile)

                # online publishing aspect
                if profile_loaded_online:
                    dsp.join(server=user_profile.dsuserver,
                             port=PORT,
                             username=user_profile.username,
                             password=user_profile.password)
                    dsp.bio(server=user_profile.dsuserver,
                            port=PORT, username=user_profile.username,
                            password=user_profile.password,
                            bio=user_profile.bio)
                    if len(valid_tups) >= 1:
                        for tup in valid_tups:
                            run_options(user_profile, tup, PORT)
                    else:
                        print("There is nothing to publish online")
            elif command_input_2 == "P":
                print(command_P(tup_list, user_profile))
            else:
                print("There is no profile loaded. Run commands 'C' or 'O.'")
        elif command_input == "O":
            try:
                directory_input = p_input_1[1]
                directory_input = Path(directory_input)
                user_profile = loadDSU(directory_input)
                print("Reminder: Everything you type is currently local")
            except Exception as ex:
                raise DsuProfileError("Error: ", ex)
            online_question = convert_online()
            if online_question == "yes":
                profile_loaded_online = True
                print("Reminder: Your profile, bio," +
                      " and posts will now be public")
            input_2 = print_user_options_2()
            p_input_2 = parse_inputs(input_2)
            command_input_2 = p_input_2[0]
            tup_list = p_input_2[2]

            # replace messages with their transcribed versions
            for i in range(len(tup_list)):
                if tup_list[i][0] == "-addpost":
                    message = tup_list[i][1]
                    if "@weather" in message:
                        open_weather = OpenWeather()
                        open_weather.set_apikey(weather_apikey)
                        open_weather.load_data()
                        # Weather Transclusion
                        message = open_weather.transclude(message)
                    if "@lastfm" in message:
                        user_artist = input("Enter the name of an " +
                                            "artist in the LastFM database: ")
                        lastfm = LastFM()
                        lastfm.set_artist(user_artist)
                        lastfm.set_apikey(lastfm_api_key)
                        lastfm.load_data()
                        # lastfm transclusion
                        message = lastfm.transclude(message)
                    tup_list[i] = (tup_list[i][0], message)
            if profile_loaded_online:
                allows = ["-addpost", "-bio"]
                valid_tups = list(filter(lambda d: d[0] in allows, tup_list))
            if command_input_2 == "E":
                editDSU(tup_list, directory_input, user_profile)
                if profile_loaded_online:
                    dsp.join(server=user_profile.dsuserver,
                             port=PORT,
                             username=user_profile.username,
                             password=user_profile.password)
                    dsp.bio(server=user_profile.dsuserver,
                            port=PORT,
                            username=user_profile.username,
                            password=user_profile.password,
                            bio=user_profile.bio)
                    if len(valid_tups) >= 1:
                        for tup in valid_tups:
                            run_options(user_profile, tup, PORT)
                    else:
                        print("There is nothing to publish online")
            elif command_input_2 == "P":
                print(command_P(tup_list, user_profile))
            else:
                print("There is not profile loaded. Run commands 'C' or 'O.'")
        input_1 = print_user_options()
        p_input_1 = parse_inputs(input_1)
        command_input = p_input_1[0]


if __name__ == "__main__":
    main()
