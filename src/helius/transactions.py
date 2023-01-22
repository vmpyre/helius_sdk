from typing import List
from config.endpoints import MAINNET_BASE_URL
from helpers.utility import _make_get_request, _make_post_request

class TransactionsAPI:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_BASE_URL
        self.api_key_query = f"?api-key={api_key}"

    def get_raw_transactions(
        self, 
        accounts: List[str], 
        start_slot: int=None,
        end_slot: int=None,
        start_time: int=None,
        end_time: int=None,
        limit: int=None,
        sort_order: str=None,
        pagination_token: str=None
        ):

        path = "/v1/raw-transactions"
        url = self.base_url + path + self.api_key_query
        payload = {
            "query": {
                "accounts": accounts,
                "startSlot": start_slot,
                "endSlot": end_slot,
                "startTime": start_time,
                "endTime": end_time
            },
            "options": {
                "limit": limit,
                "sortOrder": sort_order,
                "paginationToken": pagination_token
            }
        }
        return _make_post_request(url, payload)

    def get_parsed_transactions(self, transactions: List[str], commitment: str=None):
        path = "/v0/transactions"
        if commitment:
            url = self.base_url + path + self.api_key_query + "?commitment=commitment"
        else:
            url = self.base_url + path + self.api_key_query
        payload = {
            "transactions": transactions
        }
        return _make_post_request(url, payload)

    def get_parsed_transaction_history(
        self, 
        address: str, 
        before: str='', 
        until: str='', 
        commitment: str='',
        source: str='',
        type: str=''
        ):
        
        path = f"/v0/addresses/{address}/transactions"
        params = {
            "before": before,
            "until": until,
            "commitment": commitment,
            "source": source,
            "type": type
        }

        url = self.base_url + path + self.api_key_query
        return _make_get_request(url, params=params)