# Create your views here.
from django.http import Http404
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin,
                  # .list(), .create() 기능을 제공한다.
                  mixins.CreateModelMixin,
                  # 기본 뷰로 핵심기능을 제공한다.
                  generics.GenericAPIView):
    """
    코드 조각을 모두 보여주거나 새 코드조각을 생성
    :param request: 해당 url에 대한 요청
    :return: 코드 조각 리스트 or 생성
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    코드조각 조회, 업데이트, 삭제
    :param request: 요청
    :param pk: 코드조각의 고유 pk
    :return: 조각을 조회, 업데이트, 삭제할 수 있는 페이지로 렌더
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)