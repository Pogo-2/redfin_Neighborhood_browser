import sys
import os
import pytest
from unittest.mock import patch, MagicMock

# Adjust the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.redfin_core.TimRedfin import TimRedfin

# full discloser, I used copilot to generate the test cases below. I just wanted to see how it would do.

class TestTimRedfin:

    @patch('src.redfin_core.TimRedfin.Redfin')
    @patch('os.getenv')
    def test_init(self, mock_getenv, mock_redfin):
        mock_getenv.side_effect = lambda key: 'test_email' if key == 'REDFIN_EMAIL' else 'test_pwd'
        tim_redfin = TimRedfin(verbose=True)
        
        assert tim_redfin.verbose is True
        assert tim_redfin.email == 'test_email'
        assert tim_redfin.pwd == 'test_pwd'
        mock_redfin.assert_called_once()

    def test_parse_region_id(self):
        search_response = {
            "payload": {
                "exactMatch": {
                    "id": "1_3456"
                }
            }
        }
        region_id = TimRedfin()._parse_region_id(search_response)
        assert region_id == 3456

    @patch('src.redfin_core.TimRedfin.Redfin')
    def test_set_region_id(self, mock_redfin):
        mock_client = mock_redfin.return_value
        mock_client.search.return_value = {
            "payload": {
                "exactMatch": {
                    "id": "1_3456"
                }
            }
        }
        tim_redfin = TimRedfin()
        region_id = tim_redfin.set_region_id("Test Neighborhood")
        
        assert tim_redfin.region_id == 3456
        mock_client.search.assert_called_once_with("Test Neighborhood")

    @patch('requests.Session')
    def test_call_redfin_for_hood_data(self, mock_session):
        mock_session_instance = mock_session.return_value
        mock_session_instance.get.return_value.text = 'response text'
        
        tim_redfin = TimRedfin()
        url =f"https://www.redfin.com/stingray/api/gis-csv?al=3&has_deal=false&has_dishwasher=false&has_laundry_facility=false&has_laundry_hookups=false&has_parking=false&has_pool=false&has_short_term_lease=false&include_pending_homes=false&isRentals=false&is_furnished=false&is_income_restricted=false&is_senior_living=false&market=dallas&num_homes=350&ord=redfin-recommended-asc&page_number=1&pool=false&region_id=123&region_type=1&sf=1,2,3,5,6,7&status=9&travel_with_traffic=false&travel_within_region=false&uipt=1,2,3,4,5,6,7,8&utilities_included=false&v=8"

        response = tim_redfin._call_redfin_for_hood_data(url)
        
        print(response.text)
        assert response == 'response text'
        mock_session_instance.get.assert_called_once_with(url)