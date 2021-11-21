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