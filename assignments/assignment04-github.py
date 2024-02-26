# This program reads a text file created with my script PyGitHubTest.py in my private repository "PyGitHubTest"
# Replace all the instances of the text "Andrew" with my name "Andrea"
# Commit all changes and push the file back to the "PyGitHubTest" repository
# Author: Andrea Cignoni

from github import Github
from config import apikeys as cfg

def update_file_content(username, repo_name, apikey, file_path, new_content, commit_message):
    # Create a PyGithub instance using the access token
    g = Github(apikey)

    # Get the user (me)
    user = g.get_user()

    # Get the repository
    repo = user.get_repo(repo_name)

    # Get the file from the repository
    file = repo.get_contents(file_path)

    # Read the current content of the file
    file_content = file.decoded_content.decode('utf-8')

    # Replace "Andrew" with "Andrea" in the content
    updated_content = file_content.replace("Andrew", "Andrea")

    # Update the file with the new content
    repo.update_file(file_path, commit_message, updated_content, file.sha)

    print("File updated successfully.")

# Replace these values with your GitHub username, repository name, and access token
username = "AndreaCignoni"
repo_name = "-PyGitHubTest"
apikey = cfg["PyGitHubTest"]

# Specify the file path, new content, and commit message
file_path = "test.txt"
new_content = "This is a test file created using PyGithub created as a sample text. One of its main purposes is containing the word 'Andrew'."
commit_message = "Replace instances of 'Andrew' with 'Andrea'"

# Update the file content and commit changes to the repository
update_file_content(username, repo_name, apikey, file_path, new_content, commit_message)
