from django.urls import path
from . views import get_github_trending_repos

urlpatterns = [
    path('trending_repos/', get_github_trending_repos, name='get_github_trending_repos'),
]
