import requests
import os

# Get the token from environment variable
token = os.getenv('STAKE_API_TOKEN')

# Set up the API request
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# Make the API call to get balance
url = 'https://api.stake.com/v1/user/balance'

try:
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        balance = data.get('balance', 'N/A')
        print(f"✅ Your Stake Balance: ${balance}")
        print(f"Full Response: {data}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Message: {response.text}")
        
except Exception as e:
    print(f"❌ Request failed: {e}")
