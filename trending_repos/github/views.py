from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_github_url_repos, list_languages
from rest_framework.parsers import JSONParser


@parser_classes([JSONParser])
@api_view(['GET'])
def get_github_trending_repos(request):
    try:
        github_response = fetch_github_url_repos(days=30, nom_repos=100)
        languages = list_languages(github_response)
        return Response( languages, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response({"error message": "{0}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
