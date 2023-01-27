# WebhooksAPI
## `WebhookAPI.create_webhook()` 
The `create_webhook()` function is a part of the WebhooksAPI class in the SDK. It is used to create a new webhook.

#### Parameters
- `webhook_url` (str): The URL where the webhook will send notifications.
- `transaction_types` (List[str]): A list of transaction types to be monitored by the webhook.
- `account_addresses` (List[str]): A list of addresses associated with the account to be monitored by the webhook.
- `webhook_type` (str): The type of webhook.
- `auth_header` (str, Optional): The value of the Authorization header to be sent in the webhook notification for identification. 

#### Returns
The function returns the created webhook. The returned value is a dictionary containing the following key-value pairs:
```
{​
  "webhookID": "string",​
  "wallet": "string",​
  "webhookURL": "string",​
  "transactionTypes": [​
    "UNKNOWN"​
  ],​
  "accountAddresses": [​
    "string"​
  ],​
  "webhookType": "string",​
  "authHeader": "string"​
​}
```
#### Example usage
```python
from helius import WebhooksAPI
webhooks_api  = WebhooksAPI("api_key")

webhook_url = "https://TestServer.test.repl.co/webhooks"
transaction_types = ["Any"]
account_addresses = ["M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K"]
webhook_type = "raw"
auth_header = "<Optional_AuthHeader>"

webhook = webhooks_api.create_webhook(webhook_url, transaction_types, account_addresses, webhook_type, auth_header)
print(webhook)
```

## `WebhookAPI.get_all_webhooks()` 
The `get_all_webhooks()` function is a part of the WebhooksAPI class in the SDK. It is used to return all existing webhooks.

#### Parameters
*None*

#### Returns
The function returns a list of webhooks. Each item in the list is a dictionary containing the following key-value pairs:
```
[​
  {​
    "webhookID": "string",​
    "wallet": "string",​
    "webhookURL": "string",​
    "transactionTypes": [​
      "UNKNOWN"​
    ],​
    "accountAddresses": [​
      "string"​
    ],​
    "webhookType": "string",​
    "authHeader": "string"​
  }​
​]
```
#### Example usage
```python
from helius import WebhooksAPI
webhooks_api  = WebhooksAPI("api_key")

webhooks = webhooks_api.get_all_webhooks()
print(webhooks)
```

## `WebhookAPI.get_webhook()` 
The `get_webhook()` function is a part of the WebhooksAPI class in the SDK. It is used to return the given webhook.

#### Parameters
- `webhook_id` (str): The id of a webhook you want to edit.

#### Returns
The function returns the given webhook. The returned value is a dictionary containing the following key-value pairs:
```
{​
  "webhookID": "string",​
  "wallet": "string",​
  "webhookURL": "string",​
  "transactionTypes": [​
    "UNKNOWN"​
  ],​
  "accountAddresses": [​
    "string"​
  ],​
  "webhookType": "string",​
  "authHeader": "string"​
​}
```
#### Example usage
```python
from helius import WebhooksAPI
webhooks_api  = WebhooksAPI("api_key")

webhook_id = "EXISTING_WEBHOOK_ID_HERE"

webhook = webhooks_api.get_webhook(webhook_id)
print(webhook)
```

## `WebhookAPI.edit_webhook()` 
The `edit_webhook()` function is a part of the WebhooksAPI class in the SDK. It is used to edit an existing webhook.

#### Parameters
- `webhook_id` (str): The id of a webhook you want to edit.
- `webhook_url` (str): The URL where the webhook will send notifications.
- `transaction_types` (List[str]): A list of transaction types to be monitored by the webhook.
- `account_addresses` (List[str]): A list of addresses associated with the account to be monitored by the webhook.
- `webhook_type` (str): The type of webhook.
- `auth_header` (str, Optional): The value of the Authorization header to be sent in the webhook notification for identification. 

#### Returns
The function returns the edited webhook. The returned value is a dictionary containing the following key-value pairs:
```
{​
  "webhookID": "string",​
  "wallet": "string",​
  "webhookURL": "string",​
  "transactionTypes": [​
    "UNKNOWN"​
  ],​
  "accountAddresses": [​
    "string"​
  ],​
  "webhookType": "string",​
  "authHeader": "string"​
​}
```
#### Example usage
```python
from helius import WebhooksAPI
webhooks_api  = WebhooksAPI("api_key")

webhook_id = "EXISTING_WEBHOOK_ID_HERE"
webhook_url = "https://TestServer.test.repl.co/webhooks"
transaction_types = ["Any"]
account_addresses = ["M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K"]
webhook_type = "raw"
auth_header = "<Optional_AuthHeader>"

webhook = webhooks_api.edit_webhook(webhook_id, webhook_url, transaction_types, account_addresses, webhook_type, auth_header)
print(webhook)
```

## `WebhookAPI.delete_webhook()` 
The `delete_webhook()` function is a part of the WebhooksAPI class in the SDK. It is used to delete an existing webhook.

#### Parameters
- `webhook_id` (str): The id of a webhook you want to delete.

#### Returns
The function returns a 200 response code on success.

#### Example usage
```python
from helius import WebhooksAPI
webhooks_api  = WebhooksAPI("api_key")

webhook_id = "EXISTING_WEBHOOK_ID_HERE"

webhook = webhooks_api.delete_webhook(webhook_id)
```

# NFTAPI
## `NFTAPI.get_nft_events()` 
The `get_nft_events()` function is a part of the NFTAPI class in the SDK. It is used to query historical NFT transactions by type, address, collection, and time.

#### Parameters
- `accounts` (List[str]): List of accounts to find transactions for. Limit of 1000 accounts.
- `types` (List[str], optional): List of types of events to retrieve.
- `sources` (List[str], optional): List of sources of events to retrieve.
- `start_slot` (int, optional): Earliest slot to include in the query (inclusive). Cannot be combined with "start_time".
- `end_slot` (int, optional): Latest slot to include in the query (inclusive). Cannot be combined with "end_time".
- `start_time` (int, optional): Earliest event time (unix seconds). Cannot be combined with "start_slot".
- `end_time` (int, optional): Latest event time (unix seconds). Cannot be combined with "end_slot".
- `first_verified_creator` (List[str], optional): First verified creator of the NFT. Used to reference NFT collections
- `verified_collection_address` (List[str], optional): Verified Metaplex collection address. Does not exist for all NFT collections.
- `limit` (int, optional): Maximum number of items to return. Must be between 1 and 1000. Default is 100.
- `sort_order` (str, optional): Order of the returned results. Must be 'ASC' or 'DESC'. Results are descending by default.
- `pagination_token` (str, optional): Token used for pagination. Provide the token to the API to retrieve the results from the next page. If no token exists, the query has no results remaining.

#### Returns
The function returns NFT events. The returned value is a list containing dictionaries with the following key-value pairs:
```
[​
  {​
    "result": [​
      {​
        "description": "string",​
        "type": "NFT_SALE",​
        "source": "FORM_FUNCTION",​
        "amount": 1000000,​
        "fee": 5000,​
        "feePayer": "8cRrU1NzNpjL3k2BwjW3VixAcX6VFc29KHr4KZg8cs2Y",​
        "signature": "4jzQxVTaJ4Fe4Fct9y1aaT9hmVyEjpCqE2bL8JMnuLZbzHZwaL4kZZvNEZ6bEj6fGmiAdCPjmNQHCf8v994PAgDf",​
        "slot": 148277128,​
        "timestamp": 1656442333,​
        "saleType": "AUCTION",​
        "buyer": "string",​
        "seller": "string",​
        "staker": "string",​
        "nfts": [​
          {​
            "mint": "KG6f4Fa6YxAW8cG2Dhb18DiMn3rQ3rSLa1Eo2FYM4gi",​
            "name": "y00t #2940",​
            "burned": false,​
            "firstVerifiedCreator": "A4FM6h8T5Fmh9z2g3fKUrKfZn6BNFEgByR8QGpdbQhk1",​
            "verifiedCollectionAddress": "4mKSoDDqApmF1DqXvVTSL6tu2zixrSSNjqMxUnwvVzy2"​
          }​
        ],​
        "nativeTransfers": [​
          {​
            "fromUserAccount": "string",​
            "toUserAccount": "string",​
            "amount": 0​
          }​
        ],​
        "tokenTransfers": [​
          {​
            "fromUserAccount": "string",​
            "toUserAccount": "string",​
            "fromTokenAccount": "string",​
            "toTokenAccount": "string",​
            "tokenAmount": 0,​
            "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx"​
          }​
        ]​
      }​
    ],​
    "paginationToken": "V1_162262948_99"​
  }​
​]
```
#### Example usage
```python
from helius import NFTAPI
nft_api  = NFTAPI("api_key")

accounts = ["ACCOUNT_ADDRESS_1"]
nft_events = nft_api.get_nft_events(accounts=accounts)
print(nft_events)
```

## `NFTAPI.get_mintlists()` 
The `get_mintlists()` function is a part of the NFTAPI class in the SDK. It is used to obtain all NFTs for a given NFT collection.

#### Parameters
- `first_verified_creators` (List[str]): First verified creator of the NFT. Used to reference NFT collections
- `verified_collection_addresses` (List[str], optional): Verified Metaplex collection address. Does not exist for all NFT collections.
- `limit` (int, optional): Maximum number of items to return. Must be between 1 and 10,000. Default is 1000.
- `pagination_token` (str, optional): Token used for pagination. Provide the token to the API to retrieve the results from the next page. If no token exists, the query has no results remaining.

#### Returns
The function returns all NFTs for a given NFT collection. The returned value is a list containing dictionaries with the following key-value pairs:
```
[​
  {​
    "result": [​
      {​
        "mint": "KG6f4Fa6YxAW8cG2Dhb18DiMn3rQ3rSLa1Eo2FYM4gi",​
        "name": "y00t #2940"​
      }​
    ],​
    "paginationToken": "V1_162262948_99"​
  }​
​]
```
#### Example usage
```python
from helius import NFTAPI
nft_api  = NFTAPI("api_key")

creator_addresses = ["CREATOR_ADDRESS_1"]
mintlists = nft_api.get_mintlists(first_verified_creator=creator_addresses)
print(mintlists)
```

## `NFTAPI.get_nft_fingerprint()` 
The `get_nft_fingerprint()` function is a part of the NFTAPI class in the SDK. It is used to get information about a list of NFTs.

#### Parameters
- `mints` (List[str]): NFT mint account addresses.

#### Returns
The function returns information about a list of NFTs. The returned value is a list containing dictionaries with the following key-value pairs:
```
[​
  [​
    {​
      "mint": "KG6f4Fa6YxAW8cG2Dhb18DiMn3rQ3rSLa1Eo2FYM4gi",​
      "name": "y00t #2940",​
      "burned": false,​
      "firstVerifiedCreator": "A4FM6h8T5Fmh9z2g3fKUrKfZn6BNFEgByR8QGpdbQhk1",​
      "verifiedCollectionAddress": "4mKSoDDqApmF1DqXvVTSL6tu2zixrSSNjqMxUnwvVzy2",​
      "activeListings": [​
        {​
          "transactionSignature": "27W41DrnxGFJGX7yEGuKBtRb7oMwFdGdPwffBTTeakV8nTQTgWR2hzFKmrt8QnxaMEbw4pS2NoiLmiuB2VfqxVn7",​
          "marketplace": "MAGIC_EDEN",​
          "amount": 1000000,​
          "seller": "3ngLS7Y64DoMAHJ6k6XYh8vo5nSiG66AP1yLvbckfKrc"​
        }​
      ]​
    }​
  ]​
​]
```
#### Example usage
```python
from helius import NFTAPI
nft_api  = NFTAPI("api_key")

mints = ["MINT_ADDRESS_1"]
nft_descriptions = nft_api.get_nft_fingerprint(mints=mints)
print(nft_descriptions)
```

## `NFTAPI.get_active_listings()` 
The `get_active_listings()` function is a part of the NFTAPI class in the SDK. It is used to query for active NFT listings across marketplaces and NFT collections.

#### Parameters
- `first_verified_creators` (List[str]): First verified creator of the NFT. Used to reference NFT collections
- `verified_collection_addresses` (List[str], optional): Verified Metaplex collection address. Does not exist for all NFT collections.
- `marketplaces` (List[str], optional): List of supported marketplaces to retrieve the data for.
- `limit` (int, optional): Maximum number of items to return. Must be between 1 and 10,000. Default is 1000.
- `pagination_token` (str, optional): Token used for pagination. Provide the token to the API to retrieve the results from the next page. If no token exists, the query has no results remaining.

#### Returns
The function returns active NFT listings. The returned value is a list containing dictionaries with the following key-value pairs:
```
[​
  {​
    "result": [​
      {​
        "mint": "KG6f4Fa6YxAW8cG2Dhb18DiMn3rQ3rSLa1Eo2FYM4gi",​
        "name": "y00t #2940",​
        "firstVerifiedCreator": "A4FM6h8T5Fmh9z2g3fKUrKfZn6BNFEgByR8QGpdbQhk1",​
        "verifiedCollectionAddress": "4mKSoDDqApmF1DqXvVTSL6tu2zixrSSNjqMxUnwvVzy2",​
        "activeListings": [​
          {​
            "transactionSignature": "27W41DrnxGFJGX7yEGuKBtRb7oMwFdGdPwffBTTeakV8nTQTgWR2hzFKmrt8QnxaMEbw4pS2NoiLmiuB2VfqxVn7",​
            "marketplace": "MAGIC_EDEN",​
            "amount": 1000000,​
            "seller": "3ngLS7Y64DoMAHJ6k6XYh8vo5nSiG66AP1yLvbckfKrc"​
          }​
        ]​
      }​
    ],​
    "paginationToken": "V1_162262948_99"​
  }​
​]
```
#### Example usage
```python
from helius import NFTAPI
nft_api  = NFTAPI("api_key")

creator_addresses = ["CREATOR_ADDRESS_1"]
active_listings = nft_api.get_active_listings(first_verified_creator=creator_addresses)
print(active_listings)
```

## `NFTAPI.get_nft_metadata()` 
The `get_nft_metadata()` function is a part of the NFTAPI class in the SDK. It is used to return metadata for a list of given NFT mint addresses.

#### Parameters
- `mint_accounts` (List[str]): NFT mint account addresses.

#### Returns
The function returns token metadata (whether NFT or Fungible) for a given token address. The returned value is a list containing dictionaries with the following key-value pairs:
```
[
  {
    "mint": "string",
    "onChainData": {
      "key": "string",
      "mint": "string",
      "updateAuthority": "string",
      "data": {
        "name": "string",
        "symbol": "string",
        "uri": "string",
        "sellerFeeBasisPoints": 0,
        "creators": [
          {
            "address": "string",
            "share": "string",
            "verified": true
          }
        ]
      },
      "tokenStandard": "string",
      "primarySaleHappened": true,
      "isMutable": true,
      "editionNonce": 0,
      "collection": {
        "key": "string",
        "verified": true
      },
      "collectionDetails": {
        "size": 0
      }
    },
    "offChainData": {
      "name": "string",
      "symbol": "string",
      "attributes": [
        {
          "traitType": "string",
          "value": "string"
        }
      ],
      "sellerFeeBasisPoints": 0,
      "image": "string",
      "properties": {
        "category": "string",
        "files": [
          {
            "uri": "string",
            "type": "string"
          }
        ],
        "creators": [
          {
            "address": "string",
            "share": "string"
          }
        ]
      }
    }
  }
]
```
#### Example usage
```python
from helius import NFTAPI
nft_api  = NFTAPI("api_key")

mint_accounts = ["MINT_ADDRESS_1"]
nft_metadata = nft_api.get_nft_metadata(mint_accounts=mint_accounts)
print(nft_metadata)
```

# TransactionsAPI
## `TransactionsAPI.get_raw_transactions()` 
The `get_raw_transactions()` function is a part of the TransactionsAPI class in the SDK. It is used to retrieve an array of raw transactions for the given accounts.

#### Parameters
- `accounts` (List[str]): List of accounts to find transactions for. Limit of 1000 accounts.
- `start_slot` (int, optional): Earliest slot to include in the query (inclusive). Cannot be combined with "start_time".
- `end_slot` (int, optional): Latest slot to include in the query (inclusive). Cannot be combined with "end_time".
- `start_time` (int, optional): Earliest event time (unix seconds). Cannot be combined with "start_slot".
- `end_time` (int, optional): Latest event time (unix seconds). Cannot be combined with "end_slot".
- `limit` (int, optional): Maximum number of items to return. Must be between 1 and 500. Default is 100.
- `sort_order` (str, optional): Order of the returned results. Must be 'ASC' or 'DESC'. Results are descending by default.
- `pagination_token` (str, optional): Token used for pagination. Provide the token to the API to retrieve the results from the next page. If no token exists, the query has no results remaining.

#### Returns
The function returns the raw transactions. The returned value is a dictionary containing the following key-value pairs:
```
{
  "result": [
    {
      "slot": 0,
      "blocktime": 0,
      "transaction": {
        "signatures": [
          "string"
        ],
        "message": {
          "accountKeys": [
            "string"
          ],
          "header": {},
          "recentBlockhash": "string",
          "instructions": [
            {
              "programIdIndex": 0,
              "accounts": [
                0
              ],
              "data": "string"
            }
          ]
        }
      },
      "meta": {
        "err": {},
        "fee": 0,
        "preBalances": [
          0
        ],
        "postBalances": [
          0
        ],
        "preTokenBalances": [
          0
        ],
        "postTokenBalances": [
          0
        ],
        "logMessages": [
          "string"
        ],
        "rewards": [
          {}
        ],
        "loadedAddresses": {}
      }
    }
  ],
  "paginationToken": "V1_162262948_99"
}
```
#### Example usage
```python
from helius import TransactionsAPI
transactions_api  = TransactionsAPI("api_key")

accounts = ["ACCOUNT_ADDRESS_1"]
raw_transactions = transactions_api.get_raw_transactions(accounts=accounts)
print(raw_transactions)
```

## `TransactionsAPI.get_parsed_transactions()` 
The `get_parsed_transactions()` function is part of the TransactionsAPI class in the SDK. It is used to retrieve an array of enriched, human-readable versions of the given transactions.

#### Parameters
- `transactions` (List[str]): List of transaction IDs/signatures to parse for.
- `commitment` (str, optional): How finalized a block must be to be included in the search. If not provided, will default to "finalized" commitment. Note that "processed" level commitment is not supported.

#### Returns
The function returns parsed transaction(s). The returned value is a list containing dictionaries with the following key-value pairs:
```
[​
  {​
    "description": "Human readable interpretation of the transaction",​
    "type": "UNKNOWN",​
    "source": "FORM_FUNCTION",​
    "fee": 5000,​
    "feePayer": "8cRrU1NzNpjL3k2BwjW3VixAcX6VFc29KHr4KZg8cs2Y",​
    "signature": "yy5BT9benHhx8fGCvhcAfTtLEHAtRJ3hRTzVL16bdrTCWm63t2vapfrZQZLJC3RcuagekaXjSs2zUGQvbcto8DK",​
    "slot": 148277128,​
    "timestamp": 1656442333,​
    "nativeTransfers": [​
      {​
        "fromUserAccount": "string",​
        "toUserAccount": "string",​
        "amount": 0​
      }​
    ],​
    "tokenTransfers": [​
      {​
        "fromUserAccount": "string",​
        "toUserAccount": "string",​
        "fromTokenAccount": "string",​
        "toTokenAccount": "string",​
        "tokenAmount": 0,​
        "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx"​
      }​
    ],​
    "accountData": [​
      {​
        "account": "string",​
        "nativeBalanceChange": 0,​
        "tokenBalanceChanges": [​
          {​
            "userAccount": "F54ZGuxyb2gA7vRjzWKLWEMQqCfJxDY1whtqtjdq4CJ",​
            "tokenAccount": "2kvmbRybhrcptDnwyNv6oiFGFEnRVv7MvVyqsxkirgdn",​
            "mint": "DUSTawucrTsGU8hcqRdHDCbuYhCPADMLM2VcCb8VnFnQ",​
            "rawTokenAmount": {​
              "tokenAmount": "string",​
              "decimals": 0​
            }​
          }​
        ]​
      }​
    ],​
    "transactionError": {​
      "error": "string"​
    },​
    "instructions": [​
      {​
        "accounts": [​
          "8uX6yiUuH4UjUb1gMGJAdkXorSuKshqsFGDCFShcK88B"​
        ],​
        "data": "kdL8HQJrbbvQRGXmoadaja1Qvs",​
        "programId": "MEisE1HzehtrDpAAT8PnLHjpSSkRYakotTuJRPjTpo8",​
        "innerInstructions": [​
          {​
            "accounts": [​
              "string"​
            ],​
            "data": "string",​
            "programId": "string"​
          }​
        ]​
      }​
    ],​
    "events": {​
      "nft": {​
        "description": "string",​
        "type": "NFT_SALE",​
        "amount": 1000000,​
        "fee": 5000,​
        "feePayer": "8cRrU1NzNpjL3k2BwjW3VixAcX6VFc29KHr4KZg8cs2Y",​
        "signature": "4jzQxVTaJ4Fe4Fct9y1aaT9hmVyEjpCqE2bL8JMnuLZbzHZwaL4kZZvNEZ6bEj6fGmiAdCPjmNQHCf8v994PAgDf",​
        "slot": 148277128,​
        "timestamp": 1656442333,​
        "saleType": "AUCTION",​
        "buyer": "string",​
        "seller": "string",​
        "staker": "string",​
        "nfts": [​
          {​
            "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx",​
            "tokenStandard": "NonFungible"​
          }​
        ]​
      },​
      "swap": {​
        "nativeInput": {​
          "account": "2uySTNgvGT2kwqpfgLiSgeBLR3wQyye1i1A2iQWoPiFr",​
          "amount": "100000000"​
        },​
        "tokenInputs": [​
          null​
        ],​
        "tokenOutputs": [​
          null​
        ],​
        "tokenFees": [​
          null​
        ],​
        "nativeFees": [​
          null​
        ],​
        "innerSwaps": [​
          {​
            "tokenInputs": [​
              null​
            ],​
            "tokenOutputs": [​
              null​
            ],​
            "tokenFees": [​
              null​
            ],​
            "nativeFees": [​
              null​
            ],​
            "programInfo": {​
              "source": "ORCA",​
              "account": "whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc",​
              "programName": "ORCA_WHIRLPOOLS",​
              "instructionName": "whirlpoolSwap"​
            }​
          }​
        ]​
      }​
    }​
  }​
​]
```
#### Example usage
```python
from helius import TransactionsAPI
transactions_api  = TransactionsAPI("api_key")

transactions = ["<Transaction_ID_Here>"]
parsed_transactions = transactions_api.get_parsed_transactions(transactions=transactions)
print(parsed_transactions)
```

## `TransactionsAPI.get_parsed_transaction_history()` 
The `get_parsed_transaction_history()` function is a part of the TransactionsAPI class in the SDK. It is used to retrieve the enriched transaction history for a given address.

#### Parameters
- `address` (str): The address for which to retrieve transaction history.
- `before` (str, optional): Retrieve transactions that are chronologically before the given transaction ID.
- `until` (str, optional): Retrieve transactions that are chronologically until the given transaction ID.
- `commitment` (str, optional): How finalized a block must be to be included in the search. If not provided, will default to "finalized" commitment. Note that "processed" level commitment is not supported.
- `source` (str, optional): Retrieve transactions that match the given source.
- `type` (str, optional): Retrieve transactions that match the given type.

#### Returns
The function returns the parsed transaction history. The returned value is a list containing dictionaries with the following key-value pairs:
```
[​
  {​
    "description": "Human readable interpretation of the transaction",​
    "type": "UNKNOWN",​
    "source": "FORM_FUNCTION",​
    "fee": 5000,​
    "feePayer": "8cRrU1NzNpjL3k2BwjW3VixAcX6VFc29KHr4KZg8cs2Y",​
    "signature": "yy5BT9benHhx8fGCvhcAfTtLEHAtRJ3hRTzVL16bdrTCWm63t2vapfrZQZLJC3RcuagekaXjSs2zUGQvbcto8DK",​
    "slot": 148277128,​
    "timestamp": 1656442333,​
    "nativeTransfers": [​
      {​
        "fromUserAccount": "string",​
        "toUserAccount": "string",​
        "amount": 0​
      }​
    ],​
    "tokenTransfers": [​
      {​
        "fromUserAccount": "string",​
        "toUserAccount": "string",​
        "fromTokenAccount": "string",​
        "toTokenAccount": "string",​
        "tokenAmount": 0,​
        "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx"​
      }​
    ],​
    "accountData": [​
      {​
        "account": "string",​
        "nativeBalanceChange": 0,​
        "tokenBalanceChanges": [​
          {​
            "userAccount": "F54ZGuxyb2gA7vRjzWKLWEMQqCfJxDY1whtqtjdq4CJ",​
            "tokenAccount": "2kvmbRybhrcptDnwyNv6oiFGFEnRVv7MvVyqsxkirgdn",​
            "mint": "DUSTawucrTsGU8hcqRdHDCbuYhCPADMLM2VcCb8VnFnQ",​
            "rawTokenAmount": {​
              "tokenAmount": "string",​
              "decimals": 0​
            }​
          }​
        ]​
      }​
    ],​
    "transactionError": {​
      "error": "string"​
    },​
    "instructions": [​
      {​
        "accounts": [​
          "8uX6yiUuH4UjUb1gMGJAdkXorSuKshqsFGDCFShcK88B"​
        ],​
        "data": "kdL8HQJrbbvQRGXmoadaja1Qvs",​
        "programId": "MEisE1HzehtrDpAAT8PnLHjpSSkRYakotTuJRPjTpo8",​
        "innerInstructions": [​
          {​
            "accounts": [​
              "string"​
            ],​
            "data": "string",​
            "programId": "string"​
          }​
        ]​
      }​
    ],​
    "events": {​
      "nft": {​
        "description": "string",​
        "type": "NFT_SALE",​
        "amount": 1000000,​
        "fee": 5000,​
        "feePayer": "8cRrU1NzNpjL3k2BwjW3VixAcX6VFc29KHr4KZg8cs2Y",​
        "signature": "4jzQxVTaJ4Fe4Fct9y1aaT9hmVyEjpCqE2bL8JMnuLZbzHZwaL4kZZvNEZ6bEj6fGmiAdCPjmNQHCf8v994PAgDf",​
        "slot": 148277128,​
        "timestamp": 1656442333,​
        "saleType": "AUCTION",​
        "buyer": "string",​
        "seller": "string",​
        "staker": "string",​
        "nfts": [​
          {​
            "mint": "DsfCsbbPH77p6yeLS1i4ag9UA5gP9xWSvdCx72FJjLsx",​
            "tokenStandard": "NonFungible"​
          }​
        ]​
      },​
      "swap": {​
        "nativeInput": {​
          "account": "2uySTNgvGT2kwqpfgLiSgeBLR3wQyye1i1A2iQWoPiFr",​
          "amount": "100000000"​
        },​
        "tokenInputs": [​
          null​
        ],​
        "tokenOutputs": [​
          null​
        ],​
        "tokenFees": [​
          null​
        ],​
        "nativeFees": [​
          null​
        ],​
        "innerSwaps": [​
          {​
            "tokenInputs": [​
              null​
            ],​
            "tokenOutputs": [​
              null​
            ],​
            "tokenFees": [​
              null​
            ],​
            "nativeFees": [​
              null​
            ],​
            "programInfo": {​
              "source": "ORCA",​
              "account": "whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc",​
              "programName": "ORCA_WHIRLPOOLS",​
              "instructionName": "whirlpoolSwap"​
            }​
          }​
        ]​
      }​
    }​
  }​
​]
```
#### Example usage
```python
from helius import TransactionsAPI
transactions_api  = TransactionsAPI("api_key")

parsed_transaction_history = transactions_api.get_parsed_transaction_history(address="<ACCOUNT_ADDRESS_HERE")
print(parsed_transaction_history)
```

# BalancesAPI
## `BalancesAPI.get_balances()` 
The `get_balances()` function is part of the BalancesAPI class in the SDK. It is used to retrieve the balance of a given address.

#### Parameters
- `address` (str): The solana address whose balance is to be retrieved.

#### Returns
The function returns the solana native token balance and balances of all tokens of the given solana address in the form of a dictionary. 
```
{​
  "tokens": [​
    {​
      "mint": "string",​
      "amount": 0,​
      "decimals": 0,​
      "tokenAccount": "string"​
    }​
  ],​
  "nativeBalance": 0​
​}
```
#### Example usage
```python
from helius import BalancesAPI

balances_api = BalancesAPI("api_key")

balances = balances_api.get_balances("solana_wallet_address")
print(balances)
```

# NamesAPI
## `NamesAPI.get_address_name()` 
The `get_address_name()` function is part of the NameAPI class in the SDK. It is used to retrieve the Solana Naming Service domains associated with a given address.

#### Parameters
- `address` (str): The solana address whose domain name is to be retrieved.

#### Returns
The function returns the name associated with the given address. The returned value is of type dict with a list of domainNames. If the address does not have a name, the function will return None.
```
{​
  "domainNames": [​
    "string"​
  ]​
​}
```

#### Example usage
```python
from helius import NameAPI

name_api  = NameAPI("api_key")

name = name_api.get_address_name("solana_wallet_address")
print(name)
```