from datetime import datetime, timedelta
import requests


def fetch_github_url_repos(days:int, nom_repos:int):
    try:
        days_ago = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&page=1&per_page={1}".format(days_ago, nom_repos)
        repos = requests.get(url)
        return repos
    except requests.exceptions.HTTPError as e:
        return (e.response.text)


def list_languages(repos):
    """
    Input : repos, respone of fetch_github_url_repos(). 
    Output: returns Dict of objects, one object structure: 
        "Python" : {
            "Number of repos": 17:int,
            "List of repos": [
                [
                    "repo_URL",
                    "HTML_URL"
                ],
                [
                    "repo_URL",
                    "HTML_URL"
                ]
            ]
        }
    """
    try:
        repos_dict = repos.json()['items']
        languages = {}

        NO_OF_REPOS = "Number of repos"
        LIST_OF_REPOS = "List of repos"
        URL = "url"
        HTML_URL = "html_url"

        for repo in repos_dict:
            language = repo['language']
            # From inside the languages DICT. Get or create the current repository's language data.
            prevEntry = languages.setdefault(language,
                                            {NO_OF_REPOS: 0,
                                            LIST_OF_REPOS: []})

            languages[language][NO_OF_REPOS] = prevEntry[NO_OF_REPOS] + 1
            languages[language][LIST_OF_REPOS].append({repo[URL], repo[HTML_URL]})
        return languages

    except Exception as e:
        return ({"error message": "{0}".format(str(e))})
