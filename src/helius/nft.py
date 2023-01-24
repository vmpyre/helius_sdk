from typing import List
from config.endpoints import MAINNET_BASE_URL
from helpers.utility import _make_post_request

class NFTAPI:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_BASE_URL
        self.api_key_query = f"?api-key={api_key}"

    def get_nft_events(
        self, 
        accounts: List[str], 
        types: List[str]=None,
        sources: List[str]=None,
        start_slot: int=None,
        end_slot: int=None,
        start_time: int=None,
        end_time: int=None,
        first_verified_creator: List[str]=None,
        verified_collection_address: List[str]=None,
        limit: int=None,
        sort_order: str=None,
        pagination_token: str=None
        ):

        path = "/v1/nft-events"
        url = self.base_url + path + self.api_key_query
        payload = {
            "query": {
                "accounts": accounts,
                "types": types,
                "sources": sources,
                "startSlot": start_slot,
                "endSlot": end_slot,
                "startTime": start_time,
                "endTime": end_time,
                "nftCollectionFilters": {
                    "firstVerifiedCreator": first_verified_creator,
                    "verifiedCollectionAddress": verified_collection_address
                }
            },
            "options": {
                "limit": limit,
                "sortOrder": sort_order,
                "paginationToken": pagination_token
            }
        }
        return _make_post_request(url, payload)

    def get_mintlists(
        self, 
        first_verified_creator: List[str],
        verified_collection_address: List[str]=None,
        limit: int=None,
        pagination_token: str=None
        ):

        path = "/v1/mintlist"
        url = self.base_url + path + self.api_key_query
        payload = {
            "query": {
                "firstVerifiedCreators": first_verified_creator,
                "verifiedCollectionAddress": verified_collection_address
            },
            "options": {
                "limit": limit,
                "paginationToken": pagination_token
            }
        }
        return _make_post_request(url, payload)

    def get_nft_fingerprint(self, mints: List[str]):
        path = "/v1/nfts"
        url = self.base_url + path + self.api_key_query
        payload = {
            "mints": mints
        }
        return _make_post_request(url, payload)

    def get_active_listings(
        self, 
        first_verified_creator: List[str],
        verified_collection_address: List[str]=None,
        marketplaces: List[str]=None,
        limit: int=None,
        pagination_token: str=None
        ):

        path = "/v1/active-listings"
        url = self.base_url + path + self.api_key_query
        payload = {
            "query": {
                "marketplaces": marketplaces,
                "firstVerifiedCreators": first_verified_creator,
                "verifiedCollectionAddress": verified_collection_address
            },
            "options": {
                "limit": limit,
                "paginationToken": pagination_token
            }
        }
        return _make_post_request(url, payload)

    def get_nft_metadata(self, mint_accounts: List[str]):
        path = "/v0/tokens/metadata"
        url = self.base_url + path + self.api_key_query
        payload = {
            "mintAccounts": mint_accounts
        }
        return _make_post_request(url, payload)