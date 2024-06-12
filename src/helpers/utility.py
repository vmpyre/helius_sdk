import requests

def _make_get_request(url, headers=None, params=None):
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f'Error: {response.status_code}: {response.content}')

def _make_post_request(url, payload):
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f'Error: {response.status_code}: {response.content}')

def _make_put_request(url, payload):
    response = requests.put(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f'Error: {response.status_code}: {response.content}')

def _make_delete_request(url):
    response = requests.delete(url)
    # Check if the response contains any content
    if response.status_code == 200:
        try:
            # Try to parse JSON only if there is content
            if response.text.strip():  # Checks if response text is not empty
                return response.json()
            else:
                return None
        except JSONDecodeError:
            raise ValueError("Received unexpected response format from API")
    else:
        response.raise_for_status()  # Handle other HTTP errors
