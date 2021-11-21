from django.http import response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_github_url_repos
from rest_framework.parsers import JSONParser


@parser_classes([JSONParser])
@api_view(['GET'])
def get_github_trending_repos(request):
    if request.method == "GET":
        github_response = fetch_github_url_repos(days=30, nom_repos=100)
        return Response( github_response.json()['items'], status=status.HTTP_200_OK)
    