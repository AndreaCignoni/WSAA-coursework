import requests
import json
from config import apikeys as cfg

url = "https://api.github.com/repos/AndreaCignoni/aprivateone"

apiKey = cfg['GitHub']

# Getting a response from GitHub API

response = requests.get(url, headers={"Authorization": f"Bearer {apiKey}",
                                      "Accept": "application/vnd.github.v3+json",})
print(response.status_code)

repo_info = response.json()

# More information from my repository

print(f"Repository Name: {repo_info['name']}")
print(f"Owner: {repo_info['owner']['login']}")
print(f"Description: {repo_info['description']}")
print(f"URL: {repo_info['html_url']}")
print(f"Created At: {repo_info['created_at']}")
print(f"Last Updated At: {repo_info['updated_at']}")
print(f"Default Branch: {repo_info['default_branch']}")
print(f"Language: {repo_info['language']}")
print(f"Stars: {repo_info['stargazers_count']}")
print(f"Forks: {repo_info['forks_count']}")
print(f"Watchers: {repo_info['watchers_count']}")

# Create a Json file

filename = 'my-private-repository.json'

with open(filename, 'w') as fp:
    json.dump(repo_info, fp, indent=4)

# Update repository description

new_description = "This is my updated repository description."

update_url = url
update_headers = {
    "Authorization": f"Bearer {apiKey}",
    "Accept": "application/vnd.github.v3+json"
}

update_response = requests.patch(update_url, headers=update_headers, json={"description": new_description})

if update_response.status_code == 200:
    print(f"Repository description updated successfully.")
else:
    print(f"Failed to update repository description. Details: {update_response.text}")

