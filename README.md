# Helius APIs Python SDK 

Python SDK for interacting with the [Official Helius APIs - https://docs.helius.xyz/api-reference/](https://docs.helius.xyz/api-reference/).

## Installation

### Installing Using PIP (Recommended)
```python
pip install helius
```

### Installing from Source

1. Clone the repository: `git clone https://github.com/vmpyre/helius_sdk.git`

2. Change into the project directory: `cd helius_sdk`

3. Install the dependencies: `pip install -r requirements.txt`

## Usage

First, import the SDK's classes for the APIs you'd like to use. 
```python
>> from helius import NFTAPI, NameAPI, BalancesAPI, WebhooksAPI, TransactionsAPI
```

Then, create instances of the classes to interact with the corresponding API endpoints (in this case the BalancesAPI class):
```python
>> balances_api = BalancesAPI("<API_KEY_HERE>")
```
*Generate your API Key from here: https://docs.helius.xyz/introduction/generate-an-api-key*

For example, you can use the `get_balances()` method of the `BalancesAPI` class to retrieve native Solana balance (in lamports) and all token balances for a given address:
```python
>> balances_api.get_balances("<SOLANA_WALLET_ADDRESS_HERE>")
```
The SDK provides functionality for interacting with the NFTAPI, NameAPI, BalancesAPI, TransactionsAPI and WebhooksAPI endpoints. 
You can view the class methods below:

## Documentation
### WebhooksAPI
- [create_webhook()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#webhookapicreate_webhook)
- [get_all_webhooks()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#webhookapiget_all_webhooks)
- [get_webhook()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#webhookapiget_webhook)
- [edit_webhook()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#webhookapiedit_webhook)
- [delete_webhook()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#webhookapidelete_webhook)

### NFTAPI
- [get_nft_events()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#nftapiget_nft_events)
- [get_mintlists()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#nftapiget_mintlists)
- [get_nft_fingerprint()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#nftapiget_nft_fingerprint)
- [get_active_listings()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#nftapiget_active_listings)
- [get_nft_metadata()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#nftapiget_nft_metadata)

### TransactionsAPI
- [get_raw_transactions()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#transactionsapiget_raw_transactions)
- [get_parsed_transactions()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#transactionsapiget_parsed_transactions)
- [get_parsed_transaction_history()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#transactionsapiget_parsed_transaction_history)

### BalancesAPI
- [get_balances()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#balancesapiget_balances)

### NameAPI
- [get_address_name()](https://github.com/vmpyre/helius_sdk/blob/master/docs/apis.md#namesapiget_address_name)

*See the Official Helius documentation for additional information: https://docs.helius.xyz/api-reference/*

## Contribution
Feel free to open issues, pull requests and submit feedback. We appreciate your help!

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to the Helius team for providing an amazing product.

## Disclaimer
The developer of this SDK is not part of Helius team and this SDK was submitted for the LamportDAO Hackathon. The developer is not responsible for any errors or issues that may occur when using this SDK. Use at your own risk and feel free to report issues.

