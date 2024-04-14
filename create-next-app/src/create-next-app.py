import os
import re
import sys
import shutil
import requests
import argparse
from termcolor import colored

def main(path, repo_url, clean=False, debug=False):
    """
    Main function to perform tasks based on command-line parameters.
    
    Args:
        path (str): Path to the repository.
        repo_url (str): URL of the repository.
        clean (bool, optional): Whether to perform a clean operation. Defaults to False.
        debug (bool, optional): Whether to enable debugging. Defaults to False.
    """
    # Perform tasks based on the parameters
    if debug:
        debug_print(colored("\nDebugging enabled.", "yellow"))
    
    # Check if the path is provided, if not, ask for user input
    if not path:
        path = input("Enter the path to the repository: ")

    # Get the absolute path and display it to the user
    path = os.path.abspath(path)
    
    # Confirm the path with the user
    confirm_path = input(f"\nConfirm repository path [{path}] \n(Press Enter/Y to confirm, any other key to exit): ")
    if confirm_path.lower() not in ['', 'y']:
        sys.exit()

    print(f"\nSelected repository path: {colored(path, 'green')}")
    if not os.path.exists(path):
        os.mkdir(path)

    # Check if the repository URL exists on GitHub
    repo_url = repo_url_valid(repo_url) or 'https://github.com/sarbaaz0303/create-next-app.git'
    if not repo_url:
        print("Repository URL does not exist on GitHub.")
        sys.exit()
    
    print(f"\nSelected repository URL: {colored(repo_url, 'green')}")
            
    if clean:
        perform_clean_operation(path)

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


def debug_print(msg):
    # Check if debug is enabled
    if debug:
        print(msg)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Create Next App")
    parser.add_argument("path", nargs="?", help="Path to the repository")
    parser.add_argument("repo_url", nargs="?", help="URL of the repository")
    parser.add_argument("clean", nargs="?", type=bool, default=False, help="Perform a clean operation on the repository")
    parser.add_argument("debug", nargs="?", type=bool, default=False, help="Enable debugging")
    args = parser.parse_args()

    # Call main function
    path, repo_url, clean, debug = (args.path, args.repo_url, args.clean, args.debug)
    main(path, repo_url, clean, debug)