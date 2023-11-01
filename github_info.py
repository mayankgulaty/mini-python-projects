import requests


def get_github_stats(username):
    # Set your GitHub personal access token as an environment variable
    github_token = "Your Github Token"
    if github_token is None:
        print("Please set your GitHub personal access token as GITHUB_TOKEN environment variable.")
        return

    # GitHub API URL
    api_url = f"https://api.github.com/users/{username}/repos"

    headers = {
        "Authorization": f"token {github_token}"
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        repos = response.json()

        print(f"GitHub Stats for {username}:")
        print(f"Total Repositories: {len(repos)}")
        print("Repository List:")
        for repo in repos:
            print(f"- {repo['name']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub: {e}")


if __name__ == "__main__":
    github_username = input("Enter your GitHub username: ")
    get_github_stats(github_username)
