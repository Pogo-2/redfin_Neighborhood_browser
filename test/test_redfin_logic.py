import pytest
from unittest.mock import patch, MagicMock
from src.redfin_core.TimRedfin import TimRedfin


class TestTimRedfin:

    @patch('TimRedfin.Redfin')
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
                    "id": "123456"
                }
            }
        }
        region_id = TimRedfin._parse_region_id(search_response)
        assert region_id == "3456"

    @patch('TimRedfin.Redfin')
    def test_set_region_id(self, mock_redfin):
        mock_client = mock_redfin.return_value
        mock_client.search.return_value = {
            "payload": {
                "exactMatch": {
                    "id": "123456"
                }
            }
        }
        tim_redfin = TimRedfin()
        tim_redfin.set_region_id("Test Neighborhood")
        
        assert tim_redfin.region_id == "3456"
        mock_client.search.assert_called_once_with("Test Neighborhood")

    @patch('requests.Session')
    def test_call_redfin_for_hood_data(self, mock_session):
        mock_session_instance = mock_session.return_value
        mock_session_instance.get.return_value.text = 'response text'
        
        tim_redfin = TimRedfin()
        url = "http://example.com"
        response = tim_redfin._call_redfin_for_hood_data(url)
        
        assert response == 'response text'
        mock_session_instance.get.assert_called_once_with(url)