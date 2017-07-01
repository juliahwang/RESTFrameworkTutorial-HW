# Create your views here.
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    코드 조각을 모두 보여주거나 새 코드조각을 생성
    :param request: 해당 url에 대한 요청
    :return: 코드 조각 리스트 or 생성
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    코드조각 조회, 업데이트, 삭제
    :param request: 요청
    :param pk: 코드조각의 고유 pk
    :return: 조각을 조회, 업데이트, 삭제할 수 있는 페이지로 렌더
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
