import requests
import os

def get_github_stats(username, sort_by="stargazers_count", reverse=False):
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

        # Sort the repositories based on the selected criteria
        repos.sort(key=lambda repo: repo[sort_by], reverse=reverse)

        print(f"GitHub Stats for {username}:")
        print(f"Total Repositories: {len(repos)}")
        print("Repository List:")
        for repo in repos:
            print(f"- {repo['name']}")
            print(f"  - Stars: {repo['stargazers_count']}")
            print(f"  - Forks: {repo['forks_count']}")
            print(f"  - Watchers: {repo['watchers_count']}")
            print(f"  - Last Updated: {repo['updated_at']}")
            print(f"  - Description: {repo['description']}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub: {e}")


if __name__ == "__main__":
    github_username = input("Enter your GitHub username: ")
    sort_criteria = input("Sort by (stargazers_count, forks, watchers, updated): ")
    reverse_sort = input("Reverse sort? (True/False): ").lower() == "true"

    if sort_criteria not in ["stargazers_count", "forks", "watchers", "updated_at"]:
        print("Invalid sorting criteria. Using default: stargazers_count")
        sort_criteria = "stargazers_count"

    get_github_stats(github_username, sort_criteria, reverse_sort)
