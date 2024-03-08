# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Alex Reyes Aranda
# areyesar@uci.edu
# 69754988

import urllib
import json
from urllib import request
from urllib import error
from abc import ABC
from abc import abstractmethod
from collections import namedtuple


class WebAPI(ABC):
    def __init__(self):
        self.api_key = None
        self.data = None
        self.url = None
        self.baseurl = None
        self.keyword = None

    def _download_url(self, url: str) -> dict:
        """
        Requests and returns response from API.
        """
        resp = None
        resp_obj = None
        try:
            resp = urllib.request.urlopen(url)
            json_results = resp.read()
            resp_obj = json.loads(json_results)
        except urllib.error.HTTPError as e:
            print("Failed to download contents of URL")
            print("Status code: {}".format(e.code))
        finally:
            if resp is not None:
                resp.close()
        return resp_obj

    def set_apikey(self, apikey: str) -> None:
        """
        inits given apikey
        """
        self.api_key = apikey

    def set_keyword(self, keyword: str) -> None:
        self.keyword = keyword

    @abstractmethod
    def load_data(self):
        """
        inits data as attribute
        """
        try:
            data = self._download_url(self.url)
            self.data = data
        except Exception as ex:
            print(f"WebAPI data not loaded: {ex}")

    @abstractmethod
    def transclude(self, message: str) -> str:
        """
        replaces keyword with some data
        """
        if self.keyword in message:
            message_list = message.split()
            for m in range(len(message_list)):
                if message_list[m] == self.keyword:
                    message_list[m] = "[Pull this data]"
            output = " ".join(message_list)
        else:
            output = message
        return output
