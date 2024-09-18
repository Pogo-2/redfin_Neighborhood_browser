from redfin import Redfin
import os
import requests as req
from src.redfin_core.redfin_utils import get_neighborhood_url
from dotenv import load_dotenv


class TimRedfin:
    """
    This class is a wrapper for the Redfin class that is used to get data from the Redfin API.
    """

    def __init__(self, verbose=False) -> None:
        self.client = Redfin()
        self.verbose = verbose
        load_dotenv()
        self.email = os.getenv("REDFIN_EMAIL")
        self.pwd = os.getenv("REDFIN_PWD")
        self.region_id = None

    @staticmethod
    def _parse_region_id(search_response: dict) -> int:
        """
        Parse the region id from the response.
        """
        breakpoint
        return int(search_response["payload"]["exactMatch"]["id"][2:])


    def set_region_id(self, hood_name: str) -> str:
        """
        Get the region id for a neighborhood.
        Parameters:
        hood_name: str: the name of the neighborhood to get the region id for.
        """

        self.region_id = self._parse_region_id(self.client.search(hood_name))

    def _call_redfin_for_hood_data(self, url: str) -> str:
        """
        Create a session for the Redfin stingray API.
        params:
        url: str: the url to call the redfin stingray api.
        return:
        str: the CSV response from the redfin stingray api
        """
        body = {
            "email": self.email,
            "pwd": self.pwd,
            "authenticationAuthority": "Redfin",
        }
        user_agent_header = {"user-agent": "redfin"}

        with req.Session() as session:
            # first login to get the session cookie
            login = session.post(
                "https://www.redfin.com/stingray/do/api-login",
                headers=user_agent_header,
                data=body,
            )
            raw = session.get(url, headers=user_agent_header)
        return raw.content.decode("utf-8")

 
    def get_hood_data(self):
        """
        Get the data for a neighborhood.
        """
        if self.region_id:
            url = get_neighborhood_url(self.region_id)
            if self.verbose:
                print(f"Getting data from {url}")

            return self._call_redfin_for_hood_data(url)
        else:
            raise ValueError(
                "Region ID not set. use set_region_id() to set the region id."
            )
