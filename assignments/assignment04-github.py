# This program reads a text file created with my script PyGitHubTest.py in my private repository "PyGitHubTest"
# Replace all the instances of the text "Andrew" with my name "Andrea"
# Commit all changes and push the file back to the "PyGitHubTest" repository
# Author: Andrea Cignoni

import requests
import base64
from config import apikeys as cfg

def get_file_contents(repo_owner, repo_name, file_path, token):
    # GitHub API endpoint for fetching file contents
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"

    # Headers with authorization token and content type
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Sending GET request to GitHub API to get file details
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract content from the response
        file_content = response.json()["content"]
        # Decode Base64 content to string
        return base64.b64decode(file_content).decode('utf-8')
    else:
        # Print error details if the request fails
        print(f"Failed to fetch file contents. Status Code: {response.status_code}, Details: {response.text}")
        return None

def update_file_contents(repo_owner, repo_name, file_path, token, new_content, commit_message):
    # GitHub API endpoint for updating file contents
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"

    # Headers with authorization token and content type
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Fetch existing file details for commit
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract file details (SHA) for creating a new commit
        file_details = response.json()

        # Encode new content to Base64
        encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')

        # Create a new commit with updated content
        update_data = {
            "message": commit_message,
            "content": encoded_content,
            "sha": file_details["sha"]
        }

        # Sending PUT request to GitHub API to update file
        update_response = requests.put(url, headers=headers, json=update_data)

        # Check if the update request was successful (status code 200)
        if update_response.status_code == 200:
            print("File updated successfully.")
        else:
            print(f"Failed to update file. Status Code: {update_response.status_code}, Details: {update_response.text}")
    else:
        # Print error details if fetching file details fails
        print(f"Failed to fetch file details. Status Code: {response.status_code}, Details: {response.text}")

# Replace "Andrew" with "Andrea" in the text
def replace_text(original_text):
    return original_text.replace("Andrew", "Andrea")

# Main function
def main():
    # GitHub repository details
    repo_owner = "AndreaCignoni"
    repo_name = "-PyGitHubTest"
    file_path = "test.txt"
    
    # GitHub API token stored in the config file
    token = cfg['PyGitHubTest']

    # Commit message for the update
    commit_message = "Replace instances of 'Andrew' with 'Andrea'"

    # Get file contents from the repository
    file_contents = get_file_contents(repo_owner, repo_name, file_path, token)

    if file_contents:
        # Replace text in the file content
        updated_content = replace_text(file_contents)

        # Update file contents and commit changes to the repository
        update_file_contents(repo_owner, repo_name, file_path, token, updated_content, commit_message)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
