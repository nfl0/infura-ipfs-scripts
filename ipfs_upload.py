import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Replace with your Infura project ID and secret
INFURA_PROJECT_ID = os.environ.get('INFURA_PROJECT_ID')
INFURA_PROJECT_SECRET = os.environ.get('INFURA_PROJECT_SECRET')

# If project ID or secret not set, log an error message
if INFURA_PROJECT_ID == 'YOUR_INFURA_PROJECT_ID_HERE' or INFURA_PROJECT_SECRET == 'YOUR_INFURA_PROJECT_SECRET_HERE':
    print('Error: Please set the INFURA_PROJECT_ID and INFURA_PROJECT_SECRET variables to your Infura project ID and secret')
else:
    # URL of Infura's IPFS API
    IPFS_API_URL = 'https://ipfs.infura.io:5001/api/v0/add'

    # Path to the file you want to upload
    file_path = './index.html'

    # Open the file and read its contents
    with open(file_path, 'rb') as f:
        file_contents = f.read()

    # Set the headers for the API request
    auth_string = INFURA_PROJECT_ID + ':' + INFURA_PROJECT_SECRET
    auth_string_bytes = auth_string.encode('ascii')
    base64_bytes = base64.b64encode(auth_string_bytes)
    base64_auth_string = base64_bytes.decode('ascii')
    headers = {
        'Authorization': 'Basic ' + base64_auth_string
    }

    # Set the query parameters for the API request
    params = {
        'pin': 'false'
    }

    # Set the files parameter for the API request
    files = {
        'file': file_contents
    }

    # Make the API request to upload the file to IPFS
    response = requests.post(IPFS_API_URL, headers=headers, params=params, files=files)

    try:
        # Attempt to parse the response as JSON
        response_json = response.json()

        # Check if the response contains a hash field
        if 'Hash' in response_json:
            # Log the hash value for the uploaded file
            print(response_json['Hash'])
        else:
            # Log an error message if the response does not contain a hash field
            print('Error: Response does not contain a hash field')
    except ValueError:
        # Log an error message if the response could not be parsed as JSON
        print('Error: Response could not be parsed as JSON')
        print('Response text:', response.text)
