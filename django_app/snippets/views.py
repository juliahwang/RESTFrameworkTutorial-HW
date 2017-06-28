from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class JSONResponse(HttpResponse):
    """
    콘텐츠를 JSON 타입으로 변환한 후 HttpResponse 형태로 반환
    """
    def __init__(self, data, **kwargs):
        # 매개변수로 받은 data를 JSON 형태로 변환한 후 content에 할당
        content = JSONRenderer().render(data)
        # HttpResponse가 상속받는 HttpResponseBase에 매개변수로 정의되어 있음
        kwargs['content_type'] = 'application/json'
        # ?
        super(JSONResponse, self).__init__(content, **kwargs)


# 인증되지 않은 사용자도 이 뷰에 POST할 수 있도록 데코레이터 사용
@csrf_exempt
def snippet_list(request):
    """
    코드 조각을 모두 보여주거나 새 코드조각을 생성
    :param request: 해당 url에 대한 요청
    :return: 코드 조각 리스트 or 생성
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    코드조각 조회, 업데이트, 삭제
    :param request: 요청
    :param pk: 코드조각의 고유 pk
    :return: 조각을 조회, 업데이트, 삭제할 수 있는 페이지로 렌더
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist as e:
        return HttpResponse(status=404)

    if request.method == "POST":
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)
    elif request.method == "GET":
        data = JSONParser.parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=404)
