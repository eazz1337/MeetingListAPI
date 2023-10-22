from urllib.request import urlopen
from urllib.error import URLError
from http.client import HTTPResponse

class RequestHandle():

    """
    Request handle class collects methods to operate on URL.
    Exmaple base URL: "https://www.bmltadmin.anonimowinarkomani.org/main_server/ 
    client_interface/{format}/?switcher=GetSearchResults&services={district}&data_field_key={fields}"
    Format option list: csv/json
    District: 
    """

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
    
    def make_url(self, base_url: list[str], format: str, district: str, fields: list[str]):

        field_str = ",".join(fields)

        self.url = "".join([base_url[0], format, base_url[1], district, base_url[2], field_str])
