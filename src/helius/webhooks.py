from config.endpoints import MAINNET_BASE_URL
from helpers.utility import _make_get_request, _make_post_request, _make_put_request, _make_delete_request

class WebhooksAPI:
    def __init__(self, api_key: str):
        self.base_url = MAINNET_BASE_URL
        self.api_key_query = f"?api-key={api_key}"

    def create_webhook(
        self, 
        webhook_url: str, 
        transaction_types: list, 
        account_addresses: list, 
        webhook_type: str, 
        txn_status: str="all",
        auth_header: str=None
        ):
        
        path = "/v0/webhooks"
        url = self.base_url + path + self.api_key_query
        payload = {
            "webhookURL": webhook_url,
            "transactionTypes": transaction_types,
            "accountAddresses": account_addresses,
            "webhookType": webhook_type,
            "txnStatus": txn_status
        }
        if auth_header:
            payload["authHeader"] = auth_header

        return _make_post_request(url, payload)

    def get_all_webhooks(self):
        path = "/v0/webhooks"
        url = self.base_url + path + self.api_key_query

        return _make_get_request(url)

    def get_webhook(self, webhook_id: str):
        path = f"/v0/webhooks/{webhook_id}"
        url = self.base_url + path + self.api_key_query

        return _make_get_request(url)

    def edit_webhook(
        self, 
        webhook_id: str, 
        webhook_url: str, 
        transaction_types: list, 
        account_addresses: list, 
        webhook_type: str, 
        txn_status: str="all",
        auth_header: str=None
        ):

        path = f"/v0/webhooks/{webhook_id}"
        url = self.base_url + path + self.api_key_query
        payload = {
            "webhookURL": webhook_url,
            "transactionTypes": transaction_types,
            "accountAddresses": account_addresses,
            "webhookType": webhook_type,
            "txnStatus": txn_status
        }
    
        if auth_header:
            payload["authHeader"] = auth_header

        return _make_put_request(url, payload)

    def delete_webhook(self, webhook_id: str):
        path = f"/v0/webhooks/{webhook_id}"
        url = self.base_url + path + self.api_key_query
        
        return _make_delete_request(url)
