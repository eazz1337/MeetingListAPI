from urllib.request import urlopen
from urllib.error import URLError
from http.client import HTTPResponse

class RequestHandle():

    def __init__(self, url: str = "") -> None:
      self.url = url

    def open_request(self,) -> HTTPResponse:

        try:
            request = urlopen(self.url)

        except ValueError as e_value:
            request = None
            print("Error opening URL:", e_value)

        except URLError as e_url:
            request = None
            print(f"Error opening URL:", e_url.reason)

        return request
