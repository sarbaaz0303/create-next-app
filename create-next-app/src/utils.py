import os
import re
import shutil
import requests
from termcolor import colored

def repo_url_valid(repo_url, max_attempts=3):
    """
    Check if the repository URL exists on GitHub.
    
    Args:
        repo_url (str): URL of the repository.
        max_attempts (int, optional): Maximum number of attempts to validate the URL. Defaults to 3.
        
    Returns:
        bool: True if the repository exists, False otherwise.
    """
    attempts = 0
    while attempts < max_attempts:
        try:
            # Extract username and repo
            url = re.sub(r'\.git$', '', repo_url)
            match = re.match(r'^https?://github\.com/([^/]+)/([^/]+)$', url)
            username, repo_name = match.group(1), match.group(2) if match else (None, None)

            if username and repo_name:
                response = requests.get(f"https://api.github.com/repos/{username}/{repo_name}")
                if response.status_code == 200:
                    return repo_url if repo_url.endswith(".git") else f"{repo_url}.git"
            raise Exception('Not Found')
        except Exception as e:
            print("\nRepository URL is not valid. Please try again.")
            attempts += 1
            repo_url = input("Enter the repository URL again: ")
    return False

def perform_clean_operation(path):
    """
    Perform a clean operation on the repository.
    
    Args:
        path (str): Path to the repository.
    """
    # Clean operation implementation
    print(f"\nCleaning repository at {path}")

    # Check if there is a folder with the same name as the path
    folder_name = os.path.basename(path)
    if os.path.exists(path):
        # Remove the folder
        shutil.rmtree(path)
        debug_print(f"Removed existing folder: {colored(folder_name, 'red')}")


