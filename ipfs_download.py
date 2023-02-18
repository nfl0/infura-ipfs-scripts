import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Replace with your Infura project ID and secret
INFURA_PROJECT_ID = os.environ.get('INFURA_PROJECT_ID')
INFURA_PROJECT_SECRET = os.environ.get('INFURA_PROJECT_SECRET')

# If project ID or secret not set, log an error message
if INFURA_PROJECT_ID == 'your-project-id-here' or INFURA_PROJECT_SECRET == 'your-project-secret-here':
    print('Error: Please set the INFURA_PROJECT_ID and INFURA_PROJECT_SECRET variables to your Infura project ID and secret')
else:
    # URL of Infura's IPFS API
    IPFS_API_URL = 'https://ipfs.infura.io:5001/api/v0/cat'

    # IPFS hash of the file you want to retrieve
    ipfs_hash = 'QmcWCpksQMXaP7TZYMts3FdsoF3kvJQb2Zw8ayCaFp6Eh4'

    # Set the headers for the API request
    auth_string = f"{INFURA_PROJECT_ID}:{INFURA_PROJECT_SECRET}"
    base64_auth_string = base64.b64encode(auth_string.encode()).decode()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {base64_auth_string}'
    }

    # Set the query parameters for the API request
    params = {
        'arg': ipfs_hash
    }

    # Make the API request to retrieve the file from IPFS
    response = requests.post(IPFS_API_URL, headers=headers, params=params)

    # Log the contents of the file
    print(response.content)
