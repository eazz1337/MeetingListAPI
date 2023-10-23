from urllib.request import urlopen
from urllib.error import URLError
from http.client import HTTPResponse

import yaml

from config_handle import Config

class RequestHandle():

    """
    Request handle class collects methods to operate on URL.
    Exmaple base URL: "https://www.bmltadmin.anonimowinarkomani.org/main_server/ 
    client_interface/{format}/?switcher=GetSearchResults&services={district}&data_field_key={fields}"
    Format option list: csv/json/xml
    District option list: 
    """

    def __init__(self, config: Config = None, url: str = "") -> None:

        self.url = url

        if config is not None:
            self.formats = config.formats
            self.districts = config.districts
            self.fields = config.fields

    def open_request(self,) -> HTTPResponse:

        try:
            request = urlopen(self.url)

        except ValueError as e_value:
            request = None
            print("Error opening URL:", e_value)

        except URLError as e_url:
            request = None
            print(f"Error opening URL:", e_url.reason)

        else:
            
            if request.status != 200:
                request == None
            
        return request
    
    def make_url(self, base_url: list[str], format: str, district: str, fields: list[str]):

        field_str = ",".join(fields)

        self.url = "".join([base_url[0], format, base_url[1], str(district), base_url[2], field_str])

if __name__ == "__main__":

    URL = "https://www.bmltadmin.anonimowinarkomani.org/main_server/client_interface/csv/?switcher=GetSearchResults&services=1&data_field_key=weekday_tinyint,start_time,duration_time,meeting_name,location_text,location_info,location_street,location_city_subsection,location_municipality"
    request_handle = RequestHandle(URL)
    print(request_handle.open_request().readlines())
    