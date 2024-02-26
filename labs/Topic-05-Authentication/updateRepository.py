import requests
import json
from config import apikeys as cfg

url = "https://api.github.com/repos/AndreaCignoni/aprivateone"
api_key = cfg['GitHub']

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/vnd.github.v3+json"
}

# Fetch current repository information
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repo_info = response.json()

    # Display current description
    print(f"Current Description: {repo_info['description']}")

    # New description
    new_description = "This is my updated repository description."

    # Update the description in the repository_data dictionary
    repo_info['description'] = new_description

    # Perform the update
    update_response = requests.patch(url, headers=headers, json={"description": new_description})

    if update_response.status_code == 200:
        print(f"Repository description updated successfully.")
    else:
        print(f"Failed to update repository description. Status Code: {update_response.status_code}, Details: {update_response.text}")
else:
    print(f"Failed to fetch repository information. Status Code: {response.status_code}, Details: {response.text}")

