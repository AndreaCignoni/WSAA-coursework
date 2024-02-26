from github import Github
from config import apikeys as cfg


# Replace these values with your GitHub username, repository name, and access token
username = "AndreaCignoni"
repo_name = "-PyGitHubTest"
apikey = cfg["PyGitHubTest"]

# Create a PyGithub instance using the access token
g = Github(apikey)

# Get the user (you)
user = g.get_user()

# Get the repository
repo = user.get_repo(repo_name)

# Specify the content for the new file
file_content = "This is a test file created using PyGithub created as a sample text. One of its main purposes is containing the word 'Andrew'."

# Create or update the file
try:
    contents = repo.get_contents("test.txt")
    repo.update_file("test.txt", "Updating test.txt", file_content, contents.sha)
    print("File 'test.txt' updated successfully.")
except Exception as e:
    repo.create_file("test.txt", "Creating test.txt", file_content)
    print("File 'test.txt' created successfully.")
