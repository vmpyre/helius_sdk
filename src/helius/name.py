from config.endpoints import MAINNET_BASE_URL
from helpers.utility import _make_get_request

class NameAPI:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_BASE_URL
        self.api_key_query = f"?api-key={api_key}"

    def get_address_name(self, address: str):
        path = f"/v0/addresses/{address}/names"
        url = self.base_url + path + self.api_key_query
        return _make_get_request(url)